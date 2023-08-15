import requests
import psycopg2
import json
import os
from dotenv import load_dotenv
import time

# Load constants from .env file
load_dotenv()

API_URL = os.getenv("API_URL")
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
}

# Class for extracting data from the API
class DataExtractor:
    def __init__(self, api_url):
        self.api_url = api_url
        self.state_file = "extractor_state.json"

    def extract_data(self, page=1):
        try:
            response = requests.get(self.api_url, params={
                                    "$top": 100, "$skip": (page - 1) * 100})
            return response.json()
        except requests.RequestException as e:
            print("Error during API request:", e)
            return []

# Function to transform raw data
def transform_data(raw_data):
    source = raw_data.get('@odata.context')

    def transform_entry(entry):
        return {
            "code": entry.get("Code", "N/A"),
            "title": entry.get("Title", "N/A"),
            "source": source or '',
        }
    return [transform_entry(entry) for entry in raw_data.get('value', [])]

# Function to validate transformed data
def validate_data(data):
    return [
        _data for _data in data if all(
            isinstance(_data.get(key), str) for key in ["code", "title", "source"]
        )
    ]

# Class for loading data into the database
class DataLoader:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def load_data(self, data):
        try:
            insert_query = """
            INSERT INTO public.health_data (code, title, source)
            VALUES (%s, %s, %s);
            """

            for entry in data:
                self.cursor.execute(
                    insert_query,
                    (entry["code"], entry["title"], entry["source"])
                )

            self.conn.commit()
            print("Data loaded successfully.")
        except Exception as e:
            print("Error during data loading:", e)
        finally:
            self.cursor.close()
            self.conn.close()

# Main function that executes the ETL process
def main():
    try:
        extractor = DataExtractor(API_URL)

        # Resume extraction from saved state or start fresh
        if os.path.exists(extractor.state_file):
            with open(extractor.state_file, "r") as state_file:
                state = json.load(state_file)
            page = state.get("page", 1)
        else:
            page = 1

        while True:
            raw_data = extractor.extract_data(page)

            if not raw_data:
                break

            transformed_data = transform_data(raw_data)
            validated_data = validate_data(transformed_data)

            # Connect to the database
            conn = psycopg2.connect(
                dbname=DB_CONFIG["dbname"],
                user=DB_CONFIG["user"],
                password=DB_CONFIG["password"],
                host=DB_CONFIG["host"]
            )
            cursor = conn.cursor()

            # Create table if not exists
            create_table_query = """
                CREATE TABLE IF NOT EXISTS public.health_data (
                    id SERIAL PRIMARY KEY,
                    code VARCHAR(255),
                    title VARCHAR(255),
                    source VARCHAR(255)
                );
            """
            cursor.execute(create_table_query)
            conn.commit()
            print("Table 'health_data' created or already exists.")

            # Load data into the database
            loader = DataLoader(conn, cursor)
            loader.load_data(validated_data)
            print(f"Data from page {page} loaded successfully.")

            # Update state and introduce a delay before next API request
            page += 1
            state = {"page": page}
            with open(extractor.state_file, "w") as state_file:
                json.dump(state, state_file)

            time.sleep(1)  # Pause to avoid overwhelming the API source

        print("All data has been successfully saved to the database.")

        conn.close()
    except Exception as e:
        print("An error occurred during ETL process:", e)


# Entry point of the script
if __name__ == "__main__":
    main()

# etl-pipeline-application

etl-pipeline-application implements an ETL (Extract, Transform, Load) pipeline for processing health-related data from an external API `https://ghoapi.azureedge.net/api/Dimension` and storing it in a PostgreSQL database.

# etl-pipeline-application Overview

- In this Python script application, I've designed an ETL (Extract, Transform, Load) process to efficiently retrieve, transform, and store health-related data from a RESTful API into a PostgreSQL database.
To maintain security, sensitive data such as API URLs and database credentials are loaded from a .env file using the dotenv library. The script employs the requests library to extract paginated data from the API,
which is then transformed into a standardized format using the transform_data function. Validation of essential fields in the transformed data is ensured by the validate_data function. For the loading phase,
the script establishes a connection to the database using psycopg2, creates a table (if it doesn't exist), and then inserts validated data into it. The main function orchestrates these steps,
including resuming extraction from a saved state. Delays between API requests prevent overwhelming the API. The script incorporates error handling to address issues during the ETL process,
 enhancing robustness and data reliability.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)

## Introduction

The ETL pipeline script extracts data from an external API, transforms it into a suitable format, validates the data, and loads it into a PostgreSQL database table. The pipeline is designed to handle large datasets and supports resuming the extraction process from the last saved state.

## Prerequisites

- Python 3.x
- PostgreSQL database
- API accessURL
- [dotenv](https://pypi.org/project/python-dotenv/) package (`pip install python-dotenv`)

## Installation

1. Clone the repository.
2. Install the required packages by running: `pip install -r requirements.txt`

## Configuration

1. Create a `.env` file in the same directory as the script.
2. Add the following environment variables to the `.env` file:

   ```ini
   API_URL=<Your_API_URL>
   DB_NAME=<Your_DB_Name>
   DB_USER=<Your_DB_User>
   DB_PASSWORD=<Your_DB_Password>
   DB_HOST=<Your_DB_Host>


## Usage
- Run the script using the following command:
- `python gho_etl.py``

- Run the test by running the following command
- python `test_etl.py``

## Developer
- Bongomin Daniel

## Screen Shoots
- running Program
<img width="1439" alt="Screenshot 2023-08-16 at 8 40 20 AM" src="https://github.com/bongomin/etl-pipeline-application/assets/39218838/f88c691f-d7c8-47fc-817c-45402955be9e">

- Data Saved in the Database
<img width="1272" alt="Screenshot 2023-08-16 at 8 39 50 AM" src="https://github.com/bongomin/etl-pipeline-application/assets/39218838/842ab628-2e77-4800-b559-65afa0df83a7">


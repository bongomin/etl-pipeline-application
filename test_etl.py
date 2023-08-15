import unittest
from gho_etl import transform_data

# Test class for the transform_data function
class TestTransformData(unittest.TestCase):
    def test_transform_data(self):
        # Sample raw data from the API
        raw_data = {
            "@odata.context": "https://api.example.com/odata",
            "value": [
                {"Code": "D123", "Title": "COVID-19 Cases", "Category": "Disease"},
                {"Code": "I456", "Title": "Population", "Category": "Demographics"}
            ]
        }

        # Expected transformed data
        expected_result = [
            {"code": "D123", "title": "COVID-19 Cases",
                "source": "https://api.example.com/odata"},
            {"code": "I456", "title": "Population",
                "source": "https://api.example.com/odata"}
        ]

        # Call the transform_data function
        transformed_data = transform_data(raw_data)

        # Compare the transformed data with the expected result
        self.assertEqual(transformed_data, expected_result)


# Entry point for running the tests
if __name__ == "__main__":
    unittest.main()

# etl-pipeline-application

etl-pipeline-application implements an ETL (Extract, Transform, Load) pipeline for processing health-related data from an external API `https://ghoapi.azureedge.net/api/Dimension` and storing it in a PostgreSQL database.

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
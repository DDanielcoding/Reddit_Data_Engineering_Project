# Data Pipeline project with Reddit Data

This project offers a robust ETL (Extract, Transform, Load) pipeline designed to process Reddit data and load it into an Amazon Redshift data warehouse. The solution utilizes a suite of tools and services, including Apache Airflow for workflow management, Celery for task scheduling, PostgreSQL for data handling, Amazon S3 for storage, AWS Glue for data transformation, Amazon Athena for querying, and Amazon Redshift for data warehousing.

# Overview:

The pipeline is designed to:

- Extract data from Reddit using its API.
- Orchestrate ETL processes with Apache Airflow and Celery.
- Store the raw data into an S3 bucket from Airflow.
- Transform the data using AWS Glue and Amazon Athena.
- Load the transformed data into Amazon Redshift for analytics and querying.


# Architecture


![architecture](https://github.com/DDanielcoding/Reddit_Data_Engineering_Project/assets/155651525/a0679747-010b-47ef-a33b-21c353202e8e)


- **Reddit API**: Serves as the data source.
- **Apache Airflow & Celery**: Orchestrate the ETL process and manage task distribution.
- **PostgreSQL**: Used for temporary storage and metadata management.
- **Amazon S3**: Stores raw data.
- **AWS Glue**: Handles data cataloging and ETL jobs.
- **Amazon Athena**: Performs SQL-based data transformations.
- **Amazon Redshift**: Facilitates data warehousing and analytics.

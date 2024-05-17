# Data Pipeline with Reddit data using, Apache-Airflow, Celery, S3, AWS Glue, Athena, Postgres, Redshift

This project offers a robust ETL (Extract, Transform, Load) pipeline designed to process Reddit data and load it into an Amazon Redshift data warehouse. The solution utilizes a suite of tools and services, including Apache Airflow for workflow management, Celery for task scheduling, PostgreSQL for data handling, Amazon S3 for storage, AWS Glue for data transformation, Amazon Athena for querying, and Amazon Redshift for data warehousing.

# Overview:

The pipeline is designed to:

Extract data from Reddit using its API.
Orchestrate ETL processes with Apache Airflow and Celery.
Store the raw data into an S3 bucket from Airflow.
Transform the data using AWS Glue and Amazon Athena.
Load the transformed data into Amazon Redshift for analytics and querying.


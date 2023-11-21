# Cryptocurrency_Incremental_pipeline_AWS
This project focuses on cryptocurrency data analytics, leveraging AWS technologies to create a scalable, serverless ETL pipeline. We will extract data from Alpha Vantage, transform it using AWS Lambda, and load it into DynamoDB. Further analytics will be performed using Apache Flink, Apache Zeppelin, and Amazon Athena.
Incremental ETL Pipeline for Cryptocurrency Data using AWS CDK
What Will You Learn?
Understanding the Cryptocurrency Dataset
Grasp the basics of cryptocurrency and its market data.
Explore how digital currencies like Bitcoin use cryptography for secure transactions.
Understanding the Alpha Vantage API
Learn to interact with Alpha Vantage's API for financial data.
Fetch real-time and historical cryptocurrency market data.
Understanding the AWS CDK
Understand the AWS Cloud Development Kit (CDK) and its role in cloud infrastructure.
Learn to define cloud resources in code and provision them using AWS CloudFormation.
Installation of AWS CDK and its Various Commands
Set up AWS CDK in your environment.
Master essential AWS CDK commands for infrastructure deployment.
Advantages of Serverless Technologies
Discover the benefits of using serverless technologies in cloud computing.
Learn how serverless can streamline operations and reduce costs.
Creating an AWS Cloud9 Environment
Learn to set up and use the AWS Cloud9 IDE for development.
Understand how Cloud9 simplifies coding with a cloud-based editor.
Creating Data Producers Lambda Stack
Implement Lambda functions to fetch data from the Alpha Vantage API.
Set up a pipeline to stream this data into AWS Kinesis.
Creating Data Consumers Lambda Stack
Develop Lambda functions to consume data from AWS Kinesis.
Transform and load the data into AWS DynamoDB.
Creating Kinesis Data Streams
Set up Kinesis Data Streams to handle real-time data processing.
Learn to manage high-throughput data streaming in AWS.
Setting Up Environment Variables
Configure and manage environment variables for your AWS setup.
Ensure secure and efficient access to API keys and resources.
Deployment of AWS CDK
Deploy your AWS infrastructure using CDK.
Learn to manage and update your cloud resources.
Performing Data Analytics using Apache Flink and Apache Zeppelin
Utilize Apache Flink for real-time data processing.
Explore data with Apache Zeppelin for insightful analytics.
Creating ETL Jobs using AWS Glue
Implement AWS Glue for efficient ETL (Extract, Transform, Load) operations.
Automate data preparation and loading processes.
Performing Analysis using Amazon Athena
Use Amazon Athena for interactive data querying.
Analyze and visualize data stored in AWS DynamoDB.
Project Description
Business Overview
This project focuses on cryptocurrency data analytics, leveraging AWS technologies to create a scalable, serverless ETL pipeline. We will extract data from Alpha Vantage, transform it using AWS Lambda, and load it into DynamoDB. Further analytics will be performed using Apache Flink, Apache Zeppelin, and Amazon Athena.

Dataset Description
Alpha Vantage provides a comprehensive suite of APIs for financial market data. This project utilizes their cryptocurrency data offerings, including real-time and historical data, technical indicators, and global market data.

Tech Stack
Language: Python
Services: AWS S3, Amazon Lambda, AWS Kinesis, Amazon Aurora, AWS Glue, Amazon Athena, Quicksight, AWS CDK
AWS CDK
The AWS Cloud Development Kit (CDK) is a powerful tool to define cloud infrastructure in familiar programming languages. It simplifies the deployment and management of AWS resources, enabling developers to focus on building robust applications.

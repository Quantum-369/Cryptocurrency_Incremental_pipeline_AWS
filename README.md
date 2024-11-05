# Incremental ETL Pipeline with AWS CDK 🚀

This project implements an incremental ETL (Extract, Transform, Load) pipeline for cryptocurrency data, leveraging the AWS Cloud Development Kit (CDK) to define and manage AWS infrastructure. The pipeline processes real-time cryptocurrency exchange rate data, storing and transforming it for analytics.

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture](#architecture)
3. [Services Used](#services-used)
4. [Setup and Prerequisites](#setup-and-prerequisites)
5. [Deployment](#deployment)
6. [Usage](#usage)
7. [Conclusion](#conclusion)

## 📖 Project Overview

This ETL pipeline gathers cryptocurrency data from an external API and streams it into an AWS Kinesis data stream. Lambda functions process and transform the data, which is then stored in DynamoDB and Amazon S3 for further analysis using Amazon Athena and QuickSight.

## 🏗️ Architecture

The pipeline architecture consists of the following components:

- **Data Producer Lambda**: Fetches exchange rates from the Alpha Vantage API, and streams it to a Kinesis data stream.
- **Kinesis Data Stream**: Manages the flow of real-time data.
- **Data Consumer Lambda**: Consumes data from Kinesis, transforms it, and stores it in DynamoDB.
- **DynamoDB**: Stores processed cryptocurrency data for analytics.
- **AWS Glue and Athena**: Enables data querying and further analysis.
- **S3**: Provides storage for processed data to support analytics in QuickSight.

## 🛠️ Services Used

- **AWS CDK**: Defines and provisions infrastructure using code.
- **AWS Lambda**: Executes code for data production and consumption.
- **Amazon Kinesis**: Manages data streaming.
- **DynamoDB**: Stores transformed data.
- **AWS Glue**: Manages ETL jobs.
- **Amazon S3**: Stores data for analytics.
- **Amazon Athena and QuickSight**: Provides data querying and visualization.

## 🚀 Setup and Prerequisites

1. **Install AWS CDK**: Ensure CDK is installed with:
   ```bash
   npm install -g aws-cdk
   ```
2. **AWS Account and CLI Configuration**: Set up an AWS account and configure AWS CLI with appropriate permissions.
3. **Clone the Repository**: Clone this GitHub repository.
4. **Install Python Dependencies**: Run the following to install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Deployment

1. **Bootstrap the AWS Environment**:
   ```bash
   cdk bootstrap
   ```
2. **Deploy the Stacks**:
   Deploy all stacks defined in `app.py` using:
   ```bash
   cdk deploy --all
   ```
   This will set up resources like Kinesis streams, Lambda functions, DynamoDB tables, and S3 buckets.

## 🚀 Usage

### Running the Pipeline

1. **Trigger Data Production**: The `DataProducerStack` Lambda function fetches and streams cryptocurrency data at scheduled intervals.
2. **Data Processing**: The `DataConsumerStack` Lambda function processes incoming data and stores it in DynamoDB.
3. **Query and Analyze Data**: Use AWS Glue and Athena to query and visualize the data stored in DynamoDB and S3.

## 🔚 Conclusion

This pipeline demonstrates the use of AWS serverless services and CDK for a scalable, real-time ETL solution. The project highlights the advantages of using infrastructure-as-code, enabling rapid setup and management of cloud resources.

---

<div align="center">
Made with ❤️ by HarshaV
</div>

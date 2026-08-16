# Customer Analytics Pipeline

An end-to-end customer analytics data engineering project that processes customer purchase data, creates customer-level insights, and prepares curated datasets for business analytics.

## Project Overview

This project demonstrates a cloud-oriented customer analytics pipeline using Azure Data Lake Storage Gen2, Azure Data Factory, Python, SQL, and Power BI.

The pipeline processes customer and purchase data to generate insights such as:

- Customer spending
- Purchase frequency
- Average purchase value
- Top customers
- Category performance
- Monthly revenue trends
- City-wise revenue
- Customer segmentation

## Architecture

```text
Customer Purchase Data
          |
          v
      ADLS Gen2
          |
          v
  Azure Data Factory
          |
          v
Data Transformation
          |
          v
   Curated Data
          |
          v
       Power BI
          |
          v
 Customer Insights

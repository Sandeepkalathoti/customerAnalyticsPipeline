# Customer Analytics Pipeline Architecture

## Overview

This project implements a customer analytics data pipeline for processing customer purchase data and generating business insights.

The pipeline uses Azure Data Lake Storage for data storage, Azure Data Factory for data movement and orchestration, and Power BI for customer analytics and visualization.

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
   Curated Customer Data
          |
          v
       Power BI
          |
          v
 Customer Insights

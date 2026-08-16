# Customer Analytics ADF Pipeline

## Pipeline Name

customer_analytics_pipeline

## Objective

The Azure Data Factory pipeline orchestrates the movement of customer and purchase data from the raw ADLS Gen2 layer into the curated analytics layer.

## Pipeline Flow

```text
                ADLS Gen2
                   |
          +--------+--------+
          |                 |
          v                 v
     Customers           Purchases
        Raw                 Raw
          |                 |
          +--------+--------+
                   |
                   v
          Azure Data Factory
                   |
                   v
          Data Transformation
                   |
                   v
             Data Quality
                   |
                   v
           Curated ADLS Gen2
                   |
                   v
               Power BI

## Project Highlights

### Cloud Data Engineering

- Designed a customer analytics pipeline using Azure Data Lake Storage Gen2.
- Used Azure Data Factory for data ingestion and pipeline orchestration.
- Organized data into raw and curated layers.
- Prepared analytics-ready datasets for Power BI.

### Data Transformation

- Cleaned and standardized customer data.
- Removed duplicate customer and purchase records.
- Validated data quality rules.
- Calculated purchase-level `total_amount`.
- Generated customer-level spending metrics.

### Customer Analytics

The pipeline generates:

- Total customers
- Total purchases
- Total revenue
- Average purchase value
- Customer purchase frequency
- Top customers by spending
- Category-wise revenue
- Monthly revenue trends
- City-wise revenue
- Customer spending segments

### Engineering Practices

- Modular Python ETL code
- SQL-based analytics
- Automated data quality validation
- Unit testing with Pytest
- GitHub Actions CI
- Environment-based configuration
- Secret-safe GitHub repository
- Documented ADF architecture

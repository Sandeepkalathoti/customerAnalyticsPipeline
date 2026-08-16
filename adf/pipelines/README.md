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

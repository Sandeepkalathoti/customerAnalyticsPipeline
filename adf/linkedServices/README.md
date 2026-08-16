# Azure Data Factory Linked Services

This directory documents the external services used by the Customer Analytics pipeline.

## 1. Azure Data Lake Storage Gen2

ADF uses Azure Data Lake Storage Gen2 as the primary storage layer for customer and purchase datasets.

### Purpose

- Store raw customer data
- Store raw purchase data
- Store transformed data
- Store curated analytics datasets

### Recommended Structure

```text
customer-analytics/
│
├── raw/
│   ├── customers/
│   └── purchases/
│
├── processed/
│   ├── customers/
│   └── purchases/
│
└── curated/
    ├── customer_purchase_summary/
    └── purchase_analytics/

# Azure Data Factory Datasets

This directory documents the datasets used by the Customer Analytics pipeline.

## Dataset Architecture

```text
                    ADLS Gen2
                       |
          +------------+------------+
          |                         |
          v                         v
   Customer Dataset         Purchase Dataset
          |                         |
          +------------+------------+
                       |
                       v
              Azure Data Factory
                       |
                       v
                Curated Data

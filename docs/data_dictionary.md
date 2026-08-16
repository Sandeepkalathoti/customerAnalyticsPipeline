# Customer Analytics Data Dictionary

## Customers Dataset

| Column | Data Type | Description |
|---|---|---|
| customer_id | String | Unique identifier for each customer |
| customer_name | String | Customer full name |
| email | String | Customer email address |
| city | String | Customer city |
| age | Integer | Customer age |
| gender | String | Customer gender |
| signup_date | Date | Date when the customer registered |

## Purchases Dataset

| Column | Data Type | Description |
|---|---|---|
| purchase_id | String | Unique identifier for each purchase |
| customer_id | String | Identifier of the customer who made the purchase |
| purchase_date | Date | Date of the purchase |
| product | String | Purchased product |
| category | String | Product category |
| quantity | Integer | Number of units purchased |
| unit_price | Decimal | Price of one unit |
| payment_method | String | Payment method used for the purchase |

## Derived Fields

### Total Amount

Calculated as:

```text
total_amount = quantity × unit_price

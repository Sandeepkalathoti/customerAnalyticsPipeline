# Power BI Customer Analytics Dashboard

## Dashboard Objective

The dashboard provides customer purchase insights and helps analyze customer spending behavior, purchase patterns, product/category performance, and customer segments.

## Data Source

The dashboard is designed to consume the curated customer analytics datasets produced by the pipeline.

Primary analytical views:

- CUSTOMER_PURCHASE_SUMMARY
- TOP_CUSTOMERS
- CATEGORY_PERFORMANCE
- MONTHLY_PURCHASE_TRENDS
- CITY_CUSTOMER_ANALYTICS
- CUSTOMER_SEGMENTS

## KPI Cards

The dashboard should display the following key metrics:

### Total Customers

Count of unique customers.

### Total Purchases

Total number of customer purchases.

### Total Revenue

Total value of all purchases.

### Average Purchase Value

Average amount spent per purchase.

### High Value Customers

Number of customers belonging to the `HIGH_VALUE` segment.

## Recommended Visuals

### 1. Revenue by Month

**Chart:** Line chart

**Axis:**
- Purchase Month

**Value:**
- Total Revenue

Purpose:

Understand monthly revenue trends.

---

### 2. Top Customers

**Chart:** Bar chart

**Axis:**
- Customer Name

**Value:**
- Total Spend

Purpose:

Identify the highest-value customers.

---

### 3. Revenue by Category

**Chart:** Column chart

**Axis:**
- Category

**Value:**
- Total Revenue

Purpose:

Identify the best-performing product categories.

---

### 4. Customer Segmentation

**Chart:** Donut chart

**Legend:**
- Customer Segment

**Value:**
- Customer Count

Segments:

- HIGH_VALUE
- MEDIUM_VALUE
- LOW_VALUE
- NO_PURCHASE

Purpose:

Understand the distribution of customer value.

---

### 5. City-wise Revenue

**Chart:** Map or bar chart

**Location:**
- City

**Value:**
- Total Revenue

Purpose:

Identify high-performing customer locations.

---

### 6. Purchase Count by Customer

**Chart:** Bar chart

**Axis:**
- Customer Name

**Value:**
- Purchase Count

Purpose:

Identify frequent customers.

## Dashboard Filters

Recommended filters:

- Date
- City
- Category
- Gender
- Customer Segment
- Payment Method

## Dashboard Layout

```text
+-------------------------------------------------------+
|              CUSTOMER ANALYTICS DASHBOARD             |
+-------------------------------------------------------+
| Total Customers | Total Purchases | Total Revenue    |
| Average Purchase Value | High Value Customers        |
+-------------------------------------------------------+
|                                                       |
| Revenue by Month           | Revenue by Category     |
|                                                       |
+-------------------------------------------------------+
|                                                       |
| Top Customers              | Customer Segments      |
|                                                       |
+-------------------------------------------------------+
|                                                       |
| City-wise Revenue          | Purchase Frequency     |
|                                                       |
+-------------------------------------------------------+
| Filters: Date | City | Category | Segment | Gender   |
+-------------------------------------------------------+

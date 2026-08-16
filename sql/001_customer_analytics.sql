-- Customer Analytics SQL Models

-- 1. Customer purchase summary

CREATE OR REPLACE VIEW CUSTOMER_PURCHASE_SUMMARY AS
SELECT
    c.customer_id,
    c.customer_name,
    c.city,
    c.age,
    c.gender,

    COUNT(p.purchase_id) AS purchase_count,

    COALESCE(
        SUM(p.quantity),
        0
    ) AS total_quantity,

    COALESCE(
        SUM(p.total_amount),
        0
    ) AS total_spend,

    COALESCE(
        AVG(p.total_amount),
        0
    ) AS average_purchase_value

FROM customers c

LEFT JOIN purchases p
    ON c.customer_id = p.customer_id

GROUP BY
    c.customer_id,
    c.customer_name,
    c.city,
    c.age,
    c.gender;


-- 2. Top customers by spending

CREATE OR REPLACE VIEW TOP_CUSTOMERS AS
SELECT
    customer_id,
    customer_name,
    city,
    purchase_count,
    total_spend,
    average_purchase_value,

    RANK() OVER (
        ORDER BY total_spend DESC
    ) AS spending_rank

FROM CUSTOMER_PURCHASE_SUMMARY

ORDER BY total_spend DESC;


-- 3. Category performance

CREATE OR REPLACE VIEW CATEGORY_PERFORMANCE AS
SELECT
    category,

    COUNT(purchase_id) AS purchase_count,

    SUM(quantity) AS total_quantity,

    SUM(total_amount) AS total_revenue,

    AVG(total_amount) AS average_purchase_value

FROM purchases

GROUP BY category

ORDER BY total_revenue DESC;


-- 4. Monthly purchase trends

CREATE OR REPLACE VIEW MONTHLY_PURCHASE_TRENDS AS
SELECT
    DATE_TRUNC(
        'MONTH',
        purchase_date
    ) AS purchase_month,

    COUNT(purchase_id) AS purchase_count,

    SUM(quantity) AS total_quantity,

    SUM(total_amount) AS total_revenue,

    AVG(total_amount) AS average_purchase_value

FROM purchases

GROUP BY
    DATE_TRUNC(
        'MONTH',
        purchase_date
    )

ORDER BY purchase_month;


-- 5. City-wise customer analytics

CREATE OR REPLACE VIEW CITY_CUSTOMER_ANALYTICS AS
SELECT
    c.city,

    COUNT(DISTINCT c.customer_id)
        AS customer_count,

    COUNT(p.purchase_id)
        AS purchase_count,

    COALESCE(
        SUM(p.total_amount),
        0
    ) AS total_revenue,

    COALESCE(
        AVG(p.total_amount),
        0
    ) AS average_purchase_value

FROM customers c

LEFT JOIN purchases p
    ON c.customer_id = p.customer_id

GROUP BY c.city

ORDER BY total_revenue DESC;


-- 6. Customer segmentation

CREATE OR REPLACE VIEW CUSTOMER_SEGMENTS AS
SELECT
    customer_id,
    customer_name,
    city,
    purchase_count,
    total_spend,

    CASE
        WHEN total_spend >= 50000
            THEN 'HIGH_VALUE'

        WHEN total_spend >= 20000
            THEN 'MEDIUM_VALUE'

        WHEN total_spend > 0
            THEN 'LOW_VALUE'

        ELSE 'NO_PURCHASE'
    END AS customer_segment

FROM CUSTOMER_PURCHASE_SUMMARY;

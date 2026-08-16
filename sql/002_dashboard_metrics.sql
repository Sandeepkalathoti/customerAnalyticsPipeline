-- Customer Analytics Dashboard Metrics


-- 1. Total Customers

SELECT
    COUNT(DISTINCT customer_id) AS total_customers
FROM customers;


-- 2. Total Purchases

SELECT
    COUNT(*) AS total_purchases
FROM purchases;


-- 3. Total Revenue

SELECT
    SUM(
        quantity * unit_price
    ) AS total_revenue
FROM purchases;


-- 4. Average Purchase Value

SELECT
    AVG(
        quantity * unit_price
    ) AS average_purchase_value
FROM purchases;


-- 5. High Value Customers

SELECT
    COUNT(*) AS high_value_customers
FROM CUSTOMER_SEGMENTS
WHERE customer_segment = 'HIGH_VALUE';


-- 6. Top 10 Customers by Spending

SELECT
    customer_id,
    customer_name,
    city,
    purchase_count,
    total_spend,
    average_purchase_value
FROM CUSTOMER_PURCHASE_SUMMARY
ORDER BY total_spend DESC
LIMIT 10;


-- 7. Revenue by Category

SELECT
    category,
    COUNT(*) AS purchase_count,
    SUM(quantity) AS total_quantity,
    SUM(
        quantity * unit_price
    ) AS total_revenue
FROM purchases
GROUP BY category
ORDER BY total_revenue DESC;


-- 8. Monthly Revenue

SELECT
    DATE_TRUNC(
        'MONTH',
        purchase_date
    ) AS purchase_month,

    COUNT(*) AS purchase_count,

    SUM(
        quantity * unit_price
    ) AS total_revenue

FROM purchases

GROUP BY
    DATE_TRUNC(
        'MONTH',
        purchase_date
    )

ORDER BY purchase_month;


-- 9. City-wise Revenue

SELECT
    c.city,

    COUNT(DISTINCT c.customer_id)
        AS customer_count,

    COUNT(p.purchase_id)
        AS purchase_count,

    SUM(
        p.quantity * p.unit_price
    ) AS total_revenue

FROM customers c

LEFT JOIN purchases p
    ON c.customer_id = p.customer_id

GROUP BY c.city

ORDER BY total_revenue DESC;


-- 10. Customer Segment Distribution

SELECT
    customer_segment,
    COUNT(*) AS customer_count,
    SUM(total_spend) AS segment_revenue
FROM CUSTOMER_SEGMENTS
GROUP BY customer_segment
ORDER BY segment_revenue DESC;

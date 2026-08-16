from customer_analytics.transform import (
    transform_customers,
    transform_purchases,
    create_customer_summary,
)


def test_transform_customer():
    customers = [
        {
            "customer_id": " C001 ",
            "customer_name": " Ravi Kumar ",
            "email": "RAVI@EXAMPLE.COM",
            "city": " Hyderabad ",
            "age": "28",
            "gender": "male",
            "signup_date": "2024-01-15",
        }
    ]

    result = transform_customers(customers)

    assert len(result) == 1
    assert result[0]["customer_id"] == "C001"
    assert result[0]["customer_name"] == "Ravi Kumar"
    assert result[0]["email"] == "ravi@example.com"
    assert result[0]["city"] == "Hyderabad"
    assert result[0]["age"] == 28
    assert result[0]["gender"] == "MALE"


def test_duplicate_customers_are_removed():
    customers = [
        {
            "customer_id": "C001",
            "customer_name": "Ravi Kumar",
            "email": "ravi@example.com",
            "city": "Hyderabad",
            "age": "28",
            "gender": "Male",
            "signup_date": "2024-01-15",
        },
        {
            "customer_id": "C001",
            "customer_name": "Ravi Kumar",
            "email": "ravi@example.com",
            "city": "Hyderabad",
            "age": "28",
            "gender": "Male",
            "signup_date": "2024-01-15",
        },
    ]

    result = transform_customers(customers)

    assert len(result) == 1


def test_purchase_total_amount():
    purchases = [
        {
            "purchase_id": "P1001",
            "customer_id": "C001",
            "purchase_date": "2025-01-05",
            "product": "Laptop",
            "category": "Electronics",
            "quantity": "2",
            "unit_price": "65000",
            "payment_method": "Credit Card",
        }
    ]

    result = transform_purchases(purchases)

    assert len(result) == 1
    assert result[0]["quantity"] == 2
    assert result[0]["unit_price"] == 65000
    assert result[0]["total_amount"] == 130000
    assert result[0]["payment_method"] == "CREDIT CARD"


def test_duplicate_purchases_are_removed():
    purchases = [
        {
            "purchase_id": "P1001",
            "customer_id": "C001",
            "purchase_date": "2025-01-05",
            "product": "Laptop",
            "category": "Electronics",
            "quantity": "1",
            "unit_price": "65000",
            "payment_method": "UPI",
        },
        {
            "purchase_id": "P1001",
            "customer_id": "C001",
            "purchase_date": "2025-01-05",
            "product": "Laptop",
            "category": "Electronics",
            "quantity": "1",
            "unit_price": "65000",
            "payment_method": "UPI",
        },
    ]

    result = transform_purchases(purchases)

    assert len(result) == 1


def test_customer_summary():
    customers = [
        {
            "customer_id": "C001",
            "customer_name": "Ravi Kumar",
            "email": "ravi@example.com",
            "city": "Hyderabad",
            "age": 28,
            "gender": "MALE",
            "signup_date": "2024-01-15",
        }
    ]

    purchases = [
        {
            "purchase_id": "P1001",
            "customer_id": "C001",
            "purchase_date": "2025-01-05",
            "product": "Laptop",
            "category": "Electronics",
            "quantity": 1,
            "unit_price": 65000,
            "total_amount": 65000,
            "payment_method": "UPI",
        },
        {
            "purchase_id": "P1002",
            "customer_id": "C001",
            "purchase_date": "2025-02-05",
            "product": "Keyboard",
            "category": "Electronics",
            "quantity": 2,
            "unit_price": 1800,
            "total_amount": 3600,
            "payment_method": "UPI",
        },
    ]

    result = create_customer_summary(
        customers,
        purchases,
    )

    assert len(result) == 1
    assert result[0]["purchase_count"] == 2
    assert result[0]["total_quantity"] == 3
    assert result[0]["total_spend"] == 68600
    assert result[0]["average_purchase_value"] == 34300

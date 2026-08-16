from customer_analytics.quality import (
    validate_customers,
    validate_purchases,
)


def valid_customer():
    return {
        "customer_id": "C001",
        "customer_name": "Ravi Kumar",
        "email": "ravi@example.com",
        "city": "Hyderabad",
        "age": 28,
        "gender": "MALE",
        "signup_date": "2024-01-15",
    }


def valid_purchase():
    return {
        "purchase_id": "P1001",
        "customer_id": "C001",
        "purchase_date": "2025-01-05",
        "product": "Laptop",
        "category": "Electronics",
        "quantity": 1,
        "unit_price": 65000,
        "payment_method": "UPI",
    }


def test_valid_customer():
    valid, invalid = validate_customers(
        [valid_customer()]
    )

    assert len(valid) == 1
    assert len(invalid) == 0


def test_missing_customer_id():
    customer = valid_customer()
    customer["customer_id"] = ""

    valid, invalid = validate_customers(
        [customer]
    )

    assert len(valid) == 0
    assert len(invalid) == 1
    assert "Missing customer_id" in invalid[0]["errors"]


def test_duplicate_customer():
    customer = valid_customer()

    valid, invalid = validate_customers(
        [customer, customer.copy()]
    )

    assert len(valid) == 1
    assert len(invalid) == 1
    assert (
        "Duplicate customer_id"
        in invalid[0]["errors"]
    )


def test_invalid_customer_age():
    customer = valid_customer()
    customer["age"] = 0

    valid, invalid = validate_customers(
        [customer]
    )

    assert len(valid) == 0
    assert len(invalid) == 1
    assert "Invalid age" in invalid[0]["errors"]


def test_valid_purchase():
    valid, invalid = validate_purchases(
        [valid_purchase()]
    )

    assert len(valid) == 1
    assert len(invalid) == 0


def test_missing_purchase_id():
    purchase = valid_purchase()
    purchase["purchase_id"] = ""

    valid, invalid = validate_purchases(
        [purchase]
    )

    assert len(valid) == 0
    assert len(invalid) == 1
    assert (
        "Missing purchase_id"
        in invalid[0]["errors"]
    )


def test_duplicate_purchase():
    purchase = valid_purchase()

    valid, invalid = validate_purchases(
        [purchase, purchase.copy()]
    )

    assert len(valid) == 1
    assert len(invalid) == 1
    assert (
        "Duplicate purchase_id"
        in invalid[0]["errors"]
    )


def test_invalid_quantity():
    purchase = valid_purchase()
    purchase["quantity"] = 0

    valid, invalid = validate_purchases(
        [purchase]
    )

    assert len(valid) == 0
    assert len(invalid) == 1
    assert (
        "Quantity must be greater than 0"
        in invalid[0]["errors"]
    )


def test_negative_unit_price():
    purchase = valid_purchase()
    purchase["unit_price"] = -100

    valid, invalid = validate_purchases(
        [purchase]
    )

    assert len(valid) == 0
    assert len(invalid) == 1
    assert (
        "Unit price cannot be negative"
        in invalid[0]["errors"]
    )

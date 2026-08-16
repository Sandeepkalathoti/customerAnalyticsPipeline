from typing import Any


def validate_customers(
    customers: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Validate customer records."""

    valid = []
    invalid = []
    seen_ids = set()

    for customer in customers:
        errors = []

        customer_id = customer.get("customer_id")

        if not customer_id:
            errors.append("Missing customer_id")

        elif customer_id in seen_ids:
            errors.append("Duplicate customer_id")

        seen_ids.add(customer_id)

        if not customer.get("customer_name"):
            errors.append("Missing customer_name")

        if not customer.get("email"):
            errors.append("Missing email")

        try:
            age = int(customer.get("age", 0))

            if age <= 0:
                errors.append("Invalid age")

        except (TypeError, ValueError):
            errors.append("Invalid age")

        if errors:
            invalid.append(
                {
                    "record": customer,
                    "errors": errors,
                }
            )
        else:
            valid.append(customer)

    return valid, invalid


def validate_purchases(
    purchases: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Validate purchase records."""

    valid = []
    invalid = []
    seen_ids = set()

    for purchase in purchases:
        errors = []

        purchase_id = purchase.get("purchase_id")

        if not purchase_id:
            errors.append("Missing purchase_id")

        elif purchase_id in seen_ids:
            errors.append("Duplicate purchase_id")

        seen_ids.add(purchase_id)

        if not purchase.get("customer_id"):
            errors.append("Missing customer_id")

        if not purchase.get("product"):
            errors.append("Missing product")

        try:
            quantity = int(
                purchase.get("quantity", 0)
            )

            if quantity <= 0:
                errors.append(
                    "Quantity must be greater than 0"
                )

        except (TypeError, ValueError):
            errors.append("Invalid quantity")

        try:
            unit_price = float(
                purchase.get("unit_price", 0)
            )

            if unit_price < 0:
                errors.append(
                    "Unit price cannot be negative"
                )

        except (TypeError, ValueError):
            errors.append("Invalid unit price")

        if not purchase.get("purchase_date"):
            errors.append("Missing purchase_date")

        if errors:
            invalid.append(
                {
                    "record": purchase,
                    "errors": errors,
                }
            )
        else:
            valid.append(purchase)

    return valid, invalid

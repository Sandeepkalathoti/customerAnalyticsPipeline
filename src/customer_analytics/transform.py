from typing import Any


def transform_customers(
    customers: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Clean and standardize customer records."""

    transformed = []
    seen_customer_ids = set()

    for customer in customers:
        customer_id = str(
            customer.get("customer_id", "")
        ).strip()

        if not customer_id:
            continue

        if customer_id in seen_customer_ids:
            continue

        seen_customer_ids.add(customer_id)

        transformed.append(
            {
                "customer_id": customer_id,
                "customer_name": str(
                    customer.get("customer_name", "")
                ).strip(),
                "email": str(
                    customer.get("email", "")
                ).strip().lower(),
                "city": str(
                    customer.get("city", "")
                ).strip(),
                "age": int(customer["age"]),
                "gender": str(
                    customer.get("gender", "")
                ).strip().upper(),
                "signup_date": customer.get(
                    "signup_date"
                ),
            }
        )

    return transformed


def transform_purchases(
    purchases: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Clean purchase records and calculate total amount."""

    transformed = []
    seen_purchase_ids = set()

    for purchase in purchases:
        purchase_id = str(
            purchase.get("purchase_id", "")
        ).strip()

        if not purchase_id:
            continue

        if purchase_id in seen_purchase_ids:
            continue

        seen_purchase_ids.add(purchase_id)

        quantity = int(
            purchase.get("quantity", 0)
        )

        unit_price = float(
            purchase.get("unit_price", 0)
        )

        if quantity <= 0 or unit_price < 0:
            continue

        total_amount = quantity * unit_price

        transformed.append(
            {
                "purchase_id": purchase_id,
                "customer_id": str(
                    purchase.get("customer_id", "")
                ).strip(),
                "purchase_date": purchase.get(
                    "purchase_date"
                ),
                "product": str(
                    purchase.get("product", "")
                ).strip(),
                "category": str(
                    purchase.get("category", "")
                ).strip(),
                "quantity": quantity,
                "unit_price": unit_price,
                "total_amount": total_amount,
                "payment_method": str(
                    purchase.get("payment_method", "")
                ).strip().upper(),
            }
        )

    return transformed


def create_customer_summary(
    customers: list[dict[str, Any]],
    purchases: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Create customer-level purchase analytics."""

    purchase_summary: dict[str, dict[str, Any]] = {}

    for purchase in purchases:
        customer_id = purchase["customer_id"]

        if customer_id not in purchase_summary:
            purchase_summary[customer_id] = {
                "purchase_count": 0,
                "total_spend": 0.0,
                "total_quantity": 0,
            }

        purchase_summary[customer_id][
            "purchase_count"
        ] += 1

        purchase_summary[customer_id][
            "total_spend"
        ] += purchase["total_amount"]

        purchase_summary[customer_id][
            "total_quantity"
        ] += purchase["quantity"]

    summary = []

    for customer in customers:
        customer_id = customer["customer_id"]

        metrics = purchase_summary.get(
            customer_id,
            {
                "purchase_count": 0,
                "total_spend": 0.0,
                "total_quantity": 0,
            },
        )

        purchase_count = metrics["purchase_count"]
        total_spend = metrics["total_spend"]

        average_purchase_value = (
            total_spend / purchase_count
            if purchase_count > 0
            else 0.0
        )

        summary.append(
            {
                "customer_id": customer_id,
                "customer_name": customer[
                    "customer_name"
                ],
                "city": customer["city"],
                "age": customer["age"],
                "gender": customer["gender"],
                "purchase_count": purchase_count,
                "total_quantity": metrics[
                    "total_quantity"
                ],
                "total_spend": round(
                    total_spend,
                    2,
                ),
                "average_purchase_value": round(
                    average_purchase_value,
                    2,
                ),
            }
        )

    return summary

import csv
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parents[2]

OUTPUT_DIR = (
    BASE_DIR
    / "data"
    / "curated"
)


def write_csv(
    records: list[dict[str, Any]],
    file_name: str,
) -> Path:
    """
    Write curated records to a CSV file.
    """

    if not records:
        raise ValueError(
            "No records available for loading."
        )

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_file = OUTPUT_DIR / file_name

    with output_file.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=records[0].keys(),
        )

        writer.writeheader()
        writer.writerows(records)

    return output_file


def load_customer_summary(
    customer_summary: list[dict[str, Any]],
) -> Path:
    """
    Write customer-level analytics
    to the curated layer.
    """

    return write_csv(
        customer_summary,
        "customer_purchase_summary.csv",
    )


def load_purchase_data(
    purchases: list[dict[str, Any]],
) -> Path:
    """
    Write transformed purchase data
    to the curated layer.
    """

    return write_csv(
        purchases,
        "curated_purchases.csv",
    )

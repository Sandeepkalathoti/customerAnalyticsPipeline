import csv
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parents[2]

CUSTOMERS_FILE = BASE_DIR / "data" / "sample" / "customers.csv"
PURCHASES_FILE = BASE_DIR / "data" / "sample" / "purchases.csv"


def read_csv_file(
    file_path: Path,
) -> list[dict[str, Any]]:
    """Read records from a CSV file."""

    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    with file_path.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as file:
        reader = csv.DictReader(file)

        return list(reader)


def extract_customers() -> list[dict[str, Any]]:
    """Extract customer records."""

    return read_csv_file(CUSTOMERS_FILE)


def extract_purchases() -> list[dict[str, Any]]:
    """Extract customer purchase records."""

    return read_csv_file(PURCHASES_FILE)


if __name__ == "__main__":
    customers = extract_customers()
    purchases = extract_purchases()

    print(
        f"Customers extracted: {len(customers)}"
    )

    print(
        f"Purchases extracted: {len(purchases)}"
    )

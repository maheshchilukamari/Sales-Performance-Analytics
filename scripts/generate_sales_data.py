"""
Generate a realistic raw sales dataset.

This script is the first step in the project pipeline. It creates sample
order-level sales data that looks similar to what a business analyst might
receive from a sales operations system.

Run from the project root:
    python scripts/generate_sales_data.py
"""

from pathlib import Path
import random

import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_PATH = DATA_DIR / "sales_raw.csv"


def build_sales_dataset(row_count: int = 2500, seed: int = 42) -> pd.DataFrame:
    """
    Create a reproducible sales dataset with realistic business dimensions.

    Args:
        row_count: Number of clean order rows to generate before adding sample
            data quality issues.
        seed: Random seed used to keep the generated dataset reproducible.

    Returns:
        A Pandas DataFrame containing raw sales records.
    """
    random.seed(seed)
    np.random.seed(seed)

    states_by_region = {
        "East": ["New York", "Pennsylvania", "Massachusetts", "New Jersey", "Virginia"],
        "West": ["California", "Washington", "Oregon", "Arizona", "Colorado"],
        "Central": ["Texas", "Illinois", "Michigan", "Ohio", "Missouri"],
        "South": ["Florida", "Georgia", "North Carolina", "Tennessee", "Louisiana"],
    }

    products_by_category = {
        "Technology": [
            "Laptop Pro 14",
            "Wireless Keyboard",
            "Cloud Security Suite",
            "USB-C Docking Station",
            "Noise-Canceling Headset",
        ],
        "Furniture": [
            "Ergonomic Office Chair",
            "Standing Desk",
            "Conference Table",
            "Filing Cabinet",
            "Bookcase",
        ],
        "Office Supplies": [
            "Printer Paper Case",
            "Premium Notebook Pack",
            "Ballpoint Pen Set",
            "Desk Organizer",
            "Toner Cartridge",
        ],
    }

    price_ranges = {
        "Technology": (120, 1800),
        "Furniture": (85, 1400),
        "Office Supplies": (8, 280),
    }

    margin_ranges = {
        "Technology": (0.14, 0.34),
        "Furniture": (0.08, 0.26),
        "Office Supplies": (0.10, 0.30),
    }

    customer_segments = ["Consumer", "Corporate", "Home Office"]
    start_date = pd.Timestamp("2023-01-01")
    end_date = pd.Timestamp("2025-12-31")
    date_range_days = (end_date - start_date).days

    records = []

    for i in range(1, row_count + 1):
        # Randomly assign each order to a realistic geography, segment, and product.
        order_date = start_date + pd.Timedelta(days=random.randint(0, date_range_days))
        region = random.choices(
            population=list(states_by_region.keys()),
            weights=[0.27, 0.31, 0.20, 0.22],
            k=1,
        )[0]
        state = random.choice(states_by_region[region])
        segment = random.choices(customer_segments, weights=[0.46, 0.36, 0.18], k=1)[0]
        category = random.choices(
            population=list(products_by_category.keys()),
            weights=[0.38, 0.25, 0.37],
            k=1,
        )[0]
        product_name = random.choice(products_by_category[category])

        # Generate pricing and quantity values based on the selected category.
        unit_price = random.uniform(*price_ranges[category])
        quantity = random.choices([1, 2, 3, 4, 5, 6, 8, 10], weights=[24, 23, 18, 13, 9, 6, 4, 3], k=1)[0]
        discount = random.choices([0.00, 0.05, 0.10, 0.15, 0.20, 0.30], weights=[45, 17, 15, 10, 8, 5], k=1)[0]

        gross_sales = unit_price * quantity
        sales = gross_sales * (1 - discount)
        base_margin = random.uniform(*margin_ranges[category])

        # Higher discounts reduce realized profit and can turn low-margin orders negative.
        profit = sales * base_margin - gross_sales * discount * random.uniform(0.35, 0.65)

        records.append(
            {
                "Order ID": f"SO-{100000 + i}",
                "Order Date": order_date.strftime("%Y-%m-%d"),
                "Customer ID": f"CUST-{random.randint(1000, 1899)}",
                "Customer Segment": segment,
                "Region": region,
                "State": state,
                "Product Category": category,
                "Product Name": product_name,
                "Sales": round(sales, 2),
                "Quantity": quantity,
                "Discount": discount,
                "Profit": round(profit, 2),
            }
        )

    df = pd.DataFrame(records)

    # Add a few data quality issues so the cleaning script demonstrates useful ETL work.
    duplicate_rows = df.sample(12, random_state=seed)
    df = pd.concat([df, duplicate_rows], ignore_index=True)

    missing_segment_indexes = df.sample(8, random_state=seed + 1).index
    missing_profit_indexes = df.sample(6, random_state=seed + 2).index
    df.loc[missing_segment_indexes, "Customer Segment"] = np.nan
    df.loc[missing_profit_indexes, "Profit"] = np.nan

    return df.sample(frac=1, random_state=seed).reset_index(drop=True)


def main() -> None:
    """Generate the raw dataset and save it to the data folder."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    sales_df = build_sales_dataset()
    sales_df.to_csv(RAW_DATA_PATH, index=False)
    print(f"Generated raw sales dataset: {RAW_DATA_PATH}")
    print(f"Rows: {len(sales_df):,}")


if __name__ == "__main__":
    main()

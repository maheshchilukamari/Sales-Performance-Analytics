"""
Clean the raw sales dataset and create calculated analytics fields.

This script is the second step in the project pipeline. It shows a practical
ETL process: load raw data, clean common data quality issues, create calculated
fields, and export a reporting-ready CSV file.

Run from the project root:
    python scripts/etl_clean_sales_data.py
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_PATH = DATA_DIR / "sales_raw.csv"
CLEAN_DATA_PATH = DATA_DIR / "sales_cleaned.csv"


def clean_sales_data(raw_data_path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """
    Load, clean, and enrich the sales dataset.

    Args:
        raw_data_path: Path to the raw CSV file.

    Returns:
        A cleaned Pandas DataFrame ready for SQL and Power BI reporting.
    """
    if not raw_data_path.exists():
        raise FileNotFoundError(f"Raw data file not found: {raw_data_path}")

    df = pd.read_csv(raw_data_path)

    # Standardize column names for easier Python and SQL work.
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # Remove exact duplicate order lines.
    df = df.drop_duplicates()

    # Convert data types so dates and numbers behave correctly in analysis.
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    numeric_columns = ["sales", "quantity", "discount", "profit"]
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # Clean missing values using business-friendly defaults.
    df["customer_segment"] = df["customer_segment"].fillna("Unknown")
    df["profit"] = df["profit"].fillna(0)

    # Remove rows that cannot support reliable reporting.
    required_columns = [
        "order_id",
        "order_date",
        "customer_id",
        "region",
        "state",
        "product_category",
        "product_name",
        "sales",
        "quantity",
    ]
    df = df.dropna(subset=required_columns)

    # Keep values in sensible business ranges.
    df = df[(df["sales"] >= 0) & (df["quantity"] > 0)]
    df["discount"] = df["discount"].clip(lower=0, upper=0.90)

    # Create calculated fields used by SQL reporting and Power BI.
    df["profit_margin"] = (df["profit"] / df["sales"]).replace([float("inf"), -float("inf")], 0).fillna(0)
    df["order_month"] = df["order_date"].dt.to_period("M").astype(str)
    df["average_order_value"] = df["sales"] / df["quantity"]
    df["year"] = df["order_date"].dt.year
    df["month_name"] = df["order_date"].dt.month_name()

    # Round financial metrics for clean presentation.
    money_columns = ["sales", "profit", "average_order_value"]
    df[money_columns] = df[money_columns].round(2)
    df["profit_margin"] = df["profit_margin"].round(4)

    # Sort by order date for time-series analysis.
    df = df.sort_values(["order_date", "order_id"]).reset_index(drop=True)

    return df


def main() -> None:
    """Run the cleaning step and write the cleaned CSV file."""
    cleaned_df = clean_sales_data()
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    cleaned_df.to_csv(CLEAN_DATA_PATH, index=False)
    print(f"Cleaned dataset exported: {CLEAN_DATA_PATH}")
    print(f"Rows after cleaning: {len(cleaned_df):,}")
    print(f"Columns: {len(cleaned_df.columns)}")


if __name__ == "__main__":
    main()

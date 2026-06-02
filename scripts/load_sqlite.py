"""
Load the cleaned sales dataset into a SQLite database.

This script is the third step in the project pipeline. It demonstrates how a
cleaned CSV file can be moved into a relational database for SQL analysis.

Run from the project root:
    python scripts/load_sqlite.py
"""

from pathlib import Path
import sqlite3

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
SQL_DIR = PROJECT_ROOT / "sql"
CLEAN_DATA_PATH = DATA_DIR / "sales_cleaned.csv"
DATABASE_PATH = DATA_DIR / "sales_performance.db"
CREATE_VIEWS_PATH = SQL_DIR / "create_views.sql"


def load_cleaned_data_to_sqlite() -> None:
    """Create a SQLite database table from the cleaned CSV file."""
    if not CLEAN_DATA_PATH.exists():
        raise FileNotFoundError(f"Cleaned data file not found: {CLEAN_DATA_PATH}")

    df = pd.read_csv(CLEAN_DATA_PATH)

    with sqlite3.connect(DATABASE_PATH) as connection:
        # Replace the table each time so the database always matches the latest cleaned CSV.
        df.to_sql("sales_orders", connection, if_exists="replace", index=False)

        # Create helpful indexes for dashboard-style filtering and aggregation.
        cursor = connection.cursor()
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_sales_order_date ON sales_orders(order_date);")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_sales_region ON sales_orders(region);")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_sales_category ON sales_orders(product_category);")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_sales_segment ON sales_orders(customer_segment);")

        if CREATE_VIEWS_PATH.exists():
            # Views make common reporting datasets easier to import or inspect.
            cursor.executescript(CREATE_VIEWS_PATH.read_text(encoding="utf-8"))

        connection.commit()

    print(f"SQLite database created: {DATABASE_PATH}")
    print("Table loaded: sales_orders")
    if CREATE_VIEWS_PATH.exists():
        print("Reporting views created from sql/create_views.sql")


if __name__ == "__main__":
    load_cleaned_data_to_sqlite()

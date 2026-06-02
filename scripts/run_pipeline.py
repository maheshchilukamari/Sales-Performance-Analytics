"""
Run the full sales analytics data pipeline in one command.

This script is the easiest way for a reviewer to rebuild the project outputs.
It generates raw data, cleans it, and loads the cleaned data into SQLite.

Run from the project root:
    python scripts/run_pipeline.py
"""

from generate_sales_data import main as generate_raw_data
from etl_clean_sales_data import main as clean_raw_data
from load_sqlite import load_cleaned_data_to_sqlite


def main() -> None:
    """Run all project pipeline steps in the correct order."""
    print("Step 1: Generating raw sales data...")
    generate_raw_data()

    print("\nStep 2: Cleaning and transforming sales data...")
    clean_raw_data()

    print("\nStep 3: Loading cleaned data into SQLite...")
    load_cleaned_data_to_sqlite()

    print("\nPipeline complete.")


if __name__ == "__main__":
    main()

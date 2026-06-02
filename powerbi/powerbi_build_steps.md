# Power BI Build Steps

1. Open Power BI Desktop.
2. Select **Get Data**.
3. Choose **Text/CSV** and load `data/sales_cleaned.csv`.
4. Confirm that `order_date` is a Date field and sales/profit columns are Decimal Number fields.
5. Rename the table to `sales_cleaned`.
6. Create the measures listed in `powerbi/dax_measures.txt`.
7. Build the visuals from `powerbi/dashboard_plan.md`.
8. Add slicers for Region, Product Category, Customer Segment, and Order Date.
9. Save the Power BI file as `powerbi/Sales_Performance_Analytics_Dashboard.pbix`.
10. Add dashboard screenshots to the `screenshots/` folder for GitHub.

## Optional SQLite Import

Power BI can connect to SQLite through an ODBC driver. If using SQLite:

1. Install a SQLite ODBC driver.
2. In Power BI Desktop, select **Get Data** > **ODBC**.
3. Connect to `data/sales_performance.db`.
4. Load the `sales_orders` table.
5. If you create the same DAX measures, either rename the imported table to `sales_cleaned` or update the table name inside each DAX formula.

The CSV path is recommended for the easiest portfolio review experience.

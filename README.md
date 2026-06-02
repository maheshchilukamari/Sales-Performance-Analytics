# Sales Performance Analytics Dashboard

Professional Data Analyst portfolio project prepared for a Daxwell company submission.

## Project Overview

The **Sales Performance Analytics Dashboard** is an end-to-end analytics project that demonstrates how a Data Analyst can clean data, build an ETL pipeline, write SQL queries, create KPI reporting logic, plan a Power BI dashboard, and communicate business recommendations.

The project uses a realistic sales dataset covering orders from 2023 through 2025. The workflow starts with raw data, cleans and enriches it with Python and Pandas, loads it into SQLite, analyzes it with SQL, and documents a Power BI dashboard design for business stakeholders.

## Business Problem

Sales leadership needs a clear view of revenue, profitability, regional performance, product performance, customer segment behavior, and discount impact. Without a centralized analytics process, leaders may only see total sales and miss important profitability risks.

This project helps answer business questions such as:

- Which regions generate the highest sales?
- Which product categories are most profitable?
- Which customer segments perform best?
- Which products drive the most revenue?
- Are discounts increasing sales while reducing profit?
- What monthly trends should leadership monitor?

## Project Objectives

- Build a clean, reproducible sales analytics project.
- Demonstrate Python and Pandas data cleaning skills.
- Load cleaned data into a SQLite database.
- Write SQL queries for KPI and business analysis.
- Define Power BI dashboard visuals and DAX measures.
- Communicate insights and recommendations clearly.
- Provide recruiter-friendly documentation for GitHub.

## Tools and Technologies

- **Python**: Data generation, cleaning, and pipeline automation
- **Pandas**: Data transformation and calculated fields
- **NumPy**: Realistic sample data generation
- **SQLite**: Local database for SQL analysis
- **SQL**: KPI reporting and business analysis
- **Power BI**: Dashboard design and KPI visualization planning
- **GitHub**: Portfolio presentation and version control

## Dataset Description

The project includes a generated sales dataset with realistic order-level fields. The cleaned dataset contains **2,500 sales records**.

Main columns:

- `order_id`
- `order_date`
- `customer_id`
- `customer_segment`
- `region`
- `state`
- `product_category`
- `product_name`
- `sales`
- `quantity`
- `discount`
- `profit`

Calculated columns:

- `profit_margin`
- `order_month`
- `average_order_value`
- `year`
- `month_name`

The raw dataset intentionally includes a small number of duplicate rows and missing values so the ETL process can demonstrate realistic cleaning steps.

## ETL Workflow

The ETL workflow is stored in the `scripts/` folder.

### 1. Generate Raw Sales Data

File: `scripts/generate_sales_data.py`

This script creates a reproducible sample sales dataset with realistic regions, states, customer segments, product categories, product names, sales, quantity, discounts, and profit values.

Output:

```text
data/sales_raw.csv
```

### 2. Clean and Transform Data

File: `scripts/etl_clean_sales_data.py`

This script:

- Standardizes column names
- Removes duplicate rows
- Converts dates and numeric fields to correct data types
- Fills missing customer segments
- Fills missing profit values
- Removes records missing required reporting fields
- Creates calculated fields for analysis
- Exports the cleaned dataset

Output:

```text
data/sales_cleaned.csv
```

### 3. Load SQLite Database

File: `scripts/load_sqlite.py`

This script loads the cleaned CSV into SQLite as the `sales_orders` table, creates helpful indexes, and creates optional reporting views from `sql/create_views.sql`.

Output:

```text
data/sales_performance.db
```

### 4. Run Full Pipeline

File: `scripts/run_pipeline.py`

This script runs the full process in one command:

```bash
python scripts/run_pipeline.py
```

## SQL Analysis Summary

SQL queries are stored in:

```text
sql/analysis_queries.sql
```

The SQL analysis includes:

- Total sales
- Total profit
- Total number of orders
- Average order value
- Monthly sales trend
- Sales by region
- Profit by product category
- Top 10 products by sales
- Customer segment performance
- Discount impact on profit
- Low-profit or high-discount products

Optional SQL views are stored in:

```text
sql/create_views.sql
```

## Power BI Dashboard Design

Power BI planning files are stored in the `powerbi/` folder.

Dashboard files:

- `powerbi/dashboard_plan.md`
- `powerbi/dashboard_documentation.md`
- `powerbi/dax_measures.txt`
- `powerbi/powerbi_build_steps.md`

Recommended dashboard visuals:

- KPI cards for Total Sales, Total Profit, Total Orders, and Average Order Value
- Monthly Sales Trend line chart
- Sales by Region bar chart
- Profit by Product Category column chart
- Top 10 Products by Sales bar chart
- Sales by Customer Segment donut chart
- Slicers for Region, Product Category, and Year

## KPI Definitions

| KPI | Definition | Business Purpose |
| --- | --- | --- |
| Total Sales | Sum of all sales revenue | Measures overall revenue performance |
| Total Profit | Sum of all profit | Measures profitability |
| Total Orders | Count of unique order IDs | Measures order volume |
| Average Order Value | Total Sales divided by Total Orders | Measures average revenue per order |
| Profit Margin | Total Profit divided by Total Sales | Shows how efficiently sales convert to profit |
| Total Quantity | Sum of all units sold | Measures product volume |
| Sales YoY Growth | Year-over-year sales change | Tracks annual revenue growth |
| Profit YoY Growth | Year-over-year profit change | Tracks annual profitability growth |

## Key Business Insights

Based on the cleaned dataset:

- Total sales are **$4,372,029.21** across **2,500 orders**.
- Total profit is **$777,823.53**.
- Average order value is **$1,748.81**.
- Overall profit margin is about **17.79%**.
- The **West** region generates the highest sales at **$1,373,327.38**.
- **Technology** is the strongest category, producing **$2,613,005.91** in sales and **$535,646.17** in profit.
- The **Consumer** segment leads revenue with **$2,045,826.33** in sales.
- The top sales product is **Noise-Canceling Headset**, with **$635,537.53** in sales.
- High-discount orders produce almost no profit, showing that aggressive discounting may hurt profitability.

## Business Recommendations

- Focus growth efforts on Technology products because they generate the highest sales and profit.
- Continue investing in the West region because it is the top revenue contributor.
- Review high-discount promotions because heavy discounting is nearly eliminating profit.
- Monitor profit margin along with sales so revenue growth does not hide margin risk.
- Protect the Consumer segment while identifying ways to expand Corporate accounts.
- Use monthly sales trends to plan inventory, staffing, and promotions around peak periods.

## Folder Structure

```text
Sales_Performance_Analytics_Dashboard/
|-- data/
|   |-- sales_raw.csv
|   |-- sales_cleaned.csv
|   |-- sales_performance.db
|-- powerbi/
|   |-- dashboard_documentation.md
|   |-- dashboard_plan.md
|   |-- dax_measures.txt
|   |-- powerbi_build_steps.md
|-- screenshots/
|   |-- README.md
|-- scripts/
|   |-- generate_sales_data.py
|   |-- etl_clean_sales_data.py
|   |-- load_sqlite.py
|   |-- run_pipeline.py
|-- sql/
|   |-- analysis_queries.sql
|   |-- create_views.sql
|-- .gitignore
|-- README.md
|-- requirements.txt
|-- SUBMISSION_NOTES.md
|-- video_walkthrough_script.md
```

## How to Run the Project

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the full pipeline:

```bash
python scripts/run_pipeline.py
```

This generates:

- `data/sales_raw.csv`
- `data/sales_cleaned.csv`
- `data/sales_performance.db`

## How to Open or Build the Dashboard

1. Open Power BI Desktop.
2. Select **Get Data**.
3. Choose **Text/CSV**.
4. Load `data/sales_cleaned.csv`.
5. Rename the table to `sales_cleaned`.
6. Create the DAX measures listed in `powerbi/dax_measures.txt`.
7. Build visuals using `powerbi/dashboard_plan.md`.
8. Use `powerbi/dashboard_documentation.md` to explain the dashboard.
9. Save the Power BI file as:

```text
powerbi/Sales_Performance_Analytics_Dashboard.pbix
```

10. Export screenshots into the `screenshots/` folder.

## Future Improvements

- Build and attach the final Power BI `.pbix` file.
- Add dashboard screenshots to the `screenshots/` folder.
- Add automated data quality tests with `pytest`.
- Add a date dimension table for more advanced Power BI time intelligence.
- Connect the dashboard to a production database such as PostgreSQL or Azure SQL.
- Add revenue forecasting for future monthly sales.
- Publish the dashboard to Power BI Service.

##Conclusion
The Sales Performance Analytics Dashboard project demonstrates a complete Data Analyst workflow from raw data preparation to business insight generation. Using Python, Pandas, SQLite, SQL, and Power BI planning, this project shows how sales data can be cleaned, transformed, analyzed, and presented in a way that supports better decision-making.

The analysis highlights key performance areas such as total sales, profit, regional performance, product category profitability, customer segment behavior, monthly sales trends, and discount impact. The findings show how data can help identify high-performing regions and products while also revealing risks such as heavy discounting reducing profitability.

Overall, this project reflects my ability to work with data end to end, build clear KPI reporting, communicate business insights, and create analytics solutions that are practical, professional, and useful for stakeholders.

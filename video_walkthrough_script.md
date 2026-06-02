# 5-10 Minute Video Walkthrough Script

## 1. Introduction

Hello, my name is [Your Name], and this is my **Sales Performance Analytics Dashboard** project prepared for a Data Analyst role submission at Daxwell.

This project demonstrates an end-to-end analytics workflow using Python, Pandas, SQLite, SQL, and Power BI dashboard planning. The goal is to show how raw sales data can be cleaned, analyzed, visualized, and translated into business recommendations.

## 2. Business Problem

The business problem is that sales leadership needs a clear way to monitor sales performance, profitability, regional performance, product performance, customer segment behavior, and discount impact.

If leadership only looks at total sales, they may miss important risks such as high-discount orders that generate revenue but reduce profit. This dashboard is designed to help stakeholders make better decisions using both revenue and profitability metrics.

## 3. Project Structure

The project is organized into several folders.

The `data` folder contains the raw sales data, cleaned sales data, and SQLite database.

The `scripts` folder contains the Python pipeline files:

- `generate_sales_data.py`
- `etl_clean_sales_data.py`
- `load_sqlite.py`
- `run_pipeline.py`

The `sql` folder contains SQL analysis queries and reporting views.

The `powerbi` folder contains the dashboard plan, dashboard documentation, DAX measures, and build steps.

The `screenshots` folder is reserved for dashboard screenshots after the Power BI report is built.

The README gives a full project overview, business problem, tools, workflow, insights, recommendations, and run instructions.

## 4. Dataset Explanation

The dataset contains 2,500 cleaned order-level sales records from 2023 through 2025.

Important fields include order ID, order date, customer ID, customer segment, region, state, product category, product name, sales, quantity, discount, and profit.

The ETL process also creates calculated fields, including profit margin, order month, average order value, year, and month name.

These fields support KPI reporting, SQL analysis, and Power BI dashboard visuals.

## 5. Python ETL Explanation

The Python workflow starts with `generate_sales_data.py`. This file generates a realistic sales dataset with regions, products, customer segments, sales, discounts, and profit.

It also adds a few realistic data quality issues, such as duplicate rows and missing values, so the cleaning step has meaningful work to do.

Next, `etl_clean_sales_data.py` loads the raw CSV file. It standardizes column names, removes duplicates, converts dates and numeric fields, fills missing values, removes unusable records, and creates calculated fields.

Finally, `load_sqlite.py` loads the cleaned CSV into a SQLite database table named `sales_orders`. It also creates indexes and reporting views to make SQL analysis easier.

The full pipeline can be run with one command:

```bash
python scripts/run_pipeline.py
```

## 6. SQLite and SQL Analysis Explanation

The SQL analysis is stored in `sql/analysis_queries.sql`.

The queries calculate total sales, total profit, total orders, average order value, monthly sales trend, sales by region, profit by product category, top 10 products, customer segment performance, discount impact on profit, and low-profit or high-discount products.

These queries are written as business questions, which makes the analysis easier to explain to stakeholders.

For example, the discount impact query groups orders into discount bands and compares sales, profit, and profit margin. This helps determine whether discounting is improving performance or hurting profitability.

## 7. Power BI Dashboard Explanation

The dashboard plan is documented in `powerbi/dashboard_plan.md`, and the detailed explanation is in `powerbi/dashboard_documentation.md`.

The dashboard includes four KPI cards:

- Total Sales
- Total Profit
- Total Orders
- Average Order Value

The main visuals include:

- Monthly Sales Trend line chart
- Sales by Region bar chart
- Profit by Product Category column chart
- Top 10 Products by Sales bar chart
- Sales by Customer Segment donut chart

The dashboard also includes slicers for Region, Product Category, and Year. These filters allow users to explore the data interactively.

DAX measures are stored in `powerbi/dax_measures.txt`. These include Total Sales, Total Profit, Total Orders, Average Order Value, Profit Margin, Total Quantity, Sales YoY Growth, and Profit YoY Growth.

## 8. Key Insights

The cleaned dataset shows total sales of about $4.37 million across 2,500 orders.

Total profit is about $777.8 thousand, and the average order value is about $1,748.81.

The West region generates the highest sales, with about $1.37 million.

Technology is the strongest product category, producing about $2.61 million in sales and about $535.6 thousand in profit.

The Consumer segment generates the highest sales, with about $2.05 million.

The top sales product is Noise-Canceling Headset, followed by other Technology products.

The discount analysis shows that high-discount orders produce almost no profit, which is a major business concern.

## 9. Business Recommendations

Based on the analysis, I would recommend that the company continue investing in Technology products because they generate the highest sales and profit.

I would also recommend prioritizing the West region because it is the strongest revenue contributor.

For discounting, I would recommend reviewing high-discount promotions and setting stronger approval rules. The analysis shows that heavy discounting can create revenue while nearly eliminating profit.

I would also recommend tracking profit margin alongside sales so leadership can avoid mistaking unprofitable revenue growth for healthy growth.

## 10. Conclusion

This project demonstrates the full Data Analyst workflow: data generation, data cleaning, ETL, database loading, SQL analysis, KPI reporting, dashboard planning, business insights, and recommendations.

It shows both technical skills and business communication skills, which are important for a Data Analyst role.

Thank you for reviewing my Sales Performance Analytics Dashboard project.

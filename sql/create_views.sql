/*
Optional SQLite views for easier Power BI importing.
Run these after loading data/sales_performance.db.
*/

CREATE VIEW IF NOT EXISTS vw_kpi_summary AS
SELECT
    ROUND(SUM(sales), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(sales) / COUNT(DISTINCT order_id), 2) AS average_order_value,
    ROUND(SUM(profit) / NULLIF(SUM(sales), 0), 4) AS profit_margin
FROM sales_orders;

CREATE VIEW IF NOT EXISTS vw_monthly_sales_trend AS
SELECT
    order_month,
    ROUND(SUM(sales), 2) AS monthly_revenue,
    ROUND(SUM(profit), 2) AS monthly_profit,
    COUNT(DISTINCT order_id) AS monthly_orders
FROM sales_orders
GROUP BY order_month;

CREATE VIEW IF NOT EXISTS vw_category_performance AS
SELECT
    product_category,
    ROUND(SUM(sales), 2) AS revenue,
    ROUND(SUM(profit), 2) AS profit,
    SUM(quantity) AS units_sold,
    ROUND(SUM(profit) / NULLIF(SUM(sales), 0), 4) AS profit_margin
FROM sales_orders
GROUP BY product_category;

CREATE VIEW IF NOT EXISTS vw_region_performance AS
SELECT
    region,
    state,
    ROUND(SUM(sales), 2) AS revenue,
    ROUND(SUM(profit), 2) AS profit,
    ROUND(SUM(profit) / NULLIF(SUM(sales), 0), 4) AS profit_margin
FROM sales_orders
GROUP BY region, state;

CREATE VIEW IF NOT EXISTS vw_discount_impact AS
SELECT
    CASE
        WHEN discount = 0 THEN 'No Discount'
        WHEN discount <= 0.10 THEN 'Low Discount'
        WHEN discount <= 0.20 THEN 'Medium Discount'
        ELSE 'High Discount'
    END AS discount_band,
    ROUND(AVG(discount), 3) AS average_discount,
    ROUND(SUM(sales), 2) AS revenue,
    ROUND(SUM(profit), 2) AS profit,
    ROUND(SUM(profit) / NULLIF(SUM(sales), 0), 4) AS profit_margin
FROM sales_orders
GROUP BY discount_band;

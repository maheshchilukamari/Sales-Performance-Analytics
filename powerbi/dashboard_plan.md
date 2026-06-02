# Power BI Dashboard Plan

## Dashboard Header

**Sales Performance Analytics Dashboard**

Subtitle: Regional, product, customer segment, and profitability performance.

Recommended top-level layout:

```text
| Sales Performance Analytics Dashboard                         |
| Region Slicer | Product Category Slicer | Year Slicer          |
| Total Sales | Total Profit | Total Orders | Average Order Value |
| Monthly Sales Trend                                           |
| Sales by Region              | Profit by Product Category      |
| Top 10 Products by Sales     | Sales by Customer Segment       |
```

## Data Source

Load the cleaned CSV into Power BI:

```text
data/sales_cleaned.csv
```

Rename the imported table to:

```text
sales_cleaned
```

## KPI Cards

Place four KPI cards across the top of the dashboard.

| KPI Card | Measure | Purpose |
| --- | --- | --- |
| Total Sales | `[Total Sales]` | Shows total revenue generated |
| Total Profit | `[Total Profit]` | Shows total profitability |
| Total Orders | `[Total Orders]` | Shows order volume |
| Average Order Value | `[Average Order Value]` | Shows average revenue per order |

## Visual 1: Monthly Sales Trend

- Visual type: Line chart
- X-axis: `order_month`
- Y-axis: `[Total Sales]`
- Tooltip: `[Total Profit]`, `[Profit Margin]`, `[Total Orders]`
- Business question: How are sales trending month over month?

## Visual 2: Sales by Region

- Visual type: Horizontal bar chart
- Axis: `region`
- Values: `[Total Sales]`
- Tooltip: `[Total Profit]`, `[Profit Margin]`
- Sort: Descending by `[Total Sales]`
- Business question: Which regions generate the most sales?

## Visual 3: Profit by Product Category

- Visual type: Column chart
- Axis: `product_category`
- Values: `[Total Profit]`
- Tooltip: `[Total Sales]`, `[Profit Margin]`
- Sort: Descending by `[Total Profit]`
- Business question: Which categories are most profitable?

## Visual 4: Top 10 Products by Sales

- Visual type: Horizontal bar chart
- Axis: `product_name`
- Values: `[Total Sales]`
- Filter: Top 10 products by `[Total Sales]`
- Tooltip: `product_category`, `[Total Profit]`, `[Total Quantity]`
- Business question: Which products drive the most revenue?

## Visual 5: Sales by Customer Segment

- Visual type: Donut chart
- Legend: `customer_segment`
- Values: `[Total Sales]`
- Tooltip: `[Total Profit]`, `[Average Order Value]`, `[Profit Margin]`
- Business question: Which customer segments contribute the most sales?

## Slicers

Add slicers near the top of the dashboard:

- `region`
- `product_category`
- `year`

Optional slicers:

- `customer_segment`
- `order_date`

## Recommended Formatting

- Use a clean white or light gray report canvas.
- Use blue for sales, green for profit, and orange/red only for discount or margin risk.
- Format sales, profit, and average order value as currency.
- Format profit margin and growth measures as percentages.
- Sort charts from highest to lowest for easier scanning.
- Keep labels concise and dashboard spacing consistent.

## Dashboard Story

1. Start with KPI cards to show overall sales health.
2. Review monthly sales trend to identify growth or seasonality.
3. Compare regions to locate the strongest markets.
4. Compare product categories to understand profitability.
5. Review top products to identify revenue drivers.
6. Review customer segments to guide sales strategy.
7. Use slicers to explore performance by region, category, and year.

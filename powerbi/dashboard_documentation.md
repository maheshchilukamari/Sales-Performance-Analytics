# Dashboard Documentation

## Dashboard Purpose

The Sales Performance Analytics Dashboard helps sales leaders monitor revenue, profit, order volume, customer segment performance, product performance, and discount impact. It turns order-level sales data into executive-level metrics and visual insights.

## Target Audience

- Sales leadership
- Regional sales managers
- Business analysts
- Finance and operations stakeholders
- Recruiters or hiring managers reviewing this Data Analyst portfolio project

## Dashboard Layout

The dashboard is designed as a single-page executive summary.

Top section:

- Dashboard title
- Region slicer
- Product category slicer
- Year slicer
- KPI cards

Middle section:

- Monthly Sales Trend line chart
- Sales by Region bar chart
- Profit by Product Category column chart

Bottom section:

- Top 10 Products by Sales bar chart
- Sales by Customer Segment donut chart

## KPI Cards Explanation

### Total Sales

Shows total revenue generated from all orders. This is the primary top-line performance metric.

### Total Profit

Shows total profit after discounts and product margin assumptions. This helps leadership evaluate financial health beyond sales volume.

### Total Orders

Counts unique order IDs. This shows order activity and demand volume.

### Average Order Value

Calculates total sales divided by total orders. This helps compare customer purchasing behavior across regions, categories, and years.

## Visual-by-Visual Explanation

### Monthly Sales Trend

Shows sales by month. This helps identify seasonal patterns, sales peaks, slower periods, and changes over time.

### Sales by Region

Compares sales across regions. This helps managers identify which regions are strongest and which may need sales support.

### Profit by Product Category

Compares total profit across product categories. This helps leadership focus on categories that contribute the most financial value.

### Top 10 Products by Sales

Ranks products by sales. This helps identify the products that drive the largest share of revenue.

### Sales by Customer Segment

Shows the share of sales across Consumer, Corporate, Home Office, and Unknown segments. This supports customer strategy and segmentation decisions.

## Filters and Slicers

The dashboard includes slicers for:

- `region`
- `product_category`
- `year`

These slicers allow business users to filter every visual and answer more specific questions, such as how Technology sales performed in the West region during 2025.

## DAX Measures Explanation

The dashboard uses DAX measures from `powerbi/dax_measures.txt`.

Core measures:

- `Total Sales`: Sums the `sales` column.
- `Total Profit`: Sums the `profit` column.
- `Total Orders`: Counts unique `order_id` values.
- `Average Order Value`: Divides total sales by total orders.
- `Profit Margin`: Divides total profit by total sales.
- `Total Quantity`: Sums units sold.
- `Sales YoY Growth`: Compares sales to the previous year.
- `Profit YoY Growth`: Compares profit to the previous year.

## Business Questions Answered

- What is the company's total sales performance?
- How profitable are sales overall?
- Which regions generate the most sales?
- Which product categories generate the most profit?
- Which products are the strongest revenue drivers?
- Which customer segments contribute most to sales?
- How are monthly sales trending?
- Are discounts helping revenue but hurting profitability?

## How the Dashboard Supports Decision-Making

The dashboard supports decision-making by connecting high-level KPIs with drill-down visuals. Leaders can quickly identify strong regions, profitable categories, top products, and customer segment opportunities. The dashboard also highlights discount-related profit risk so the business can adjust promotional strategy before margin erosion becomes a larger problem.

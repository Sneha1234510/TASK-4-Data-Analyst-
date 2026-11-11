# Sales Data Visualization and Storytelling

## Project objective
Analyze a sample retail sales dataset and communicate business patterns through clear charts and concise insights.

## Dataset
- File: `data/sales_data.csv`
- Records: 500
- Fields: Order ID, Order Date, Region, Segment, Category, Product, Quantity, Sales, Profit
- **Important:** This is a reproducible, synthetic practice dataset created for this project. It is not real company data and should not be represented as actual Superstore data.

## Key performance indicators
| Metric | Result |
|---|---:|
| Total sales | 505,965.92 |
| Total profit | 44,710.77 |
| Number of orders | 500 |
| Average sales per order | 1,011.93 |
| Orders with negative profit | 154 |

## Visual findings
1. **Category performance:** Technology contributes the highest total sales in this sample.
2. **Regional performance:** Central is the leading region by sales.
3. **Sales over time:** The monthly trend chart helps identify peaks and quieter periods that may need further investigation.
4. **Customer segment profitability:** Consumer has the highest total profit among the three segments.

## Business recommendations
- Review the strongest category and region to understand which products and practices are driving results.
- Investigate months with unusually high or low sales before changing inventory or marketing plans.
- Review loss-making orders to understand whether discounts, costs, or product mix are reducing profit.
- Compare sales and profit together; high sales alone do not guarantee strong profitability.

## Method
The analysis uses Python, pandas, and Matplotlib. The charts use bar charts for category/region/segment comparisons and a line chart for the monthly trend.

## Limitations
The data is randomly generated for learning. The findings demonstrate a visualization workflow only and should not be used for real business decisions.

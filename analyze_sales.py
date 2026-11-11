"""
Task 2: Data Visualization and Storytelling
Run from the project root:
    pip install -r requirements.txt
    python src/analyze_sales.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sales_data.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["Order Date"])
required = {"Order ID", "Order Date", "Region", "Segment", "Category", "Product",
            "Quantity", "Sales", "Profit"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")

print("SALES SUMMARY")
print(f"Total sales: {df['Sales'].sum():,.2f}")
print(f"Total profit: {df['Profit'].sum():,.2f}")
print(f"Orders: {df['Order ID'].nunique():,}")
print("\\nSales by category:")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

def save_bar(series, title, xlabel, filename, rotate=0):
    ax = series.sort_values(ascending=False).plot(kind="bar", figsize=(8, 5))
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Amount")
    plt.xticks(rotation=rotate, ha="right" if rotate else "center")
    plt.tight_layout()
    plt.savefig(OUT / filename, dpi=160)
    plt.close()

save_bar(df.groupby("Category")["Sales"].sum(),
         "Total Sales by Product Category", "Category", "sales_by_category.png", 20)
save_bar(df.groupby("Region")["Sales"].sum(),
         "Total Sales by Region", "Region", "sales_by_region.png")
save_bar(df.groupby("Segment")["Profit"].sum(),
         "Total Profit by Customer Segment", "Segment", "profit_by_segment.png")

monthly = (df.set_index("Order Date").resample("MS")["Sales"].sum())
ax = monthly.plot(kind="line", marker="o", figsize=(8, 5))
ax.set_title("Monthly Sales Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
plt.tight_layout()
plt.savefig(OUT / "monthly_sales_trend.png", dpi=160)
plt.close()

print(f"\\nCharts saved to: {OUT}")

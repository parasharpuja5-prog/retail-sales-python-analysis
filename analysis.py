"""
Retail Sales Data Analysis
A beginner-friendly portfolio project using Python, Pandas, and Matplotlib.
Run from the project folder: python analysis.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = PROJECT_DIR / "data" / "retail_sales.csv"
OUTPUT_DIR = PROJECT_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def load_and_clean_data(path: Path) -> pd.DataFrame:
    """Load the sales file and perform basic data-quality checks."""
    df = pd.read_csv(path)
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    df["discount"] = pd.to_numeric(df["discount"], errors="coerce")

    # Remove duplicate orders and rows missing essential fields.
    df = df.drop_duplicates(subset=["order_id"])
    df = df.dropna(subset=["order_id", "order_date", "product", "quantity", "unit_price"])
    df = df[(df["quantity"] > 0) & (df["unit_price"] >= 0)]
    df["discount"] = df["discount"].fillna(0).clip(0, 1)
    df["gross_sales"] = df["quantity"] * df["unit_price"]
    df["revenue"] = df["gross_sales"] * (1 - df["discount"])
    df["month"] = df["order_date"].dt.to_period("M").astype(str)
    return df

def main() -> None:
    df = load_and_clean_data(DATA_PATH)

    total_revenue = df["revenue"].sum()
    total_orders = df["order_id"].nunique()
    total_units = df["quantity"].sum()
    average_order_value = total_revenue / total_orders if total_orders else 0

    category_sales = (
        df.groupby("category", as_index=False)["revenue"]
        .sum().sort_values("revenue", ascending=False)
    )
    product_sales = (
        df.groupby("product", as_index=False)["revenue"]
        .sum().sort_values("revenue", ascending=False)
    )
    monthly_sales = (
        df.groupby("month", as_index=False)["revenue"]
        .sum().sort_values("month")
    )
    region_sales = (
        df.groupby("region", as_index=False)["revenue"]
        .sum().sort_values("revenue", ascending=False)
    )

    # Save reusable summary tables.
    category_sales.to_csv(OUTPUT_DIR / "revenue_by_category.csv", index=False)
    product_sales.to_csv(OUTPUT_DIR / "revenue_by_product.csv", index=False)
    monthly_sales.to_csv(OUTPUT_DIR / "monthly_revenue.csv", index=False)
    region_sales.to_csv(OUTPUT_DIR / "revenue_by_region.csv", index=False)

    print("\\n=== RETAIL SALES SUMMARY ===")
    print(f"Clean orders: {total_orders:,}")
    print(f"Units sold: {total_units:,}")
    print(f"Total revenue: ${total_revenue:,.2f}")
    print(f"Average revenue per order: ${average_order_value:,.2f}")
    print("\\nRevenue by category:")
    print(category_sales.to_string(index=False, formatters={"revenue": "${:,.2f}".format}))
    print("\\nTop 5 products by revenue:")
    print(product_sales.head(5).to_string(index=False, formatters={"revenue": "${:,.2f}".format}))
    print("\\nRevenue by region:")
    print(region_sales.to_string(index=False, formatters={"revenue": "${:,.2f}".format}))

    # Chart 1: revenue by category
    plt.figure(figsize=(8, 5))
    plt.bar(category_sales["category"], category_sales["revenue"])
    plt.title("Revenue by Product Category")
    plt.xlabel("Category")
    plt.ylabel("Revenue ($)")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "revenue_by_category.png", dpi=150)
    plt.close()

    # Chart 2: monthly revenue trend
    plt.figure(figsize=(10, 5))
    plt.plot(monthly_sales["month"], monthly_sales["revenue"], marker="o")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue ($)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "monthly_revenue.png", dpi=150)
    plt.close()

    # Chart 3: revenue by region
    plt.figure(figsize=(8, 5))
    plt.bar(region_sales["region"], region_sales["revenue"])
    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue ($)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "revenue_by_region.png", dpi=150)
    plt.close()

    print(f"\\nCharts and summary tables saved in: {OUTPUT_DIR}")
    print("Note: this portfolio dataset is synthetic and for learning purposes.")

if __name__ == "__main__":
    main()

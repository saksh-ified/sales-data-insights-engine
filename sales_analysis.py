import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("sales_data.csv")

# Create Revenue column
df["Revenue"] = df["Units_Sold"] * df["Price"]

# Total revenue
total_revenue = df["Revenue"].sum()

# Best selling product
best_product = df.groupby("Product")["Units_Sold"].sum().idxmax()

# Category performance
top_category = df.groupby("Category")["Revenue"].sum().idxmax()

# Monthly revenue
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month
monthly_revenue = df.groupby("Month")["Revenue"].sum()

print("📊 SALES REPORT")
print("Total Revenue:", total_revenue)
print("Best Selling Product:", best_product)
print("Top Revenue Category:", top_category)
print("\nMonthly Revenue:")
print(monthly_revenue)
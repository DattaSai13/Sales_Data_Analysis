# Week 3: Sales Data Analysis using Pandas
# Dataset: sales_data.csv
# This program analyzes real sales data and generates insights

import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

print("📊 FIRST 5 ROWS OF DATA")
print(df.head())

# Basic dataset information
print("\n📌 DATASET INFORMATION")
print(df.info())

# -------------------------
# Data Cleaning
# -------------------------

# Check for missing values
print("\n❓ Missing Values")
print(df.isnull().sum())

# (Dataset has no missing values, but this is good practice)
df.fillna(0, inplace=True)

# Remove duplicates if any
df.drop_duplicates(inplace=True)

# -------------------------
# Data Analysis
# -------------------------

# 1. Total Revenue
total_revenue = df["Total_Sales"].sum()

# 2. Average Sales Value
average_sales = df["Total_Sales"].mean()

# 3. Highest Sale Value
highest_sale = df["Total_Sales"].max()

# 4. Best-Selling Product (by total sales)
best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

# 5. Best Performing Region
best_region = df.groupby("Region")["Total_Sales"].sum().idxmax()

# -------------------------
# Report
# -------------------------

print("\n📈 SALES ANALYSIS REPORT")
print("----------------------------")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Average Sales Value: ₹{average_sales:,.2f}")
print(f"Highest Single Sale: ₹{highest_sale:,.2f}")
print(f"Best Selling Product: {best_product}")
print(f"Top Performing Region: {best_region}")
print("----------------------------")

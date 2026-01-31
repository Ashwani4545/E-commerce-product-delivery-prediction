# 🟢 PHASE-1:- Data Preparation
# Goal: Convert raw e-commerce orders data into an ML-ready dataset.

# STEP 1: Load the dataset
import pandas as pd
df = pd.read_csv(r"C:\Users\DELL\Desktop\E-commerce-preoduct-delivery-prediction\ecommerce_orders_clean.csv")
# Quick inspection
df.head()

# STEP 2: Understand the Dataset
# Dataset info
df.info()
# Missing values count
df.isnull().sum()


# STEP 3: Handle Missing Values
# Separate numerical and categorical columns
num_cols = df.select_dtypes(include=["int64", "float64"]).columns
cat_cols = df.select_dtypes(include=["object"]).columns
# Fill numerical columns with median
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())
# Fill categorical columns with mode
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])
    
    
# Step-4 Convert Date Columns
# Convert date columns to datetime
df["order_date"] = pd.to_datetime(df["order_date"])
df["shipping_date"] = pd.to_datetime(df["shipping_date"])


# STEP 5: Create delivery_days
# Calculate delivery duration
df["delivery_days"] = (df["shipping_date"] - df["order_date"]).dt.days


# STEP 6: Create Target Variable delivery_delayed
# Define SLA threshold
SLA_DAYS = 5
# Create target variable
df["delivery_delayed"] = df["delivery_days"].apply(
    lambda x: 1 if x > SLA_DAYS else 0
)


# STEP 7: Final Validation
# Check the final structure
df.info()
# Check target distribution
df["delivery_delayed"].value_counts(normalize=True) * 100


# STEP 8: Save the Cleaned Dataset
df.to_csv("ecommerce_orders_processed.csv", index=False)

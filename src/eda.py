# STEP 1: Basic Sanity Checks
# Target distribution
df["delivery_delayed"].value_counts(normalize=True)*100


# STEP 2: Delivery Delays by Product Category
# Check actual column names
print(df.columns.tolist())

# Fix extra spaces in column names
df.columns = df.columns.str.strip()

# Group by category and calculate delay rate
category_delay = (
    df.groupby("category")["delivery_delayed"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)
category_delay.columns = ["category", "delay_rate"]
print(category_delay)

# Confirm delivery_delayed exists
print("delivery_delayed" in df.columns)

# Visualization
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
sns.barplot(data=category_delay, x="category", y="delay_rate")
plt.xticks(rotation=45)
plt.title("Delivery Delay Rate by Product Category")
plt.ylabel("Delay Rate")
plt.show()


# STEP 3: Customer Segment vs Delivery Delay
segment_delay = (
    df.groupby("customer_segment")["delivery_delayed"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)
segment_delay

# Visualization
plt.figure(figsize=(8,5))
sns.barplot(data=segment_delay, x="customer_segment", y="delivery_delayed")
plt.title("Delivery Delay by Customer Segment")
plt.show()


# STEP 4: Channel Impact on Delivery Delay
channel_delay = (
    df.groupby("channel")["delivery_delayed"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)
channel_delay

# Visualization
plt.figure(figsize=(8,5))
sns.barplot(data=channel_delay, x="channel", y="delivery_delayed")
plt.title("Delivery Delay by Order Channel")
plt.show()


# STEP 5: Device Type Impact
device_delay = (
    df.groupby("device_type")["delivery_delayed"]
    .mean()
    .reset_index()
)
device_delay

# Visualization
plt.figure(figsize=(8,5))
sns.barplot(data=device_delay, x="device_type", y="delivery_delayed")
plt.title("Delivery Delay by Device Type")
plt.show()


# STEP 6: Cross Analysis
pivot = pd.pivot_table(
    df,
    values="delivery_delayed",
    index="category",
    columns="channel",
    aggfunc="mean"
)
pivot


# STEP 7: Document Business Insights
# Insight 1: Category Risk
# Electronics and bulky products have higher delay probability due to handling and shipment complexity.

# Insight 2: Customer Behavior
# Loyal customers experience fewer delays, indicating better logistics prioritization.

# Insight 3: Channel Surge Effect
# Campaign-driven channels increase delays due to sudden demand spikes.

# Insight 4: Device Influence
# Mobile-based orders show slightly higher delays, likely due to flash-sale behavior.


# STEP 8: Save EDA Outputs
category_delay.to_csv("eda_category_delay.csv", index=False)
segment_delay.to_csv("eda_segment_delay.csv", index=False)
channel_delay.to_csv("eda_channel_delay.csv", index=False)
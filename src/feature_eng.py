# 🟢 PHASE 3: Feature Engineering
# Goal: Convert raw columns into high-signal features that help the model predict delivery delays accurately.
# We will create 4 features and then build a preprocessing pipeline.


# STEP 1: Create order_value
# Create order value
df["order_value"] = df["price"] * df["quantity"]


# STEP 2: Create Day-of-Week Feature
# Day of week (0=Monday, 6=Sunday)
df["order_dayofweek"] = df["order_date"].dt.dayofweek

# Readable version for EDA
df["order_day_name"] = df["order_date"].dt.day_name()


# STEP 3: Create Month / Seasonality Features
# Month number
df["order_month"] = df["order_date"].dt.month

# Optional Advanced Season Feature
df["is_peak_season"] = df["order_month"].isin([10, 11, 12]).astype(int)


# STEP 4: Create Customer Risk Score
# Step 4.1: Calculate Historical Delay Rate per Customer
customer_delay_rate = (
    df.groupby("customer_id")["delivery_delayed"]
    .mean()
    .reset_index()
    .rename(columns={"delivery_delayed": "customer_delay_rate"})
)

# Step 4.2: Merge Back into Main Dataset
df = df.merge(customer_delay_rate, on="customer_id", how="left")

# Step 4.3: Create Customer Risk Score
df["customer_risk_score"] = df["customer_delay_rate"]


# STEP 5: Drop Leakage Columns
df = df.drop(columns=["shipping_date", "delivery_days", "customer_delay_rate"])


# STEP 6: Define Features & Target
X = df.drop(columns=["delivery_delayed"])
y = df["delivery_delayed"]


# STEP 7: Build Preprocessing Pipeline
# Step 7.1: Identify Feature Types
from sklearn.model_selection import train_test_split

num_features = [
    "price", "quantity", "order_value",
    "order_dayofweek", "order_month",
    "customer_risk_score"
]

cat_features = [
    "category",
    "customer_segment",
    "channel",
    "device_type"
]

# Step 7.2: Create Transformers
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

numeric_transformer = StandardScaler()

categorical_transformer = OneHotEncoder(
    handle_unknown="ignore",
    sparse_output=False
)

# Step 7.3: Build ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, num_features),
        ("cat", categorical_transformer, cat_features)
    ]
)


# STEP 8: Combine Preprocessing + Model
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

model_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", RandomForestClassifier(
            n_estimators=200,
            random_state=42
        ))
    ]
)
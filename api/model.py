# Step 1.2: Load Model (api/model.py)
import joblib
import os

# Trying the multiple possible paths with environment variable support
MODEL_PATH_ENV = os.getenv("MODEL_PATH", None)

POSSIBLE_PATHS = []
if MODEL_PATH_ENV:
    POSSIBLE_PATHS.append(MODEL_PATH_ENV)

# default fallback paths
POSSIBLE_PATHS.extend([
    "model/delivery_deay_model.pkl",
    "delivery_delay_model.pkl",
    "model/delivery_delay_model.pkl",
    "../model/delivery_deay_model.pkl",
    "../delivery_delay_model.pkl",
])

def load_model():
    for path in POSSIBLE_PATHS:
        if os.path.exists(path):
            print(f" Loading model from: {path}")
            return joblib.load(path)
    raise FileNotFoundError(f"Model file not found. Checked paths: {POSSIBLE_PATHS}")

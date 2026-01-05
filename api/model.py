# Step 1.2: Load Model (api/model.py)
import joblib
import os

# Try multiple possible paths
POSSIBLE_PATHS = [
    "delivery_delay_model.pkl",
    "model/delivery_delay_model.pkl",
    "../delivery_delay_model.pkl",
    "model/delivery_deay_model.pkl",
    "../model/delivery_deay_model.pkl"
]

def load_model():
    for path in POSSIBLE_PATHS:
        if os.path.exists(path):
            print(f"Loading model from: {path}")
            return joblib.load(path)
    raise FileNotFoundError(f"Model file not found in any of these locations: {POSSIBLE_PATHS}")

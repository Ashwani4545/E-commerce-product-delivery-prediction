from fastapi import FastAPI
from api.schemas import PredictionInput
from api.model import load_model
import pandas as pd

app = FastAPI(title="E-Commerce Delivery Delay Prediction API")

model = None  # placeholder

@app.on_event("startup")
def startup_event():
    global model
    model = load_model()
    print("✅ Model loaded successfully")

@app.post("/predict")
def predict_delay(data: PredictionInput):
    data_dict = data.dict()

    # Calculate order_value if missing
    if data_dict.get("order_value") is None:
        data_dict["order_value"] = data_dict["price"] * data_dict["quantity"]

    input_df = pd.DataFrame([data_dict])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    return {
        "delivery_delayed": int(prediction),
        "delay_probability": round(float(probability), 3)
    }

@app.get("/")
def read_root():
    return {
        "message": "E-Commerce Delivery Delay Prediction API",
        "docs": "/docs"
    }

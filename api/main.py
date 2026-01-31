from fastapi import FastAPI
from api.schemas import PredictionInput
from api.model import load_model
import pandas as pd

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


app = FastAPI(title="E-Commerce Delivery Delay Prediction API")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # change later for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = None  # placeholder


@app.on_event("startup")
def startup_event():
    global model
    model = load_model()
    logger.info("✅ Model loaded successfully")


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
logger.info(f"Prediction requested with data: {input_data}")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def read_root():
    return {
        "message": "E-Commerce Delivery Delay Prediction API",
        "docs": "/docs"
    }

from fastapi import FastAPI
from api.schemas import PredictionInput
from api.model import load_model

import pandas as pd
import logging

# ---------------------------------------------------
# Logging Configuration
# ---------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# ---------------------------------------------------
# FastAPI App
# ---------------------------------------------------
app = FastAPI(
    title="E-Commerce Delivery Delay Prediction API",
    description="Predicts whether an e-commerce order will be delayed",
    version="1.0.0"
)

# ---------------------------------------------------
# CORS Middleware
# ---------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------
# Load ML Model on Startup
# ---------------------------------------------------
model = None  # sklearn pipeline


@app.on_event("startup")
def startup_event():
    global model
    model = load_model()
    logger.info("✅ ML model loaded successfully")

# ---------------------------------------------------
# Prediction Endpoint
# ---------------------------------------------------
@app.post("/predict")
def predict_delay(data: PredictionInput):
    data_dict = data.dict()

    # Calculate order_value if not provided
    if data_dict.get("order_value") is None:
        data_dict["order_value"] = data_dict["price"] * data_dict["quantity"]

    logger.info(f"Prediction request received: {data_dict}")

    input_df = pd.DataFrame([data_dict])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    return {
        "delivery_delayed": int(prediction),
        "delay_probability": round(float(probability), 3)
    }

# ---------------------------------------------------
# Health Check Endpoint
# ---------------------------------------------------
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# ---------------------------------------------------
# Root Endpoint
# ---------------------------------------------------
@app.get("/")
def root():
    return {
        "message": "E-Commerce Delivery Delay Prediction API",
        "docs": "/docs"
    }

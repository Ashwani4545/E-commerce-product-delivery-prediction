# E-Commerce Delivery Delay Prediction

## Project Overview

Timely delivery is a critical success factor in e-commerce. Late deliveries increase refunds, reduce customer trust, and raise operational costs.
This project builds an end-to-end, production-ready system to predict whether an order will be delivered on time or delayed, using historical e-commerce order data.

The solution combines machine learning, MLOps automation, APIs, dashboards, and cloud-ready deployment to support proactive logistics decision-making.

## Project Structure
```
.
├── api/                    # FastAPI backend
│   ├── main.py            # API endpoints
│   ├── model.py           # Model loading
│   └── schemas.py         # Pydantic schemas
├── app/                   # Frontend
│   └── streamlit_app.py   # Streamlit UI
├── model/                 # Saved models
├── data/                  # Data files
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
### 1. Start FastAPI Server
```bash
cd C:\Users\DELL\Desktop\E-commerce-preoduct-delivery-prediction
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

API will be available at:
- API: http://localhost:8000
- Swagger Docs: http://localhost:8000/docs

### 2. Start Streamlit App (in a new terminal)
```bash
streamlit run app/streamlit_app.py
```

App will open at: http://localhost:8501

## API Usage Example

```python
import requests

payload = {
    "price": 29.99,
    "quantity": 2,
    "category": "Electronics",
    "customer_segment": "Regular",
    "channel": "Direct",
    "device_type": "Mobile",
    "order_dayofweek": 1,
    "order_month": 11,
    "customer_risk_score": 0.3
}

response = requests.post("http://localhost:8000/predict", json=payload)
print(response.json())
```

## Model Training

See `mainFile.ipynb` for complete training pipeline including:
- Data preparation
- EDA
- Feature engineering
- Model training & tuning
- MLOps integration

## Features

- **Real-time predictions**: FastAPI REST API
- **Interactive UI**: Streamlit web app
- **ML Pipeline**: Complete end-to-end workflow
- **MLOps**: MLflow tracking, Airflow automation, Evidently drift detection

## Tech Stack

- **ML**: scikit-learn, XGBoost
- **API**: FastAPI, Uvicorn
- **UI**: Streamlit
- **MLOps**: MLflow, Airflow, Evidently
- **Data**: pandas, numpy

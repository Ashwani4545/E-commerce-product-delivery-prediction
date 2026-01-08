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

## 🎯 Business Problem

E-commerce companies face:
- Unpredictable delivery delays
- No early warning system for risky orders
- Poor visibility into delay drivers (category, customer, channel)
- Reactive logistics planning
- Increased operational costs and customer dissatisfaction

## ✅ Solution

This project provides:
- Early prediction of delivery delays
- Business insights into why delays occur
- Automated ML pipelines (MLOps)
- Real-time predictions via API & UI
- Interactive dashboards for stakeholders

## 📂 Dataset
#### Final Dataset Used: ``` ecommerce_orders_clean.csv ```

### Key Characteristics

- Order-level e-commerce data
- Order & shipping dates
- Product, customer, channel, and device information
- Suitable for ML, visualization, and MLOps

### Engineered Targets

- delivery_days = shipping_date − order_date
delivery_delayed (target):
  - 0 → Delivered on time
  - 1 → Delivery delayed (SLA > 5 days)

## 🧠 Features Engineered

- Order value (price × quantity)
- Day of week
- Month / seasonality
- Customer risk score (historical delay behavior)
- Product category
- Customer segment
- Order channel
- Device type

## 🧪 Machine Learning
### Models Trained

- Logistic Regression (baseline)
- Decision Tree
- Random Forest (tuned & selected)
- XGBoost (optional comparison)

### Evaluation Metric

- F1-Score (handles class imbalance)

### Final Model

- Tuned Random Forest
- Saved as a single deployable pipeline (.pkl) including preprocessing

## 🔁 MLOps Architecture

The project follows a full ML lifecycle:
```
Data → Feature Engineering → Training → Evaluation
     → Model Registry → Deployment → Monitoring → Retraining
```
### MLOps Tools

- MLflow – experiment tracking & model registry
- Apache Airflow / Prefect – automated training pipelines
- Evidently AI – data & concept drift detection
- GitHub Actions – CI/CD (optional)

## 🌐 API & Application
### Backend

- FastAPI
- Input validation using Pydantic
- Real-time predictions

### Frontend

- Streamlit
- Business-friendly UI for non-technical users

### Output

- Delivery prediction (On-time / Delayed)
- Delay probability score

## 📊 Visualization & Dashboards

Interactive dashboards were built using Power BI / Tableau.

### Dashboards Included
#### 1️⃣ Delivery Performance

-On-time vs delayed orders
-Average delivery days
-SLA breach rate

#### 2️⃣ Delay Trends

-Monthly & seasonal delay patterns
-Weekday vs weekend analysis

#### 3️⃣ Customer Behavior

-Delay rate by customer segment
-Channel & device impact
-Customer risk score analysis
-Screenshots are embedded below 👇

## 📸 Dashboard Snapshots
### Delivery Performance
### Delay Trends
### Customer Behavior

## 🧱 Tech Stack (Final)
### Data & ML

-Python, Pandas, NumPy
-Scikit-learn
-XGBoost

### MLOps

-MLflow
-Airflow / Prefect
-Evidently AI

### API & UI

-FastAPI
-Streamlit

### Visualization

-Power BI / Tableau

### Deployment
-Docker
-Streamlit Cloud / Hugging Face Spaces
-AWS (S3, EC2, ECS – optional)

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

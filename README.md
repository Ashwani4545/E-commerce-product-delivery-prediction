# 🚚 E-Commerce Delivery Delay Prediction System

An **end-to-end, production-ready Machine Learning system** that predicts whether an e-commerce order will be **delivered on time or delayed** *before dispatch*.

This project integrates **Machine Learning, MLOps, APIs, dashboards, and deployable architecture** to help e-commerce businesses reduce SLA breaches, refunds, and customer dissatisfaction.

---

## 📌 Problem Statement

E-commerce platforms commonly face:

- SLA penalties and refunds  
- Loss of customer trust  
- Inefficient logistics planning  
- Increased operational costs  
- No early-warning mechanism for risky orders  

**This system enables proactive decision-making by predicting delivery delays in advance.**

---

## 🎯 Objectives

- Predict delivery delays at the order level  
- Identify key drivers of delivery delays  
- Provide real-time predictions via REST API  
- Offer a business-friendly UI  
- Implement a complete MLOps lifecycle  
- Enable cloud-ready deployment  

---

## 🧠 ML Problem Formulation

### Target Variable

| Variable | Description |
|--------|-------------|
| `delivery_delayed` | 0 → On-time, 1 → Delayed (SLA > 5 days) |

### Feature Engineering

- Order value (`price × quantity`)
- Order day of week and month (seasonality)
- Customer risk score (historical behavior)
- Product category
- Customer segment
- Order channel
- Device type

---

## 🗃️ Dataset

**File:** `ecommerce_orders_clean.csv`

Includes:
- Order and shipping dates  
- Customer, product, device, and channel attributes  
- Cleaned and structured for ML and BI dashboards  

---

## 🧪 Models Trained

| Model | Purpose |
|------|--------|
| Logistic Regression | Baseline |
| Decision Tree | Interpretability |
| **Random Forest** | Final selected model |
| XGBoost | Performance comparison |

**Evaluation Metric:** F1-Score

---

## 🏗️ System Architecture

```text
Raw Data
   ↓
Feature Engineering
   ↓
Model Training & Evaluation
   ↓
MLflow Experiment Tracking
   ↓
FastAPI Model Serving
   ↓
Streamlit UI
   ↓
Monitoring (Evidently AI)
   ↓
Retraining (Airflow / Prefect)
```

<h2>📂 Project Structure</h2>

<pre>
E-commerce-product-delivery-prediction/
│
├── api/
├── app/
├── model/
│   └── delivery_delay_model.pkl
├── notebooks/
├── reports/
│
├── Dockerfile
├── Dockerfile.streamlit
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
</pre>

<hr>

<h2>⚙️ Tech Stack</h2>

<h3>Data & ML</h3>
<p>Python, Pandas, NumPy, Scikit-learn, XGBoost</p>

<h3>MLOps</h3>
<p>MLflow, Airflow/Prefect, Evidently AI, GitHub Actions</p>

<h3>API & UI</h3>
<p>FastAPI, Pydantic, Streamlit</p>

<h3>Visualization</h3>
<p>Power BI / Tableau</p>

<h3>Deployment</h3>
<p>Docker, Streamlit Cloud, AWS</p>

<h2>🚀 Installation</h2>

<pre>
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
</pre>

<hr>

<h2>▶️ Running the Application</h2>

<h3>Start FastAPI</h3>
<pre>
uvicorn api.main:app --reload --port 8000
</pre>

<h3>Start Streamlit</h3>
<pre>
streamlit run app/streamlit_app.py
</pre>

<h2>pip install pytest httpx</h2>

## 🧪 Automated Testing

The project includes automated tests to validate:

- Model loading and prediction consistency
- Core feature transformations
- API health and prediction endpoints

Tests are implemented using `pytest` and can be executed locally:

pytest

<h2>🔌 API Example</h2>

<pre>
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

print(requests.post("http://localhost:8000/predict", json=payload).json())
</pre>

<h2>📊 Business Dashboards</h2>
<ul>
  <li>On-time vs delayed trends</li>
  <li>Seasonal delay patterns</li>
  <li>Customer segment risk</li>
  <li>Channel & device impact</li>
</ul>

<p><i>Add dashboard screenshots here</i></p>

<h2>💼 Business Impact</h2>
<ul>
  <li>Early detection of risky orders</li>
  <li>Better logistics planning</li>
  <li>Reduced refunds and penalties</li>
  <li>Improved customer satisfaction</li>
</ul>

<h2>✨ What Makes This Project Unique</h2>
<ul>
  <li>Business-focused ML system</li>
  <li>Customer behavior integrated into prediction</li>
  <li>Complete MLOps lifecycle</li>
  <li>API + UI + Dashboards</li>
  <li>Cloud-ready architecture</li>
</ul>

<h2>🧠 Interview One-Liner</h2>
<p>
“I built a production-grade ML system that predicts e-commerce delivery delays using behavioral, seasonal,
and operational signals, deployed via FastAPI with monitoring and business dashboards.”
</p>

<h2>🔮 Future Enhancements</h2>
<ul>
  <li>ETA prediction (regression)</li>
  <li>Warehouse and route optimization</li>
  <li>Kafka streaming pipeline</li>
  <li>Explainable AI (SHAP)</li>
</ul>

<h2>👤 Author</h2>
<p><b>Ashwani Pandey</b><br>
Data Science & Machine Learning Enthusiast</p>

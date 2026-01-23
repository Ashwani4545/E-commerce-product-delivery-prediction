<h1>🚚 E-Commerce Delivery Delay Prediction System</h1>

<p>
An end-to-end, production-ready Machine Learning system that predicts whether an e-commerce order will be 
<b>delivered on time or delayed</b> before shipping happens.
</p>

<p>
This project combines <b>Machine Learning, MLOps, APIs, dashboards, and deployable architecture</b> 
to help e-commerce businesses reduce SLA breaches, refunds, and customer dissatisfaction.
</p>

<hr>

<h2>📌 Problem Statement</h2>
<ul>
  <li>SLA penalties and refunds</li>
  <li>Loss of customer trust</li>
  <li>Inefficient logistics planning</li>
  <li>Increased operational costs</li>
  <li>No early warning mechanism for risky orders</li>
</ul>

<p><b>This system enables proactive decision-making by predicting delays in advance.</b></p>

<hr>

<h2>🎯 Objectives</h2>
<ul>
  <li>Predict delivery delay at the order level</li>
  <li>Identify key drivers of delay</li>
  <li>Provide real-time predictions via API</li>
  <li>Provide a business-friendly UI</li>
  <li>Implement a complete MLOps lifecycle</li>
  <li>Make the system cloud-deployable</li>
</ul>

<hr>

<h2>🧠 ML Problem Formulation</h2>

<h3>Target Variable</h3>
<table border="1" cellpadding="8">
<tr><th>Variable</th><th>Description</th></tr>
<tr><td>delivery_delayed</td><td>0 → On-time, 1 → Delayed (&gt; 5 days SLA)</td></tr>
</table>

<h3>Feature Engineering</h3>
<ul>
  <li>Order value (price × quantity)</li>
  <li>Day of week & month (seasonality)</li>
  <li>Customer risk score (historical behavior)</li>
  <li>Product category</li>
  <li>Customer segment</li>
  <li>Order channel</li>
  <li>Device type</li>
</ul>

<hr>

<h2>🗃️ Dataset</h2>
<p><b>File used:</b> ecommerce_orders_clean.csv</p>
<ul>
  <li>Order & shipping dates</li>
  <li>Customer, product, device, and channel information</li>
  <li>Suitable for ML and BI dashboards</li>
</ul>

<hr>

<h2>🧪 Models Trained</h2>
<table border="1" cellpadding="8">
<tr><th>Model</th><th>Purpose</th></tr>
<tr><td>Logistic Regression</td><td>Baseline</td></tr>
<tr><td>Decision Tree</td><td>Interpretability</td></tr>
<tr><td><b>Random Forest</b></td><td>Final selected model</td></tr>
<tr><td>XGBoost</td><td>Performance comparison</td></tr>
</table>

<p><b>Evaluation Metric:</b> F1-Score</p>

<hr>

<h2>🏗️ System Architecture</h2>

<pre>
Raw Data
   ↓
Feature Engineering
   ↓
Model Training & Evaluation
   ↓
MLflow Tracking
   ↓
FastAPI Deployment
   ↓
Streamlit UI
   ↓
Monitoring (Evidently)
   ↓
Retraining (Airflow/Prefect)
</pre>

<hr>

<h2>📂 Project Structure</h2>

<pre>
E-commerce-product-delivery-prediction/
│
├── api/
├── app/
├── model/
├── requirements.txt
└── Dockerfile
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

<hr>

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

<hr>

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

<hr>

<h2>📊 Business Dashboards</h2>
<ul>
  <li>On-time vs delayed trends</li>
  <li>Seasonal delay patterns</li>
  <li>Customer segment risk</li>
  <li>Channel & device impact</li>
</ul>

<p><i>Add dashboard screenshots here</i></p>

<hr>

<h2>💼 Business Impact</h2>
<ul>
  <li>Early detection of risky orders</li>
  <li>Better logistics planning</li>
  <li>Reduced refunds and penalties</li>
  <li>Improved customer satisfaction</li>
</ul>

<hr>

<h2>✨ What Makes This Project Unique</h2>
<ul>
  <li>Business-focused ML system</li>
  <li>Customer behavior integrated into prediction</li>
  <li>Complete MLOps lifecycle</li>
  <li>API + UI + Dashboards</li>
  <li>Cloud-ready architecture</li>
</ul>

<hr>

<h2>🧠 Interview One-Liner</h2>
<p>
“I built a production-grade ML system that predicts e-commerce delivery delays using behavioral, seasonal,
and operational signals, deployed via FastAPI with monitoring and business dashboards.”
</p>

<hr>

<h2>🔮 Future Enhancements</h2>
<ul>
  <li>ETA prediction (regression)</li>
  <li>Warehouse and route optimization</li>
  <li>Kafka streaming pipeline</li>
  <li>Explainable AI (SHAP)</li>
</ul>

<hr>

<h2>👤 Author</h2>
<p><b>Ashwani Pandey</b><br>
Data Science & Machine Learning Enthusiast</p>

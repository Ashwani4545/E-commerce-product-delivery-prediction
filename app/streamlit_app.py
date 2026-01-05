# STEP 2: Connect Streamlit UI to FastAPI
# Step 2.1: Streamlit App (app/streamlit_app.py)
import streamlit as st
import requests

st.title("📦 E-Commerce Delivery Delay Predictor")

api_url = "http://127.0.0.1:8000/predict"

price = st.number_input("Product Price", min_value=0.0)
quantity = st.number_input("Quantity", min_value=1)
category = st.selectbox("Category", ["Electronics", "Fashion", "Home"])
customer_segment = st.selectbox("Customer Segment", ["Regular", "Loyal", "New"])
channel = st.selectbox("Order Channel", ["Direct", "Campaign", "Referral"])
device_type = st.selectbox("Device", ["Mobile", "Desktop", "Tablet"])
order_dayofweek = st.selectbox("Day of Week (0=Mon)", list(range(7)))
order_month = st.selectbox("Month", list(range(1,13)))
customer_risk_score = st.slider("Customer Risk Score", 0.0, 1.0)

if st.button("Predict Delivery"):
    payload = {
        "price": price,
        "quantity": quantity,
        "category": category,
        "customer_segment": customer_segment,
        "channel": channel,
        "device_type": device_type,
        "order_dayofweek": order_dayofweek,
        "order_month": order_month,
        "customer_risk_score": customer_risk_score
    }

    try:
        response = requests.post(api_url, json=payload, timeout=10)
        
        if response.status_code != 200:
            st.error(f"❌ API Error: {response.status_code}")
            st.code(response.text)
        else:
            result = response.json()
            
            if result["delivery_delayed"] == 1:
                st.error(f"⚠️ Delivery likely delayed (Risk: {result['delay_probability']*100:.1f}%)")
            else:
                st.success(f"✅ Delivery likely on time (Risk: {result['delay_probability']*100:.1f}%)")
                
    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to API. Make sure FastAPI server is running at http://localhost:8000")
        st.info("Start the API with: uvicorn api.main:app --reload")
    except requests.exceptions.Timeout:
        st.error("❌ Request timeout. The API is taking too long to respond.")
    except requests.exceptions.JSONDecodeError:
        st.error("❌ Invalid response from API")
        st.code(response.text if response else "No response")
    except Exception as e:
        st.error(f"❌ Unexpected error: {str(e)}")
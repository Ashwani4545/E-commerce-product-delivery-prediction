from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_prediction_endpoint():
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

    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert "delay_probability" in response.json()


# Step 1.3: Define Input Schema
from pydantic import BaseModel

class PredictionInput(BaseModel):
    price: float
    quantity: int
    category: str
    customer_segment: str
    channel: str
    device_type: str
    order_dayofweek: int
    order_month: int
    customer_risk_score: float
    order_value: float = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "price": 29.99,
                "quantity": 2,
                "category": "Electronics",
                "customer_segment": "Regular",
                "channel": "Direct",
                "device_type": "Mobile",
                "order_dayofweek": 1,
                "order_month": 11,
                "customer_risk_score": 0.3,
                "order_value": 59.98
            }
        }

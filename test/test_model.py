import joblib
import os
from dotenv import load_dotenv

MODEL_PATH = "model/delivery_delay_model.pkl"
load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH")

if not MODEL_PATH:
    raise ValueError("MODEL_PATH is not set")
    
def test_model_loads():
    assert os.path.exists(MODEL_PATH)
    model = joblib.load(MODEL_PATH)
    assert model is not None

def test_model_prediction_shape():
    model = joblib.load(MODEL_PATH)

    sample_input = [[
        59.99,     # price
        1,         # quantity
        "Electronics",
        "Regular",
        "Direct",
        "Mobile",
        2,         # day of week
        10,        # month
        0.4        # customer risk
    ]]

    prediction = model.predict(sample_input)
    assert prediction[0] in [0, 1]


import os
import joblib
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Read model path from environment
MODEL_PATH = os.getenv("MODEL_PATH")

if not MODEL_PATH:
    raise ValueError(
        "MODEL_PATH not found in environment variables. "
        "Please set MODEL_PATH in .env file."
    )

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model file not found at path: {MODEL_PATH}"
        )

    print(f"✅ Loading model from: {MODEL_PATH}")
    return joblib.load(MODEL_PATH)


# Load model once at startup
model = load_model()

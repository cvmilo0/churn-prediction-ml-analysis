from fastapi import FastAPI
from .models.schemas import Customer
import joblib
from fastapi.middleware.cors import CORSMiddleware
from .limiter import limiter
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from slowapi.middleware import SlowAPIMiddleware
from fastapi import Request
import pandas as pd
from .utils import load_pipeline, load_feature_order
from mangum import Mangum
app = FastAPI(
    title="Churn Prediction API",
    description="API for telecom customer churn prediction",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rate limiter configuration
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

# Artifacts loading
pipeline = load_pipeline()
feature_order = load_feature_order()

@app.get("/status")
def status():
    return {"status": "Churn Prediction API is running"}

@app.post("/predict")
@limiter.limit("5/day")
def predict(request: Request, customer: Customer):
    payload = customer.model_dump()
    
    # Create DataFrame with features in the exact order expected by the pipeline
    df_data = {feature: payload[feature] for feature in feature_order}
    df = pd.DataFrame([df_data], columns=feature_order)
    
    # Make predictions using the simplified pipeline
    # The pipeline has 'scaler' and 'model' steps
    y_prob = pipeline.predict_proba(df)[0, 1]
    y_pred = pipeline.predict(df)[0]
    
    return {
        "label": int(y_pred),
        "churn_probability": float(y_prob),
    }

# Handler for AWS Lambda
handler = Mangum(
    app,
    lifespan="off",
    api_gateway_base_path="/"
)
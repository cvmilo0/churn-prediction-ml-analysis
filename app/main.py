from fastapi import FastAPI
from .models.schemas import Customer
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from .limiter import limiter
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from slowapi.middleware import SlowAPIMiddleware
from fastapi import Request

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
app.state.limiter =limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)


# Artifacts loading
model = joblib.load('./ml_models/rf.pkl')
feature_order = joblib.load('./ml_models/feature_order.pkl')


@app.get("/status")
def status():
    return {"status": "Churn Prediction API is running"}

@app.post("/predict")
@limiter.limit("5/day")
def predict(request: Request, customer: Customer):
    payload = customer.model_dump()
    row = [payload[feature] for feature in feature_order]
    X = np.array([row])
    y_prob = model.predict_proba(X)[0, 1]
    y_pred = model.predict(X)[0]
    return{
        "label": int(y_pred),
        "churn_probability": float(y_prob),
    }
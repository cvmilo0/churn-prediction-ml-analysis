# ML Customer Churn Prediction

## Project Objective
End-to-end machine learning solution for predicting customer churn. The project includes data wrangling, model training, and deployment of a production-ready API on AWS Lambda.

## Business Context
- Dataset comprising 5,000 customers with 20 different variables
- Variables include demographic data, usage patterns, and service metrics
- Target variable: "churn"

## Tech stack
- **Programming Language:** Python 3.11
- **ML Libraries:**
  - Pandas & NumPy: Data manipulation and analysis
  - Scikit-learn: Predictive modeling and evaluation
  - Imbalanced-learn: Class imbalance handling (SMOTE)
  - Joblib: Model serialization
- **API & Deployment:**
  - FastAPI: Web framework for building the API
  - uv: Fast Python package manager
  - Docker: Containerization
  - AWS Lambda: Serverless deployment

## Technical Skills

### 1. Data Preprocessing
- Outlier handling (winsorization)
- Categorical variable treatment
- Class balancing using SMOTE
- Feature engineering

### 2. Exploratory Analysis
- Correlation studies
- Data visualization

### 3. Predictive Modeling
- Random Forest Classifier implementation
- Hyperparameter optimization with Optuna
- Stratified cross-validation
- Robust model evaluation

### 4. Performance Metrics (Original Model)
- ROC-AUC: 0.888
- Precision in majority class: 94%
- Churn detection recall: 58%
- Global F1-Score: 88%

---

## API Deployment

### Live API Endpoint

The churn prediction model is deployed as a REST API on AWS Lambda:

**Base URL:** `https://tafuylh2rdjlgrat4e35vdjkpi0owtqo.lambda-url.eu-west-3.on.aws/`

### API Endpoints

#### 1. Health Check
```http
GET /status
```

**Response:**
```json
{
  "status": "Churn Prediction API is running"
}
```

#### 2. Churn Prediction
```http
POST /predict
Content-Type: application/json
```

**Request Body:**
```json
{
  "total_day_minutes": 265.1,
  "total_day_charge": 45.07,
  "number_customer_service_calls": 1,
  "avg_call_duration": 3.5,
  "number_vmail_messages": 25,
  "total_intl_calls": 3,
  "avg_cost_per_minute": 0.17,
  "total_eve_minutes": 197.4,
  "total_eve_charge": 16.78,
  "phone_number": 4155551234
}
```

**Response:**
```json
{
  "label": 0,
  "churn_probability": 0.22613065326633167
}
```

**Response Fields:**
- `label`: Binary prediction (0 = no churn, 1 = churn)
- `churn_probability`: Probability of churn (0.0 to 1.0)

### Rate Limiting
- **Limit:** 5 requests per day per IP

### API Architecture
- **Platform:** AWS Lambda (Serverless)
- **Runtime:** Python 3.11
- **Framework:** FastAPI with Mangum adapter
- **Container:** Docker-based deployment
- **Endpoint Type:** Lambda Function URL

---

## Local Development

### Setup

1. **Clone the repository**
```bash
git clone github.com/cvmilo0/churn-prediction-ml-analysis
cd churn_ml
```

2. **Install dependencies**
```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Or using pip
pip install -r requirements.txt
```

3. **Run locally with Docker**
```bash
docker-compose up
```

The API will be available at `http://localhost:8000`

### Project Structure
```
churn_ml/
├── app/
│   ├── main.py              # FastAPI application
│   ├── models/
│   │   └── schemas.py       # Pydantic models
│   ├── utils.py             # Model loading utilities
│   └── limiter.py           # Rate limiting configuration
├── notebooks/
│   ├── churn.ipynb          # Model training notebook
│   └── ml/
│       ├── pipeline_simple.pkl      # Trained model
│       └── feature_order_simple.pkl # Feature order
├── Dockerfile.prod          # Production Dockerfile (Lambda)
├── Dockerfile.dev           # Development Dockerfile
├── requirements.txt         # Development dependencies
├── requirements-prod.txt    # Production dependencies
└── README.md
```
---

## Author

Camilo Cortés Gómez

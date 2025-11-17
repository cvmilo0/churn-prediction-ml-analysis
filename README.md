# ML Customer Churn Prediction

## 🎯 Project Objective
Development of a predictive analytics solution to identify high-risk churn customers in a telecommunications company, leveraging Machine Learning

## 🔍 Business Context
- Dataset comprising 5,000 customers with 20 different variables
- Variables include demographic data, usage patterns, and service metrics
- Target variable: "churn" (customer abandonment)
- Class imbalance: 14.14% of customers have churned

## 💻 Technologies Used
- **Programming Language:** Python3.11
- **Main Libraries:**
  - Pandas & NumPy: Data manipulation and analysis
  - Scikit-learn: Predictive modeling and evaluation
  - SMOTE: Class imbalance handling
  - Seaborn & Matplotlib: Data visualization
  - Optuna: Hyperparameter optimization

## 🛠 Technical Skills Demonstrated

### 1. Data Preprocessing
- Outlier handling through winsorization techniques
- Categorical variable treatment
- Class balancing using SMOTE
- Advanced feature engineering

### 2. Exploratory Analysis
- Univariate distribution analysis
- Correlation studies
- Advanced data visualization
- Identification of key customer behavior patterns

### 3. Predictive Modeling
- Random Forest Classifier implementation
- Hyperparameter optimization with Optuna
- Stratified cross-validation
- Robust model evaluation

### 4. Performance Metrics
- ROC-AUC: 0.888
- Precision in majority class: 94%
- Churn detection recall: 58%
- Global F1-Score: 88%

## 📊 Key Findings

### Most Influential Variables
1. Total day minutes (13.9%)
2. Day charges (11.8%)
3. Average call duration (6.0%)
4. Average cost per minute (4.9%)
5. High customer service usage (4.2%)

### Business Insights
- Daytime usage patterns are the strongest predictors of churn
- Multiple customer service calls are a critical indicator
- Customers are sensitive to average cost per minute
- International usage, while minor, is a relevant indicator

## 🎯 Business Impact
- Proactive identification of at-risk customers with 88.8% accuracy
- 77.6% more effective than random selection
- Strategic prioritization of top 500 high-risk customers
- Actionable retention recommendations


## 🔄 Development Process
1. Detailed exploratory analysis
2. Extensive feature engineering
3. Random Forest modeling
4. Hyperparameter optimization
5. Model evaluation and tuning
6. Business insight generation
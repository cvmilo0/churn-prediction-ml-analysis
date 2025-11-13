import pandas as pd
import joblib

state_encoder = joblib.load('./notebooks/ml/state_encoder.pkl')

def bool_to_int_func(df):
    return df.astype(int)

def load_pipeline(pipeline_path='./notebooks/ml/pipeline_simple.pkl'):
    """Load pipeline with proper module registration for pickle"""    
    return joblib.load(pipeline_path)

def load_feature_order(path='./notebooks/ml/feature_order_simple.pkl'):
    """Load feature order"""
    return joblib.load(path)
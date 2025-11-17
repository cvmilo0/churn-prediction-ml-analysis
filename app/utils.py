import pandas as pd
import joblib
import os

def bool_to_int_func(df):
    return df.astype(int)

def _get_ml_path(filename):
    """Get the path to ML artifacts, handling both local and AWS Lambda environments"""
    if os.path.exists('/var/task'):
        base_path = '/var/task'
    else:
        base_path = '.'
    
    return os.path.join(base_path, 'notebooks', 'ml', filename)

def load_pipeline(pipeline_path=None):
    """Load pipeline with proper module registration for pickle"""
    if pipeline_path is None:
        pipeline_path = _get_ml_path('pipeline_simple.pkl')
    return joblib.load(pipeline_path)

def load_feature_order(path=None):
    """Load feature order"""
    if path is None:
        path = _get_ml_path('feature_order_simple.pkl')
    return joblib.load(path)
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

def load_data(path):
    """Load methylation data from Excel file"""
    df = pd.read_excel(path)
    x = df.drop(columns=['Sample ID', 'Diagnosed', 'Missing_Values'])
    y = df['Diagnosed']
    return x, y

def preprocess_data(x, y, test_size=0.25):
    """Preprocess data: handle imbalance, scale features, split"""
    # Handle class imbalance
    x_resampled, y_resampled = SMOTE().fit_resample(x, y)
    
    # Scale features
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x_resampled)
    
    # Split into train/test sets
    return train_test_split(x_scaled, y_resampled, test_size=test_size, stratify=y_resampled)
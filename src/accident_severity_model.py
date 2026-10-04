import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("../data/accident_data.csv")

# Display basic information
print("Dataset Shape:", data.shape)
print("\nDataset Columns:")
print(data.columns)

# Display first few records
print("\nFirst 5 Records:")
print(data.head())

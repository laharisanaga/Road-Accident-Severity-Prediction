import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("../data/indian_road_accident_severity_10000.csv")

# Display dataset information
print("Dataset Shape:", data.shape)
print("\nDataset Columns:")
print(data.columns)

# Encode categorical columns
encoder = LabelEncoder()

for column in data.select_dtypes(include="object").columns:
    data[column] = encoder.fit_transform(data[column])

# Separate features and target
X = data.drop("Accident_Severity", axis=1)
y = data["Accident_Severity"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=150,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

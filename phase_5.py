import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Load Dataset
data = pd.read_csv("dataset.csv")

# Features
X = data.drop("label", axis=1)

# Labels
y = data["label"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create Model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

# Train Model
print("Training Model...")

model.fit(X_train, y_train)

print("Training Completed!")

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy")
print("-" * 40)
print(f"{accuracy*100:.2f}%")

# Classification Report
print("\nClassification Report")
print("-" * 40)
print(classification_report(y_test, y_pred))

# Confusion Matrix
print("\nConfusion Matrix")
print("-" * 40)
print(confusion_matrix(y_test, y_pred))

# Save Model
joblib.dump(model, "sign_model.pkl")

print("\nModel Saved Successfully!")
print("File : sign_model.pkl")
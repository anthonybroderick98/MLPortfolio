import pandas as pd  # Data handling
import numpy as np  # Numerical operations
from sklearn.model_selection import train_test_split  # Data splitting
from sklearn.linear_model import LogisticRegression  # Classification model
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix  # Evaluation metrics


# -------------------------------------------------------
# CREATING SAMPLE DATA FOR CLASSIFICATION
# -------------------------------------------------------

# We generate a simple dataset with two numerical features and a binary target
print("\n📌 Creating Sample Data")

data = {
    "Feature1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Example numerical feature
    "Feature2": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],  # Another numerical feature
    "Target": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]  # Binary classification target
}

df = pd.DataFrame(data)  # Convert dictionary to DataFrame
print(df)


# -------------------------------------------------------
# SPLITTING DATA INTO TRAIN AND TEST SETS
# -------------------------------------------------------

# We split the dataset into training (70%) and testing (30%) sets
print("\n📌 Splitting Data")

X = df[["Feature1", "Feature2"]]  # Select features
y = df["Target"]  # Target variable

# Perform the split with a fixed random state for reproducibility
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Print dataset sizes
print(f"Training Samples: {len(X_train)}, Testing Samples: {len(X_test)}")


# -------------------------------------------------------
# TRAINING A LOGISTIC REGRESSION MODEL
# -------------------------------------------------------

# We train a Logistic Regression model on the training data
print("\n📌 Training Logistic Regression Model")

model = LogisticRegression()
model.fit(X_train, y_train)  # Train model


# -------------------------------------------------------
# MAKING PREDICTIONS
# -------------------------------------------------------

# Once trained, we use the model to make predictions on the test set
y_pred = model.predict(X_test)


# -------------------------------------------------------
# EVALUATING THE MODEL
# -------------------------------------------------------

# We assess model performance using accuracy, confusion matrix, and classification report
print("\n📌 Model Performance")

accuracy = accuracy_score(y_test, y_pred)  # Compute accuracy
conf_matrix = confusion_matrix(y_test, y_pred)  # Generate confusion matrix
classification_rep = classification_report(y_test, y_pred)  # Generate classification report

# Print results
print(f"Accuracy: {accuracy:.2f}")
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", classification_rep)


# -------------------------------------------------------
# GENERATING MODEL EVALUATION REPORT (HTML)
# -------------------------------------------------------

# We generate an HTML report to visualize model performance
html_report = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Scikit-Learn Model Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #2c3e50; }}
        h2 {{ color: #34495e; }}
        table {{ width: 50%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ padding: 10px; border: 1px solid #ddd; text-align: center; }}
        th {{ background-color: #3498db; color: white; }}
    </style>
</head>
<body>
    <h1>Scikit-Learn Model Evaluation Report</h1>
    <h2>Model: Logistic Regression</h2>
    <h3>Accuracy: {accuracy:.2f}</h3>
    
    <h2>Confusion Matrix</h2>
    <table>
        <tr><th></th><th>Predicted 0</th><th>Predicted 1</th></tr>
        <tr><th>Actual 0</th><td>{conf_matrix[0][0]}</td><td>{conf_matrix[0][1]}</td></tr>
        <tr><th>Actual 1</th><td>{conf_matrix[1][0]}</td><td>{conf_matrix[1][1]}</td></tr>
    </table>

    <h2>Classification Report</h2>
    <pre>{classification_rep}</pre>
</body>
</html>
"""


# -------------------------------------------------------
# SAVING REPORT TO HTML FILE
# -------------------------------------------------------

# We save the model evaluation report as an HTML file for easy viewing
html_file = "model_report.html"

with open(html_file, "w") as file:
    file.write(html_report)

print(f"\n✅ Model evaluation report saved successfully: {html_file}")

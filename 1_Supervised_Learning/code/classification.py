# Import required libraries for data processing, visualization, and model evaluation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    accuracy_score,
    confusion_matrix,
    roc_curve,
    auc,
    precision_recall_curve
)

# Load the dataset from the specified file path
file_path = "C:/Users/antho/Documents/AI and ML Internship Projects/1_Supervised_Learning/data/titanic.csv"
df = pd.read_csv(file_path)
print("\nDataset loaded successfully.")

# ---------------------------
# DATA PREPROCESSING
# ---------------------------

# Handle missing values to ensure dataset integrity
df["Age"].fillna(df["Age"].median(), inplace=True)  # Fill missing Age values with the median
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)  # Fill missing Embarked values with the most frequent value
df.drop(columns=["Cabin"], inplace=True)  # Drop Cabin column due to excessive missing values

# Feature Engineering: Create FamilySize to capture the effect of traveling with family
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1  

# Convert categorical variables into numerical values
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})  # Encode Sex (0 = Male, 1 = Female)
df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)  # Apply one-hot encoding to Embarked column

# Define input features (X) and target variable (y)
features = ["Pclass", "Sex", "Age", "Fare", "FamilySize", "Embarked_Q", "Embarked_S"]
X = df[features]  # Predictor variables
y = df["Survived"]  # Target variable (0 = Not Survived, 1 = Survived)

# ---------------------------
# TRAIN-TEST SPLIT
# ---------------------------

# Split dataset into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------------------------
# MODEL TRAINING & EVALUATION
# ---------------------------

# Define classification models to train
models = {
    "LogisticRegression": LogisticRegression(max_iter=200),
    "DecisionTreeClassifier": DecisionTreeClassifier(random_state=42),
    "RandomForestClassifier": RandomForestClassifier(random_state=42)
}

# Iterate through each model, train, and evaluate
for model_name, model in models.items():
    model.fit(X_train, y_train)  # Train the model
    y_pred = model.predict(X_test)  # Generate predictions on the test set

    # Compute model performance metrics
    acc = accuracy_score(y_test, y_pred)  # Calculate accuracy
    conf_matrix = confusion_matrix(y_test, y_pred)  # Generate confusion matrix

    # Display results
    print(f"\nModel: {model_name}")
    print(f"Accuracy: {acc:.2f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(conf_matrix)

    # ---------------------------
    # VISUALIZATION & METRICS
    # ---------------------------

    # Compute ROC Curve (if model supports probability predictions)
    y_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None
    if y_proba is not None:
        fpr, tpr, _ = roc_curve(y_test, y_proba)
        roc_auc = auc(fpr, tpr)

        plt.figure(figsize=(6, 6))
        plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
        plt.plot([0, 1], [0, 1], linestyle="--", color="gray")  # Reference diagonal
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title(f"{model_name} - ROC Curve")
        plt.legend(loc="lower right")
        plt.savefig(f"../results/plots/{model_name}_roc_curve.png")  # Save plot
        plt.close()

    # Compute Precision-Recall Curve (if model supports probability predictions)
    if y_proba is not None:
        precision, recall, _ = precision_recall_curve(y_test, y_proba)

        plt.figure(figsize=(6, 6))
        plt.plot(recall, precision, label="Precision-Recall Curve")
        plt.xlabel("Recall")
        plt.ylabel("Precision")
        plt.title(f"{model_name} - Precision-Recall Curve")
        plt.legend()
        plt.savefig(f"../results/plots/{model_name}_precision_recall_curve.png")  # Save plot
        plt.close()

    # Generate Confusion Matrix Heatmap
    plt.figure(figsize=(6, 6))
    sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues",
                xticklabels=["Not Survived", "Survived"],
                yticklabels=["Not Survived", "Survived"])
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.title(f"{model_name} - Confusion Matrix")
    plt.savefig(f"../results/plots/{model_name}_confusion_matrix.png")  # Save plot
    plt.close()

    # Generate Feature Importance Plot (only for tree-based models)
    if hasattr(model, "feature_importances_"):
        feature_importances = model.feature_importances_
        plt.figure(figsize=(8, 6))
        sns.barplot(x=feature_importances, y=features)
        plt.xlabel("Feature Importance")
        plt.ylabel("Feature Names")
        plt.title(f"{model_name} - Feature Importance")
        plt.savefig(f"../results/plots/{model_name}_feature_importance.png")  # Save plot
        plt.close()

print("\nAll models have been trained and evaluated. Results are saved in the results/plots directory.")

# ---------------------------
# SAVE PREDICTIONS
# ---------------------------

# Prepare a DataFrame to store predictions
predictions_data = []

for model_name, model in models.items():
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None

    for idx, (actual, predicted) in zip(X_test.index, zip(y_test, y_pred)):
        probability = y_proba[idx] if y_proba is not None else "N/A"
        predictions_data.append({
            "PassengerIndex": X_test.index[idx],
            "ActualSurvived": actual,
            "PredictedSurvived": predicted,
            "ProbabilitySurvived": probability,
            "Model": model_name
        })

# Convert to DataFrame and save to CSV
predictions_df = pd.DataFrame(predictions_data)
predictions_file_path = "../results/titanic_predictions.csv"
predictions_df.to_csv(predictions_file_path, index=False)

print(f"Predictions saved to {predictions_file_path}")

# ---------------------------
# CLEANING DATASET FOR FUTURE USE
# ---------------------------

from utils import preprocess_and_save

# Define file paths
raw_data_path = "../data/titanic.csv"
cleaned_data_path = "../data/Processed/titanic_cleaned.csv"

# Generate and save the cleaned dataset
preprocess_and_save(raw_data_path, cleaned_data_path)

print("\n✅ All outputs successfully generated!")
print(f"📂 Cleaned dataset saved at: {cleaned_data_path}")
print(f"📂 Model predictions saved at: {predictions_file_path}")
print("📊 Visualization plots are stored in the results/plots directory.")

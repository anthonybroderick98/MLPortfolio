# -------------------------------------------------------
# IMPORT REQUIRED LIBRARIES
# -------------------------------------------------------

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# -------------------------------------------------------
# DATA LOADING & PREPROCESSING FUNCTIONS
# -------------------------------------------------------

def load_data(file_path):
    """
    Loads the Titanic dataset from a CSV file and returns a Pandas DataFrame.
    """
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    """
    Cleans the dataset by handling missing values, encoding categorical variables, 
    and engineering additional features to enhance model performance.
    """
    # Handle missing values
    df["Age"].fillna(df["Age"].median(), inplace=True)  # Fill missing Age with median
    df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)  # Fill missing Embarked with mode
    df.drop(columns=["Cabin"], inplace=True, errors="ignore")  # Drop Cabin column due to excessive missing values

    # Feature Engineering: Create FamilySize
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1  # Combine SibSp and Parch

    # Convert categorical variables to numerical format
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})  # Encode Sex column (0 = Male, 1 = Female)
    df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)  # One-hot encode Embarked feature

    return df

# -------------------------------------------------------
# MODEL EVALUATION FUNCTION
# -------------------------------------------------------

def evaluate_model(model, X_test, y_test):
    """
    Evaluates a trained model using accuracy, classification report, and confusion matrix.
    """
    y_pred = model.predict(X_test)  # Generate predictions on test data

    print("\n📊 Model Performance:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

# -------------------------------------------------------
# DATA PREPROCESSING & SAVING FUNCTION
# -------------------------------------------------------

def preprocess_and_save(input_path, output_path):
    """
    Loads the raw Titanic dataset, performs data cleaning, 
    feature engineering, and saves the processed dataset.
    """
    # Load dataset
    df = pd.read_csv(input_path)

    # Handle missing values
    df["Age"].fillna(df["Age"].median(), inplace=True)  # Fill missing Age with median
    df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)  # Fill missing Embarked with mode
    df.drop(columns=["Cabin"], inplace=True, errors="ignore")  # Drop Cabin column

    # Feature Engineering: Create FamilySize
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1  # Capture family influence on survival
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})  # Convert Sex to numerical
    df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)  # Encode Embarked

    # Save cleaned dataset
    df.to_csv(output_path, index=False)
    print(f"\n✅ Cleaned dataset saved at: {output_path}")

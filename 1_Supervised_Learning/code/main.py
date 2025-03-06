# -------------------------------------------------------
# IMPORT REQUIRED LIBRARIES
# -------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# -------------------------------------------------------
# FILE PATH CONFIGURATION
# -------------------------------------------------------

# Define the dataset location (Ensure the correct path before execution)
FILE_PATH = "C:/Users/antho/Documents/AI and ML Internship Projects/1_Supervised_Learning/data/titanic.csv"

# -------------------------------------------------------
# FUNCTION DEFINITIONS
# -------------------------------------------------------

def load_data(file_path):
    """
    Loads the Titanic dataset from a CSV file and returns a Pandas DataFrame.
    Provides an initial overview of the dataset structure.
    """
    df = pd.read_csv(file_path)
    
    print("\n✅ Dataset Loaded Successfully")
    print(df.info())  # Display dataset structure
    print(df.head())  # Preview first few rows
    
    return df

def preprocess_data(df):
    """
    Handles missing values, encodes categorical variables, 
    and creates additional features to enhance model performance.
    """
    # Handle missing values
    df["Age"].fillna(df["Age"].median(), inplace=True)  # Fill missing Age values with median
    df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)  # Fill missing Embarked values with mode
    df.drop(columns=["Cabin"], inplace=True, errors='ignore')  # Drop Cabin due to excessive missing data

    # Feature Engineering: Create FamilySize (Combining SibSp & Parch)
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

    # Convert categorical variables to numerical
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})  # Encode gender (0 = Male, 1 = Female)
    df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)  # One-hot encode Embarked feature

    print("\n✅ Data Preprocessing Completed")
    print(df.head())  # Preview first few rows after preprocessing
    
    return df

def split_data(df):
    """
    Splits the dataset into training (80%) and testing (20%) sets.
    Defines the feature set and target variable.
    """
    features = ["Pclass", "Sex", "Age", "Fare", "FamilySize", "Embarked_Q", "Embarked_S"]
    X = df[features]  # Predictor variables
    y = df["Survived"]  # Target variable (0 = Not Survived, 1 = Survived)

    # Perform train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("\n✅ Data Split Completed")
    print(f"Training Data Size: {X_train.shape}")
    print(f"Testing Data Size: {X_test.shape}")

    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """
    Trains a Logistic Regression model and returns the trained model.
    """
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    print("\n✅ Model Training Completed")
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluates the trained model on the test set and prints 
    accuracy, classification report, and confusion matrix.
    """
    y_pred = model.predict(X_test)  # Generate predictions

    print("\n📊 Model Evaluation Results:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

# -------------------------------------------------------
# EXECUTION PIPELINE
# -------------------------------------------------------

if __name__ == "__main__":
    print("\n🚀 Starting Data Pipeline...\n")

    # Load dataset
    df = load_data(FILE_PATH)

    # Preprocess dataset
    df = preprocess_data(df)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = split_data(df)

    # Train model
    print("\n🔄 Training Logistic Regression Model...")
    model = train_model(X_train, y_train)

    # Evaluate model performance
    print("\n📊 Evaluating Model Performance...")
    evaluate_model(model, X_test, y_test)

    print("\n✅ Pipeline Completed Successfully!")

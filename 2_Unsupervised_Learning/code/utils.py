# ------------------------------------------------------------
# Utility Functions for Titanic Clustering Project
# ------------------------------------------------------------
# This script contains helper functions for:
# - Loading and preprocessing data
# - Scaling features for clustering
# - Determining the optimal number of clusters using Silhouette Scores
# - Reducing dimensions for visualization using PCA
# ------------------------------------------------------------

import pandas as pd
import numpy as np
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# ------------------------------------------------------------
# 📌 Step 1: Load Dataset
# ------------------------------------------------------------

def load_data(file_path):
    """
    Loads the Titanic dataset from a CSV file.

    Parameters:
    - file_path (str): Path to the dataset file.

    Returns:
    - pd.DataFrame: Loaded dataset or None if file not found.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Dataset loaded successfully from: {file_path}")
        return df
    except FileNotFoundError:
        print(f"❌ Error: File not found at {file_path}. Check the file path and try again.")
        return None

# ------------------------------------------------------------
# 📌 Step 2: Data Preprocessing
# ------------------------------------------------------------

def preprocess_data(df):
    """
    Preprocesses the Titanic dataset by handling missing values and encoding categorical variables.

    Parameters:
    - df (pd.DataFrame): Raw dataset.

    Returns:
    - pd.DataFrame: Cleaned dataset ready for clustering.
    """
    # Drop irrelevant columns
    df = df.drop(columns=["Name", "Ticket", "Cabin"], errors="ignore")

    # Handle missing values
    df["Age"] = df["Age"].fillna(df["Age"].median())  # Fill missing Age with median
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())  # Fill missing Fare with median
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])  # Fill missing Embarked with most common value

    # Encode categorical variables
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})  # Convert gender to numerical
    df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)  # One-hot encode Embarked column

    print("✅ Data preprocessing completed.")
    return df

# ------------------------------------------------------------
# 📌 Step 3: Feature Scaling
# ------------------------------------------------------------

def scale_features(df, feature_columns):
    """
    Standardizes numerical features using StandardScaler to ensure
    clustering is not affected by feature scale differences.

    Parameters:
    - df (pd.DataFrame): Dataset with selected features.
    - feature_columns (list): List of column names to scale.

    Returns:
    - np.array: Scaled feature matrix.
    """
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df[feature_columns])
    print("✅ Feature scaling completed.")
    return scaled_features

# ------------------------------------------------------------
# 📌 Step 4: Finding the Optimal Number of Clusters (K)
# ------------------------------------------------------------

def find_optimal_k(data, k_range):
    """
    Determines the optimal number of clusters (K) using silhouette scores.

    Parameters:
    - data (np.array): Scaled dataset for clustering.
    - k_range (range): Range of K values to test.

    Returns:
    - int: Optimal number of clusters.
    """
    best_k = None
    best_score = -1

    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(data)
        score = silhouette_score(data, labels)

        print(f"🔍 Tested K={k}, Silhouette Score={score:.2f}")

        if score > best_score:
            best_score = score
            best_k = k

    print(f"\n✅ Optimal K found: {best_k} with Silhouette Score: {best_score:.2f}")
    return best_k

# ------------------------------------------------------------
# 📌 Step 5: Dimensionality Reduction (PCA)
# ------------------------------------------------------------

def reduce_dimensions(data, n_components=2):
    """
    Reduces dataset dimensions using PCA to aid in visualization.

    Parameters:
    - data (np.array): Scaled dataset.
    - n_components (int): Number of PCA components.

    Returns:
    - np.array: Reduced dataset.
    """
    pca = PCA(n_components=n_components)
    reduced_data = pca.fit_transform(data)
    print(f"✅ Dimensionality reduction completed. Data reduced to {n_components} components.")
    return reduced_data

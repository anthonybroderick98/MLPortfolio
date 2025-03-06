# -------------------------------------------------------
# REUSABLE PYTHON FUNCTIONS FOR AI/ML
# -------------------------------------------------------

# This script contains reusable functions for handling missing data,
# encoding categorical variables, standardizing numerical features,
# computing statistics, and saving/loading datasets. These functions
# help automate data preprocessing for AI/ML models.

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


# -------------------------------------------------------
# HANDLE MISSING DATA
# -------------------------------------------------------

# This function fills missing values in a specified column using the
# chosen strategy (median, mean, or mode). Handling missing data is
# crucial for ensuring dataset integrity in AI/ML models.

def fill_missing_values(df, column_name, strategy="median"):
    """
    Fills missing values in a DataFrame column using the specified strategy.
    
    Parameters:
    - df (DataFrame): The input DataFrame.
    - column_name (str): Column where missing values need to be handled.
    - strategy (str): Method to fill missing values ('median', 'mean', 'mode').

    Returns:
    - DataFrame with missing values filled.
    """
    if strategy == "median":
        df[column_name] = df[column_name].fillna(df[column_name].median())
    elif strategy == "mean":
        df[column_name] = df[column_name].fillna(df[column_name].mean())
    elif strategy == "mode":
        df[column_name] = df[column_name].fillna(df[column_name].mode()[0])
    return df


# -------------------------------------------------------
# ENCODE CATEGORICAL VARIABLES
# -------------------------------------------------------

# This function converts categorical data into numerical codes,
# making it suitable for machine learning models that require
# numerical input.

def encode_categorical(df, column_name):
    """Encodes categorical values into numerical format."""
    df[column_name] = df[column_name].astype("category").cat.codes
    return df


# -------------------------------------------------------
# STANDARDIZE NUMERICAL FEATURES
# -------------------------------------------------------

# This function standardizes numerical columns using StandardScaler,
# ensuring that all features have a mean of 0 and a standard deviation
# of 1, improving model performance.

def scale_features(df, column_names):
    """Standardizes numerical features using StandardScaler."""
    scaler = StandardScaler()
    df[column_names] = scaler.fit_transform(df[column_names])
    return df


# -------------------------------------------------------
# COMPUTE BASIC STATISTICS
# -------------------------------------------------------

# This function computes basic statistics (mean, median, standard
# deviation, min, and max) for a given numerical column.

def compute_statistics(df, column_name):
    """Returns basic statistics for a given column."""
    stats = {
        "Mean": np.mean(df[column_name]),
        "Median": np.median(df[column_name]),
        "Std Dev": np.std(df[column_name]),
        "Min": np.min(df[column_name]),
        "Max": np.max(df[column_name])
    }
    return stats


# -------------------------------------------------------
# SAVE & LOAD CSV FILES
# -------------------------------------------------------

# These functions allow saving and loading DataFrames to and from
# CSV files, which is useful for storing processed datasets.

def save_dataframe(df, filename):
    """Saves a DataFrame to a CSV file."""
    df.to_csv(filename, index=False)
    print(f"✅ Data saved to {filename}")

def load_dataframe(filename):
    """Loads a CSV file into a DataFrame."""
    return pd.read_csv(filename)


# -------------------------------------------------------
# TESTING THE FUNCTIONS
# -------------------------------------------------------

if __name__ == "__main__":
    # Sample dataset for testing
    sample_data = {
        "Age": [25, np.nan, 30, 35, np.nan],
        "Gender": ["Male", "Female", "Female", "Male", "Male"],
        "Income": [50000, 55000, np.nan, 60000, 58000]
    }
    
    df = pd.DataFrame(sample_data)
    print("\n📌 Original Data:\n", df)

    # Fill Missing Values
    df = fill_missing_values(df, "Age", "median")
    df = fill_missing_values(df, "Income", "mean")

    # Encode Categorical Variables
    df = encode_categorical(df, "Gender")

    # Scale Features
    df = scale_features(df, ["Income"])

    print("\n📌 Processed Data:\n", df)

    # Compute Statistics
    stats = compute_statistics(df, "Age")
    print("\n📌 Age Statistics:\n", stats)

    # Save Data
    save_dataframe(df, "processed_data.csv")

    # Load Data
    loaded_df = load_dataframe("processed_data.csv")
    print("\n📌 Loaded Data:\n", loaded_df)

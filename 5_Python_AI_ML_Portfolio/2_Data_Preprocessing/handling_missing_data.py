# -------------------------------------------------------
# HANDLING MISSING DATA IN AI/ML
# -------------------------------------------------------

# This script detects and handles missing values in datasets. Missing values
# can negatively impact machine learning models, so they must be addressed
# before training.

# Import necessary libraries for data handling and numerical operations.
import pandas as pd  # Library for working with datasets
import numpy as np  # Library for numerical computations

# -------------------------------------------------------
# DETECTING MISSING VALUES
# -------------------------------------------------------

# This function scans the dataset for missing values and prints a summary.

def detect_missing_values(df):
    """
    Detects and prints missing values in each column of a DataFrame.

    Parameters:
    - df (DataFrame): The input dataset.

    Returns:
    - Series: A count of missing values per column.
    """
    missing_values = df.isnull().sum()  # Count missing values in each column
    print("\n📌 Missing Values in Dataset:\n", missing_values)
    return missing_values

# -------------------------------------------------------
# FILLING MISSING VALUES
# -------------------------------------------------------

# This function fills missing values using a specified strategy.

def fill_missing_values(df, column_name, strategy="median"):
    """
    Fills missing values in a specified column using median, mean, or mode.

    Parameters:
    - df (DataFrame): The input dataset.
    - column_name (str): The column where missing values need to be handled.
    - strategy (str): The method used to fill missing values ('median', 'mean', 'mode').

    Returns:
    - DataFrame with missing values filled.
    """
    if strategy == "median":
        df[column_name] = df[column_name].fillna(df[column_name].median())  # Uses median
    elif strategy == "mean":
        df[column_name] = df[column_name].fillna(df[column_name].mean())  # Uses mean
    elif strategy == "mode":
        df[column_name] = df[column_name].fillna(df[column_name].mode()[0])  # Uses mode
    print(f"✅ Missing values in '{column_name}' filled using {strategy}.")
    return df

# -------------------------------------------------------
# CREATING SAMPLE DATA
# -------------------------------------------------------

# This section creates a sample dataset with missing values for testing.

if __name__ == "__main__":
    # Define a dictionary representing raw data with some missing values.
    sample_data = {
        "Age": [25, np.nan, 30, 35, np.nan],  # Some missing age values
        "Gender": ["Male", "Female", "Female", "Male", "Male"],  # Categorical column
        "Income": [50000, 55000, np.nan, 60000, 58000]  # Some missing income values
    }
    
    # Convert the dictionary to a Pandas DataFrame.
    df = pd.DataFrame(sample_data)
    
    # Display the original dataset before processing.
    print("\n📌 Original Data:\n", df)

    # Detect missing values.
    detect_missing_values(df)

    # Fill missing values in 'Age' using the median.
    df = fill_missing_values(df, "Age", "median")

    # Fill missing values in 'Income' using the mean.
    df = fill_missing_values(df, "Income", "mean")

    # Display the processed dataset after handling missing values.
    print("\n📌 Processed Data:\n", df)

# -------------------------------------------------------
# SAVING CLEANED DATA TO CSV
# -------------------------------------------------------

# Define the output file name.
output_file = "cleaned_data.csv"

# Save the processed DataFrame to a CSV file.
df.to_csv(output_file, index=False)

# Confirm that the file has been saved successfully.
print(f"\n✅ Cleaned dataset saved to {output_file}")




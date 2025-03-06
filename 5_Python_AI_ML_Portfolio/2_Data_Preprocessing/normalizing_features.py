# -------------------------------------------------------
# NORMALIZING AND STANDARDIZING FEATURES FOR MACHINE LEARNING
# -------------------------------------------------------

# This script applies two different feature scaling techniques: Standardization and Normalization.
# Scaling ensures that numerical values are properly adjusted, improving the performance of
# machine learning models.

# Import required libraries for data manipulation and feature scaling.
import pandas as pd  # Library for working with datasets
from sklearn.preprocessing import StandardScaler, MinMaxScaler  # Scalers for feature transformation

# -------------------------------------------------------
# STANDARDIZATION (MEAN = 0, STANDARD DEVIATION = 1)
# -------------------------------------------------------

# This function standardizes numerical features so that they have a mean of 0 and a
# standard deviation of 1. Standardization helps models that assume normally distributed data.

def standardize_features(df, column_names):
    """
    Standardizes numerical features using StandardScaler.

    Parameters:
    - df (DataFrame): The input DataFrame.
    - column_names (list): List of numerical columns to standardize.

    Returns:
    - DataFrame with standardized features.
    """
    scaler = StandardScaler()  # Initialize StandardScaler
    df[column_names] = scaler.fit_transform(df[column_names])  # Apply transformation
    print(f"✅ Features {column_names} standardized using StandardScaler.")
    return df

# -------------------------------------------------------
# NORMALIZATION (SCALE VALUES BETWEEN 0 AND 1)
# -------------------------------------------------------

# This function normalizes numerical features to a range between 0 and 1. Normalization is 
# useful when features have different units or scales, ensuring uniformity across all values.

def normalize_features(df, column_names):
    """
    Normalizes numerical features to a range of 0 to 1 using MinMaxScaler.

    Parameters:
    - df (DataFrame): The input DataFrame.
    - column_names (list): List of numerical columns to normalize.

    Returns:
    - DataFrame with normalized features.
    """
    scaler = MinMaxScaler()  # Initialize MinMaxScaler
    df[column_names] = scaler.fit_transform(df[column_names])  # Apply transformation
    print(f"✅ Features {column_names} normalized using MinMaxScaler.")
    return df

# -------------------------------------------------------
# CREATING SAMPLE DATA & APPLYING SCALING TECHNIQUES
# -------------------------------------------------------

# This section creates a sample dataset with numerical features for testing
# standardization and normalization techniques.

if __name__ == "__main__":
    # Define a dictionary representing a dataset with different numerical features.
    sample_data = {
        "Height": [150, 160, 170, 180, 190],  # Heights in cm
        "Weight": [50, 60, 70, 80, 90],  # Weights in kg
        "Income": [30000, 40000, 50000, 60000, 70000]  # Yearly income in dollars
    }
    
    # Convert the dictionary into a Pandas DataFrame.
    df = pd.DataFrame(sample_data)
    
    # Display the original dataset before processing.
    print("\n📌 Original Data:\n", df)

    # Apply Standardization
    df = standardize_features(df, ["Height", "Weight", "Income"])

    # Apply Normalization
    df = normalize_features(df, ["Height", "Weight", "Income"])

    # Display the processed dataset after scaling.
    print("\n📌 Processed Data:\n", df)

# -------------------------------------------------------
# SAVING PROCESSED DATA TO CSV
# -------------------------------------------------------

# Define the output file name.
output_file = "scaled_data.csv"

# Save the processed DataFrame to a CSV file.
df.to_csv(output_file, index=False)

# Confirm that the file has been saved successfully.
print(f"\n✅ Processed data saved to '{output_file}'.")


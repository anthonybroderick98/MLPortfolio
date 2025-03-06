# -------------------------------------------------------
# 📌 DATA PREPROCESSING MODULE
# -------------------------------------------------------
# This script handles missing values and scales numerical features 
# to prepare the dataset for clustering.

import pandas as pd
import numpy as np
import logging
from sklearn.preprocessing import StandardScaler

# ✅ Logging setup for debugging & tracking execution
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# -------------------------------------------------------
# 📌 FUNCTION: LOAD & CLEAN DATA
# -------------------------------------------------------
def load_and_clean_data(file_path):
    """
    Loads the customer dataset, handles missing values, 
    and returns a cleaned DataFrame.
    """
    logging.info("\n📌 Loading customer dataset...")
    
    # Load dataset
    df = pd.read_csv(file_path)

    # Check for missing values
    missing_values = df.isnull().sum()
    logging.info(f"🔍 Missing values per column:\n{missing_values}")

    # Handle missing data: If >40% missing, drop column. Otherwise, impute with median.
    for column in df.columns:
        if df[column].isnull().mean() > 0.4:
            df.drop(columns=[column], inplace=True)
            logging.warning(f"⚠ Column '{column}' dropped due to excessive missing values.")
        else:
            df[column].fillna(df[column].median(), inplace=True)
            logging.info(f"✅ Missing values in '{column}' filled using median imputation.")

    logging.info("✅ Data cleaning complete.")
    return df

# -------------------------------------------------------
# 📌 FUNCTION: FEATURE SCALING
# -------------------------------------------------------
def scale_features(df, save_path="processed_customer_data.csv"):
    """
    Applies feature scaling (StandardScaler) to ensure fair clustering
    and saves the processed dataset.
    """
    logging.info("\n📌 Scaling numerical features...")

    scaler = StandardScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

    # Save cleaned & scaled dataset
    df_scaled.to_csv(save_path, index=False)
    logging.info(f"✅ Processed dataset saved as '{save_path}'.")

    return df_scaled

# -------------------------------------------------------
# 📌 MAIN EXECUTION
# -------------------------------------------------------
if __name__ == "__main__":
    # Load and clean the data
    df_cleaned = load_and_clean_data("raw_customer_data.csv")

    # Scale numerical features
    df_scaled = scale_features(df_cleaned)

    logging.info("\n🎯 Data Preprocessing Completed!")

# -------------------------------------------------------
# IMPORT REQUIRED LIBRARIES
# -------------------------------------------------------

import pandas as pd
import os

# -------------------------------------------------------
# FILE PATH CONFIGURATION
# -------------------------------------------------------

# Define the dataset location (Ensure the correct path before execution)
BASE_DIR = r"C:\Users\antho\Documents\AI and ML Internship Projects\3_Model_Evaluation"
DATA_DIR = os.path.join(BASE_DIR, "data")
PREDICTIONS_FILE = os.path.join(DATA_DIR, "predictions_data.csv")

# -------------------------------------------------------
# FUNCTION TO FIX PREDICTIONS FILE
# -------------------------------------------------------

def clean_predictions(file_path):
    """
    Cleans and formats the Titanic predictions dataset to ensure compatibility 
    with model evaluation scripts.

    Steps:
    - Loads dataset and removes any incorrect headers or empty rows
    - Ensures column names are correctly assigned
    - Converts data to numeric format
    - Drops any NaN (empty) rows
    - Saves the cleaned dataset back to CSV
    """
    
    print(f"\n🔄 Cleaning predictions file: {file_path}")

    try:
        # Load the predictions file
        df = pd.read_csv(file_path)

        # Ensure correct column names
        expected_columns = ["Actual", "Predicted", "Probability"]
        df = df[df.columns[:3]]  # Keep only the first 3 columns
        df.columns = expected_columns  # Rename columns correctly

        # Convert data to numeric (handles any formatting issues)
        df = df.apply(pd.to_numeric, errors="coerce")

        # Drop any empty rows
        df = df.dropna()

        # Save the cleaned CSV file
        df.to_csv(file_path, index=False)

        print(f"✅ Fully cleaned predictions file saved at {file_path}")

    except FileNotFoundError:
        print(f"❌ Error: Predictions file not found at {file_path}. Please check the file path.")
    except pd.errors.EmptyDataError:
        print(f"❌ Error: The file at {file_path} is empty. Check data integrity.")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

# -------------------------------------------------------
# EXECUTION
# -------------------------------------------------------

if __name__ == "__main__":
    clean_predictions(PREDICTIONS_FILE)

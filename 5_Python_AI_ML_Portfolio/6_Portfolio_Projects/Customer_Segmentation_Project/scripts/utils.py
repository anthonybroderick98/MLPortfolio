# -------------------------------------------------------
# 📌 UTILITY FUNCTIONS MODULE
# -------------------------------------------------------
# This script contains helper functions for logging, file handling,
# and general reusable components to improve modularity.

import logging
import os
import pandas as pd
import time

# ✅ Logging setup for debugging & execution tracking
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# -------------------------------------------------------
# 📌 FUNCTION: CREATE OUTPUT DIRECTORIES
# -------------------------------------------------------
def ensure_directories_exist(directories):
    """
    Ensures that the specified output directories exist.
    If they don't exist, they are created.
    
    Args:
        directories (list): List of directory paths to check/create.
    """
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        logging.info(f"✅ Directory verified/created: {directory}")

# -------------------------------------------------------
# 📌 FUNCTION: SAVE DATA TO CSV
# -------------------------------------------------------
def save_dataframe(df, file_path):
    """
    Saves a DataFrame to a CSV file.
    
    Args:
        df (pd.DataFrame): The DataFrame to save.
        file_path (str): The path where the CSV will be saved.
    """
    try:
        df.to_csv(file_path, index=False)
        logging.info(f"✅ Data saved successfully: {file_path}")
    except Exception as e:
        logging.error(f"❌ ERROR: Failed to save data to {file_path}. {e}")

# -------------------------------------------------------
# 📌 FUNCTION: LOAD DATA FROM CSV
# -------------------------------------------------------
def load_dataframe(file_path):
    """
    Loads a CSV file into a Pandas DataFrame.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        logging.info(f"✅ Data loaded successfully: {file_path}")
        return df
    except Exception as e:
        logging.error(f"❌ ERROR: Failed to load data from {file_path}. {e}")
        return None

# -------------------------------------------------------
# 📌 FUNCTION: TRACK EXECUTION TIME
# -------------------------------------------------------
def time_it(func):
    """
    Decorator function to measure execution time of a function.
    
    Args:
        func (function): The function to be timed.
    
    Returns:
        function: Wrapped function with execution time logging.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"✅ {func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# -------------------------------------------------------
# 📌 FUNCTION: VALIDATE DATASET
# -------------------------------------------------------
def check_data_integrity(df):
    """
    Checks for missing values and invalid data types in a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to check.
    
    Returns:
        bool: True if data is valid, False otherwise.
    """
    if df.isnull().sum().sum() > 0:
        logging.warning("⚠ WARNING: Dataset contains missing values.")
        return False
    
    if not all(df.dtypes != 'object'):
        logging.warning("⚠ WARNING: Dataset contains non-numeric columns.")
        return False

    logging.info("✅ Data integrity check passed.")
    return True

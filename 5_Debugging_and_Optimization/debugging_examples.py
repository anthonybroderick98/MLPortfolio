# -------------------------------------------------------
# 📌 DEBUGGING & OPTIMIZING AI/ML PIPELINES
# -------------------------------------------------------

import pandas as pd  # Data handling
import numpy as np  # Numerical operations
import matplotlib.pyplot as plt  # Visualization
import seaborn as sns  # Statistical visualizations
from sklearn.model_selection import train_test_split  # Data splitting
from sklearn.linear_model import LogisticRegression  # Model training
from sklearn.metrics import accuracy_score  # Model evaluation
import time  # Execution time profiling
import warnings  # Suppress warnings
import os  # File handling
from datetime import datetime  # Timestamped logs

warnings.filterwarnings("ignore")  # Suppress warnings for cleaner debugging

# -------------------------------------------------------
# ✅ SETUP: OUTPUT DIRECTORIES & LOGGING
# -------------------------------------------------------

os.makedirs("outputs", exist_ok=True)  
os.makedirs("logs", exist_ok=True)  

# ✅ Create Debug Log File with Timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"outputs/debugging_log_{timestamp}.txt"

with open(log_filename, "w", encoding="utf-8") as debug_log:

    def log_message(message):
        """Logs messages to console and file."""
        print(message)
        debug_log.write(message + "\n")

    # ✅ Start Profiling Execution Time
    start_time = time.time()

    # -------------------------------------------------------
    # 📌 1. HANDLING MISSING VALUES
    # -------------------------------------------------------

    log_message("\n📌 Debugging: Handling Missing Values")

    data = {"Age": [25, np.nan, 30, 35, np.nan], "Salary": [50000, 55000, np.nan, 60000, 58000]}
    df = pd.DataFrame(data)

    log_message("\nBefore Fixing:\n" + str(df))

    # Compute missing percentages
    missing_percentage = df.isnull().mean() * 100
    log_message("\nMissing Data (%):\n" + str(missing_percentage))

    # Drop columns with over 40% missing
    df = df.dropna(axis=1, thresh=0.6 * len(df))

    # Fill remaining missing values with median
    df.fillna(df.median(), inplace=True)

    # ✅ Save fixed dataset
    df.to_csv("outputs/debugged_missing_values.csv", index=False)
    log_message("\nAfter Fixing:\n" + str(df))

    # -------------------------------------------------------
    # 📌 2. DEBUGGING DATA TYPE ISSUES
    # -------------------------------------------------------

    log_message("\n📌 Debugging: Data Type Issues")

    df["Salary"] = df["Salary"].astype(str)  # Incorrectly converted to string
    log_message(f"\n❌ WARNING: Incorrect Salary Data Type {df['Salary'].dtype}")

    try:
        df["Salary"] = df["Salary"] + "1000"  # This will cause an error
    except Exception as e:
        log_message(f"❌ ERROR: {e}")

    # Fix: Convert salary back to numeric safely
    df["Salary"] = df["Salary"].apply(pd.to_numeric, errors="coerce") + 1000

    log_message(f"\n✅ Fixed Salary Column Data Type: {df['Salary'].dtype}")
    log_message("\nFixed Salary Column:\n" + str(df))

    # ✅ Save fixed dataset
    df.to_csv("outputs/debugged_data_types.csv", index=False)

    # -------------------------------------------------------
    # 📌 3. DEBUGGING MODEL TRAINING ISSUES
    # -------------------------------------------------------

    log_message("\n📌 Debugging: Model Training Issues")

    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y = np.array([0, 0, 1, 1])

    log_message(f"\nDataset Shape: X={X.shape}, y={y.shape}")

    try:
        model = LogisticRegression(random_state=42)
        model.fit(X, y)
        predictions = model.predict(X)
        accuracy = accuracy_score(y, predictions)
        log_message(f"\n✅ Model trained successfully. Accuracy: {accuracy:.4f}")
    except Exception as e:
        log_message(f"❌ ERROR: {e}")

    # -------------------------------------------------------
    # 📌 4. DEBUGGING DATA SPLITTING ISSUES
    # -------------------------------------------------------

    log_message("\n📌 Debugging: Data Splitting Issues")

    df_large = pd.DataFrame(np.random.rand(3, 2), columns=["Feature1", "Feature2"])
    df_large["Target"] = [1, 0, 1]  # Only 3 samples

    log_message(f"\nInitial Data:\n{df_large}")

    try:
        test_size = 0.3 if len(df_large) < 5 else 0.5
        X_train, X_test, y_train, y_test = train_test_split(df_large[["Feature1", "Feature2"]], df_large["Target"], test_size=test_size, random_state=42)
        log_message(f"\n✅ Data split successfully. Train: {len(X_train)}, Test: {len(X_test)}")
    except Exception as e:
        log_message(f"❌ ERROR: {e}")

    # -------------------------------------------------------
    # 📌 5. PROFILING EXECUTION TIME
    # -------------------------------------------------------

    execution_time = time.time() - start_time
    log_message(f"\n⏳ Total Execution Time: {execution_time:.2f} seconds")
    log_message("\n🎯 Debugging & Optimization Complete!")
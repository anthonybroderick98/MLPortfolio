# -------------------------------------------------------
# 📌 WRITING REUSABLE & OPTIMIZED AI/ML CODE
# -------------------------------------------------------
# This script demonstrates best practices in modularity, logging, 
# and file handling for AI/ML pipelines.
# -------------------------------------------------------

import pandas as pd  # Data handling
import numpy as np  # Numerical operations

import os # File handling
os.environ["LOKY_MAX_CPU_COUNT"] = "4"  # Set this to the number of logical cores you want to use

import logging  # Logging for debugging
import matplotlib.pyplot as plt  # Visualization
from sklearn.preprocessing import StandardScaler  # Feature scaling
from sklearn.cluster import KMeans  # K-Means clustering

# -------------------------------------------------------
# ✅ SETUP: OUTPUT DIRECTORIES & LOGGING
# -------------------------------------------------------

# ✅ Ensure necessary output directories exist
output_dirs = ["outputs"]
for directory in output_dirs:
    os.makedirs(directory, exist_ok=True)

# ✅ Setup Logging (Better Alternative to Print Statements)
logging.basicConfig(
    filename="outputs/logging_report.txt",  # Save logs
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w"
)

# -------------------------------------------------------
# ✅ 1. FUNCTION FOR HANDLING MISSING VALUES
# -------------------------------------------------------

def fill_missing_values(df, column_name, strategy="median"):
    """Fills missing values using median, mean, or mode."""
    try:
        if strategy == "median":
            df.loc[:, column_name] = df[column_name].fillna(df[column_name].median())  # FIXED
        elif strategy == "mean":
            df.loc[:, column_name] = df[column_name].fillna(df[column_name].mean())
        elif strategy == "mode":
            df.loc[:, column_name] = df[column_name].fillna(df[column_name].mode()[0])
        logging.info(f"✅ Missing values in '{column_name}' filled using {strategy}.")
    except Exception as e:
        logging.error(f"❌ ERROR: Failed to fill missing values in '{column_name}'. {e}")
    return df

# -------------------------------------------------------
# ✅ 2. FUNCTION FOR FEATURE SCALING
# -------------------------------------------------------

def scale_features(df, column_names):
    """Standardizes numerical features using StandardScaler."""
    try:
        scaler = StandardScaler()
        df[column_names] = scaler.fit_transform(df[column_names])
        logging.info(f"✅ Scaled features: {column_names}")
    except Exception as e:
        logging.error(f"❌ ERROR: Feature scaling failed. {e}")
    return df

# -------------------------------------------------------
# ✅ 3. FUNCTION FOR RUNNING K-MEANS CLUSTERING
# -------------------------------------------------------

def run_kmeans(df, features, k=3):
    """Applies K-Means clustering on selected features."""
    try:
        df_selected = df[features]
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        df["Cluster"] = kmeans.fit_predict(df_selected)
        logging.info(f"✅ K-Means applied with {k} clusters.")
    except Exception as e:
        logging.error(f"❌ ERROR: K-Means clustering failed. {e}")
    return df

# -------------------------------------------------------
# ✅ 4. FUNCTION FOR VISUALIZING CLUSTERS
# -------------------------------------------------------

def plot_clusters(df, features):
    """Generates a scatter plot for clustered data."""
    try:
        plt.figure(figsize=(8, 5))
        scatter = plt.scatter(df[features[0]], df[features[1]], c=df["Cluster"], cmap="viridis", edgecolors="k")
        plt.colorbar(scatter, label="Cluster")
        plt.xlabel(features[0])
        plt.ylabel(features[1])
        plt.title("Customer Segments (K-Means Clustering)")
        plt.savefig("outputs/kmeans_clusters.png")  # Save visualization
        plt.show()
        logging.info("✅ Cluster visualization saved as 'outputs/kmeans_clusters.png'.")
    except Exception as e:
        logging.error(f"❌ ERROR: Cluster visualization failed. {e}")

# -------------------------------------------------------
# ✅ 5. RUNNING ALL FUNCTIONS IN A PIPELINE
# -------------------------------------------------------

if __name__ == "__main__":
    # ✅ Sample Dataset
    data = {
        "Age": [25, np.nan, 30, 35, np.nan],
        "Annual Income": [15000, 18000, 20000, 22000, 24000],
        "Spending Score": [39, 81, 6, 77, 40]
    }

    df = pd.DataFrame(data)
    logging.info("\n📌 Original Data:\n")
    print(df)

    # ✅ Apply Functions
    df = fill_missing_values(df, "Age", "median")
    df = scale_features(df, ["Annual Income", "Spending Score"])
    df = run_kmeans(df, ["Annual Income", "Spending Score"], k=3)

    # ✅ Save Processed Data
    df.to_csv("outputs/final_processed_data.csv", index=False)
    logging.info("✅ Final processed dataset saved as 'outputs/final_processed_data.csv'.")

    # ✅ Visualize & Save the Clusters
    plot_clusters(df, ["Annual Income", "Spending Score"])

    logging.info("\n📌 Final Processed Data:\n")
    print(df)

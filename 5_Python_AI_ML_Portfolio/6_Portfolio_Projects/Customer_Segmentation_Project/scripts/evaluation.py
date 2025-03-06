# -------------------------------------------------------
# 📌 CUSTOMER SEGMENTATION: CLUSTER EVALUATION
# -------------------------------------------------------
# This script evaluates the quality of the K-Means clustering results 
# using Silhouette Score and Davies-Bouldin Index.

import pandas as pd
import numpy as np
import logging
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import silhouette_score, davies_bouldin_score

# ✅ Logging setup for tracking evaluation steps
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# -------------------------------------------------------
# 📌 FUNCTION: EVALUATE CLUSTER PERFORMANCE
# -------------------------------------------------------
def evaluate_clusters(df, save_path="segmentation_metrics.txt"):
    """
    Computes Silhouette Score and Davies-Bouldin Index for cluster validation.
    """
    logging.info("\n📌 Evaluating cluster quality...")

    if "Cluster" not in df.columns:
        logging.error("❌ ERROR: No 'Cluster' column found. Ensure clustering has been applied.")
        return

    silhouette = silhouette_score(df.drop(columns=["Cluster"]), df["Cluster"])
    davies_bouldin = davies_bouldin_score(df.drop(columns=["Cluster"]), df["Cluster"])

    # Save evaluation metrics to a text file
    with open(save_path, "w") as f:
        f.write(f"Silhouette Score: {silhouette:.4f}\n")
        f.write(f"Davies-Bouldin Index: {davies_bouldin:.4f}\n")

    logging.info(f"✅ Evaluation metrics saved to '{save_path}'.")
    logging.info(f"🔹 Silhouette Score: {silhouette:.4f}")
    logging.info(f"🔹 Davies-Bouldin Index: {davies_bouldin:.4f}")

    return silhouette, davies_bouldin

# -------------------------------------------------------
# 📌 FUNCTION: VISUALIZE CLUSTER SEPARATION
# -------------------------------------------------------
def plot_clusters(df, save_path="cluster_scatterplot.png"):
    """
    Generates a scatter plot to visualize cluster separation.
    """
    logging.info("\n📌 Generating cluster visualization...")

    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x=df.columns[0], y=df.columns[1], hue="Cluster", palette="viridis", edgecolor="black", s=100)

    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])
    plt.title("Customer Segmentation Clusters")
    plt.legend()
    plt.savefig(save_path)
    plt.show()

    logging.info(f"✅ Cluster scatter plot saved as '{save_path}'.")

# -------------------------------------------------------
# 📌 MAIN EXECUTION
# -------------------------------------------------------
if __name__ == "__main__":
    logging.info("\n🎯 Starting Cluster Evaluation Process...")

    # Load clustered dataset
    df_clustered = pd.read_csv("segmented_customers.csv")

    # Evaluate cluster performance
    evaluate_clusters(df_clustered)

    # Generate cluster visualization
    plot_clusters(df_clustered)

    logging.info("\n✅ 🎯 Cluster Evaluation Completed!")

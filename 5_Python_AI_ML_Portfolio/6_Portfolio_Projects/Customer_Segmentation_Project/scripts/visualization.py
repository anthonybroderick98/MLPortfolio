import os
import logging
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Logging setup for execution tracking
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# -------------------------------------------------------
# 📌 Ensure results directory exists
# -------------------------------------------------------
def ensure_directory_exists(file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

# -------------------------------------------------------
# 📌 FUNCTION: PLOT CUSTOMER SEGMENTATION
# -------------------------------------------------------
def plot_customer_clusters(df, x_feature, y_feature, cluster_col, save_path="../results/customer_segmentation.png"):
    """
    Generates a scatter plot of customer segments.

    Args:
        df (pd.DataFrame): Dataset containing clustering results.
        x_feature (str): Feature for x-axis.
        y_feature (str): Feature for y-axis.
        cluster_col (str): Column containing cluster labels.
        save_path (str): File path for saving the plot.
    """
    logging.info("\n📌 Generating customer segmentation plot...")

    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=x_feature, y=y_feature, hue=cluster_col, palette="viridis", s=100, edgecolor="black")

    plt.xlabel(x_feature)
    plt.ylabel(y_feature)
    plt.title(f"Customer Segmentation: {x_feature} vs {y_feature}")

    # ✅ Ensure directory exists before saving
    ensure_directory_exists(save_path)
    plt.savefig(save_path)
    logging.info(f"✅ Cluster visualization saved as '{save_path}'.")
    plt.close()

# -------------------------------------------------------
# 📌 FUNCTION: FEATURE CORRELATION HEATMAP
# -------------------------------------------------------
def plot_correlation_heatmap(df, save_path="../results/feature_correlation.png"):
    """
    Generates a heatmap showing correlations between numerical features.

    Args:
        df (pd.DataFrame): Input dataset.
        save_path (str): File path for saving the heatmap.
    """
    logging.info("\n📌 Generating feature correlation heatmap...")

    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
    plt.title("Feature Correlation Heatmap")

    ensure_directory_exists(save_path)
    plt.savefig(save_path)
    logging.info(f"✅ Feature correlation heatmap saved as '{save_path}'.")
    plt.close()

# -------------------------------------------------------
# 📌 FUNCTION: ELBOW METHOD PLOT
# -------------------------------------------------------
def plot_elbow_method(inertia_values, k_range, save_path="../results/elbow_method.png"):
    """
    Generates an Elbow Method plot to determine the optimal number of clusters.

    Args:
        inertia_values (list): List of inertia values for different k values.
        k_range (list): List of k values tested.
        save_path (str): File path for saving the elbow method plot.
    """
    logging.info("\n📌 Generating Elbow Method plot...")

    plt.figure(figsize=(8, 6))
    plt.plot(k_range, inertia_values, marker='o', linestyle='--')
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Inertia (WCSS)")
    plt.title("Elbow Method for Optimal k")

    ensure_directory_exists(save_path)
    plt.savefig(save_path)
    logging.info(f"✅ Elbow Method plot saved as '{save_path}'.")
    plt.close()

# -------------------------------------------------------
# 📌 FUNCTION: SILHOUETTE SCORE PLOT
# -------------------------------------------------------
def plot_silhouette_scores(scores, k_range, save_path="../results/silhouette_scores.png"):
    """
    Generates a silhouette score plot to evaluate clustering performance.

    Args:
        scores (list): List of silhouette scores for different k values.
        k_range (list): List of k values tested.
        save_path (str): File path for saving the silhouette score plot.
    """
    logging.info("\n📌 Generating silhouette score plot...")

    plt.figure(figsize=(8, 6))
    plt.plot(k_range, scores, marker='s', linestyle='-', color="darkorange")
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Silhouette Score")
    plt.title("Silhouette Score for Cluster Evaluation")

    ensure_directory_exists(save_path)
    plt.savefig(save_path)
    logging.info(f"✅ Silhouette score plot saved as '{save_path}'.")
    plt.close()

# -------------------------------------------------------
# 📌 MAIN EXECUTION
# -------------------------------------------------------
if __name__ == "__main__":
    logging.info("\n🎯 Running Visualization Module...")

    # Load clustered dataset
    df = pd.read_csv("../results/cluster_assignments.csv")

    # Generate segmentation scatter plot
    plot_customer_clusters(df, "Annual Income", "Spending Score", "Cluster")

    # Generate feature correlation heatmap
# Ensure the file exists before reading
    processed_data_path = "../results/processed_customer_data.csv"

if os.path.exists(processed_data_path):
    df_raw = pd.read_csv("../results/processed_customer_data.csv")
    plot_correlation_heatmap(df_raw)
else:
    logging.warning(f"⚠ Processed customer data file not found: {processed_data_path}")
    logging.warning("Skipping correlation heatmap generation.")
    plot_correlation_heatmap(df_raw)

    logging.info("\n✅ 🎯 Visualization Process Completed!")

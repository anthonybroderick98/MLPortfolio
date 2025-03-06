# -------------------------------------------------------
# 📌 CUSTOMER SEGMENTATION USING K-MEANS
# -------------------------------------------------------
# This script applies K-Means clustering to group customers 
# based on spending behavior and income.

import os
import pandas as pd
import numpy as np
import joblib  # For saving the trained model
import logging
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# ✅ Logging setup for execution tracking
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Ensure necessary directories exist
os.makedirs("../results", exist_ok=True)
os.makedirs("../models", exist_ok=True)

# -------------------------------------------------------
# 📌 FUNCTION: FIND OPTIMAL CLUSTER COUNT
# -------------------------------------------------------
def find_optimal_clusters(df, max_k=10, save_path="../results/elbow_silhouette_plot.png"):
    """
    Determines the best number of clusters using the Elbow and Silhouette methods.
    Prevents silhouette score errors by ensuring K is within the valid range.
    """
    logging.info("\n📌 Running cluster optimization...")

    n_samples = df.shape[0]
    valid_max_k = min(max_k, n_samples - 1)  # Prevents K exceeding valid range

    if valid_max_k < 2:
        logging.warning("⚠ Not enough data points for clustering. Defaulting to K=2.")
        return 2  # Defaulting to at least 2 clusters

    inertia = []
    silhouette_scores = []
    k_range = range(2, valid_max_k + 1)

    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(df)
        inertia.append(kmeans.inertia_)

        # Compute silhouette score only if K < n_samples
        if k < n_samples:
            silhouette_scores.append(silhouette_score(df, kmeans.labels_))
        else:
            silhouette_scores.append(-1)  # Invalid silhouette score case

    # ✅ Plot Elbow & Silhouette Scores
    fig, ax1 = plt.subplots(figsize=(8, 5))
    ax1.plot(k_range, inertia, marker='o', linestyle='--', label="Inertia (Elbow Method)", color="blue")
    ax1.set_xlabel("Number of Clusters (K)")
    ax1.set_ylabel("Inertia", color="blue")

    ax2 = ax1.twinx()
    ax2.plot(k_range, silhouette_scores, marker='s', linestyle='--', color="green", label="Silhouette Score")
    ax2.set_ylabel("Silhouette Score", color="green")

    plt.title("Elbow & Silhouette Method for Optimal K")
    ax1.legend(loc="upper left")
    ax2.legend(loc="upper right")

    plt.savefig(save_path)
    logging.info(f"✅ Elbow & Silhouette plot saved as '{save_path}'.")
    plt.close()

    optimal_k = k_range[np.argmax(silhouette_scores)]  # Select K with highest silhouette score
    logging.info(f"✅ Optimal number of clusters determined: {optimal_k}")

    return optimal_k

# -------------------------------------------------------
# 📌 FUNCTION: APPLY K-MEANS CLUSTERING
# -------------------------------------------------------
def apply_kmeans(df, k, save_path="../results/cluster_assignments.csv", model_path="../models/kmeans_model.pkl"):
    """
    Runs K-Means clustering on the dataset with the determined K.
    Saves the clustered data and trained K-Means model.
    
    Args:
        df (pd.DataFrame): The dataset for clustering.
        k (int): The optimal number of clusters.
        save_path (str): File path to save clustered customer assignments.
        model_path (str): File path to save the trained K-Means model.

    Returns:
        tuple: (Clustered DataFrame, Cluster Centroids)
    """
    logging.info(f"\n📌 Applying K-Means clustering with {k} clusters...")

    # ✅ Edge Case: Prevent K from exceeding unique data points
    unique_points = len(df.drop_duplicates())
    if k > unique_points:
        logging.warning(f"⚠ Warning: K ({k}) is greater than unique data points ({unique_points}). Reducing K to {unique_points}.")
        k = unique_points  # Reduce K to the number of unique points

    # ✅ Initialize and Fit K-Means Model
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    df["Cluster"] = kmeans.fit_predict(df)

    # ✅ Save cluster assignments
    df.to_csv(save_path, index=False)
    logging.info(f"✅ Clustered data saved as '{save_path}'.")

    # ✅ Save the trained K-Means model
    joblib.dump(kmeans, model_path)
    logging.info(f"✅ K-Means model saved as '{model_path}'.")

    return df, kmeans.cluster_centers_

# -------------------------------------------------------
# 📌 FUNCTION: SAVE CLUSTER CENTROIDS
# -------------------------------------------------------
def save_cluster_centroids(centroids, save_path="../results/cluster_centroids.csv"):
    """
    Saves the cluster centroids for reference.
    """
    logging.info("\n📌 Saving cluster centroids...")

    np.savetxt(save_path, centroids, delimiter=",", header="Centroid1,Centroid2", comments='')
    logging.info(f"✅ Cluster centroids saved as '{save_path}'.")

# -------------------------------------------------------
# 📌 MAIN EXECUTION
# -------------------------------------------------------
if __name__ == "__main__":
    logging.info("\n🎯 Starting K-Means Clustering Process...")

    # ✅ Load selected features
    file_path = "../results/selected_features.csv"
    try:
        df = pd.read_csv(file_path)
        logging.info(f"✅ Loaded dataset with shape: {df.shape}")
    except FileNotFoundError:
        logging.error(f"❌ ERROR: Missing file '{file_path}'. Ensure feature selection is completed.")
        exit()

    # ✅ Determine the optimal number of clusters
    optimal_k = find_optimal_clusters(df)

    # ✅ Apply K-Means with optimal K
    df_clustered, centroids = apply_kmeans(df, optimal_k)

    # ✅ Save cluster centroids
    save_cluster_centroids(centroids)

    logging.info("\n✅ 🎯 K-Means Clustering Completed!")

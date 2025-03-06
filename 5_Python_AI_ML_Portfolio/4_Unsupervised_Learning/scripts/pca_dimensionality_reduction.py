# -------------------------------------------------------
# PCA DIMENSIONALITY REDUCTION & CUSTOMER SEGMENTATION
# -------------------------------------------------------

# This script reduces high-dimensional customer data using PCA, applies clustering, 
# and generates necessary visualizations.

import os
import pandas as pd  # Data handling
import numpy as np  # Numerical computations
import matplotlib.pyplot as plt  # Static visualizations
import seaborn as sns  # Heatmaps
import plotly.express as px  # Interactive visualizations
from sklearn.decomposition import PCA  # PCA algorithm
from sklearn.preprocessing import StandardScaler  # Standardization
from sklearn.cluster import KMeans  # K-Means clustering

# ✅ Ensure necessary output directories exist
os.makedirs("outputs", exist_ok=True)

# -------------------------------------------------------
# CREATING SAMPLE HIGH-DIMENSIONAL DATA
# -------------------------------------------------------

# Generate a small dataset with multiple features to simulate customer data
print("\n📌 Creating Sample High-Dimensional Data")
data = {
    "Annual Income": [15, 16, 17, 35, 37, 40, 75, 77, 80, 85],
    "Spending Score": [39, 81, 6, 77, 40, 76, 10, 4, 90, 88],
    "Age": [18, 22, 28, 45, 39, 50, 55, 42, 30, 21],
    "Membership Duration": [1, 2, 3, 5, 6, 8, 10, 7, 4, 2],
    "Discount Usage": [3, 5, 2, 8, 9, 6, 4, 7, 5, 3]
}

df = pd.DataFrame(data)

# ✅ Save raw data
df.to_csv("outputs/raw_customer_data.csv", index=False)
print("✅ Data saved as 'outputs/raw_customer_data.csv'")

# -------------------------------------------------------
# STANDARDIZING THE DATA
# -------------------------------------------------------

# StandardScaler ensures all features contribute equally to PCA by:
# - Centering values around 0 (mean = 0)
# - Scaling features to have the same standard deviation
print("\n📌 Standardizing Features for PCA")
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# -------------------------------------------------------
# APPLYING PRINCIPAL COMPONENT ANALYSIS (PCA)
# -------------------------------------------------------

# PCA reduces dimensionality while preserving important data patterns.
print("\n📌 Applying Principal Component Analysis (PCA)")
pca = PCA(n_components=2)  # Reduce data to 2 dimensions for visualization
df_pca = pca.fit_transform(df_scaled)

# ✅ Save PCA-transformed data
df_pca_df = pd.DataFrame(df_pca, columns=["PC1", "PC2"])
df_pca_df.to_csv("outputs/pca_transformed_data.csv", index=False)
print("✅ PCA-transformed data saved as 'outputs/pca_transformed_data.csv'")

# -------------------------------------------------------
# VISUALIZING PCA EXPLAINED VARIANCE
# -------------------------------------------------------

# The variance explained ratio tells us how much information PCA retains.
explained_variance = pca.explained_variance_ratio_
print(f"\n📌 Variance Captured by PCA Components: {explained_variance}")

plt.figure(figsize=(8, 5))
plt.bar(["PC1", "PC2"], explained_variance * 100, color=["blue", "green"])
plt.xlabel("Principal Components")
plt.ylabel("Explained Variance (%)")
plt.title("Variance Explained by PCA Components")

# ✅ Save PCA variance plot
plt.savefig("outputs/pca_variance_explained.png")
plt.show()
print("✅ PCA variance plot saved as 'outputs/pca_variance_explained.png'")

# -------------------------------------------------------
# APPLYING K-MEANS CLUSTERING ON PCA DATA
# -------------------------------------------------------

# Now that we’ve reduced dimensions, we apply K-Means to group similar customers.
print("\n📌 Applying K-Means on Reduced Dimensions")
optimal_k = 3  # Based on previous elbow method analysis
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
clusters = kmeans.fit_predict(df_pca)

df_pca_df["Cluster"] = clusters

# ✅ Save clustered PCA-transformed data
df_pca_df.to_csv("outputs/pca_clustered_data.csv", index=False)
print("✅ PCA-clustered data saved as 'outputs/pca_clustered_data.csv'")

# -------------------------------------------------------
# VISUALIZING PCA-REDUCED CLUSTERS (STATIC)
# -------------------------------------------------------

# A 2D scatter plot showing clustered customer segments after PCA.
plt.figure(figsize=(8, 5))
plt.scatter(df_pca[:, 0], df_pca[:, 1], c=clusters, cmap="viridis", edgecolors="k")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA-Based Customer Segmentation")
plt.colorbar(label="Cluster")

# ✅ Save PCA scatter plot
plt.savefig("outputs/pca_customer_segmentation.png")
plt.show()
print("✅ PCA customer segmentation plot saved as 'outputs/pca_customer_segmentation.png'")

# -------------------------------------------------------
# INTERACTIVE PCA-BASED CLUSTERING VISUALIZATION
# -------------------------------------------------------

# Interactive visualization for better analysis of PCA-based clusters.
fig = px.scatter(
    df_pca_df, x="PC1", y="PC2", color=df_pca_df["Cluster"].astype(str),
    title="Interactive PCA-Based Customer Segmentation",
    labels={"PC1": "Principal Component 1", "PC2": "Principal Component 2", "Cluster": "Cluster"}
)

# ✅ Save interactive visualization
fig.write_html("outputs/interactive_pca_segmentation.html")
print("✅ Interactive PCA segmentation saved as 'outputs/interactive_pca_segmentation.html'")

# -------------------------------------------------------
# FINAL OUTPUT SUMMARY
# -------------------------------------------------------

print("\n📌 Final PCA-Reduced Data with Cluster Assignments:\n", df_pca_df.head())


# -------------------------------------------------------
# FEATURE SELECTION FOR CUSTOMER SEGMENTATION
# -------------------------------------------------------

# This script selects the most important features for clustering, applies K-Means clustering,
# and ensures all output files (correlation heatmap, feature rankings, segmented customers) are saved.

import os
import pandas as pd  # Data handling
import numpy as np  # Numerical operations
import matplotlib.pyplot as plt  # Static visualizations
import seaborn as sns  # Correlation heatmaps
import plotly.express as px  # Interactive visualizations
from sklearn.ensemble import RandomForestRegressor  # Feature importance ranking
from sklearn.preprocessing import StandardScaler  # Feature scaling
from sklearn.cluster import KMeans  # K-Means clustering
from sklearn.metrics import silhouette_score  # Clustering evaluation metric

import warnings
warnings.simplefilter("ignore", UserWarning)  # Suppress sklearn warnings

# -------------------------------------------------------
# ENSURE OUTPUT DIRECTORIES EXIST
# -------------------------------------------------------

output_dirs = ["data", "outputs", "results"]
for directory in output_dirs:
    os.makedirs(directory, exist_ok=True)

# -------------------------------------------------------
# LOAD CUSTOMER DATA
# -------------------------------------------------------

print("\n📌 Loading Customer Data")

np.random.seed(42)
data = {
    "Annual Income": np.random.randint(20, 120, 30),
    "Spending Score": np.random.randint(1, 100, 30),
    "Age": np.random.randint(18, 65, 30),
    "Membership Duration (Years)": np.random.randint(1, 15, 30),
    "Transactions Per Year": np.random.randint(5, 50, 30)
}

df = pd.DataFrame(data)

# ✅ Save dataset
customer_data_path = "data/customer_data.csv"
df.to_csv(customer_data_path, index=False)
print(f"✅ Data saved as '{customer_data_path}'")
print(df.head())

# -------------------------------------------------------
# GENERATE CORRELATION HEATMAP
# -------------------------------------------------------

print("\n📌 Generating Correlation Heatmap")

correlation_matrix = df.corr()
plt.figure(figsize=(8, 5))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Feature Correlation Matrix")

# ✅ Save heatmap
heatmap_path = "outputs/correlation_heatmap.png"
plt.savefig(heatmap_path)
plt.show()
print(f"✅ Correlation heatmap saved as '{heatmap_path}'")

# -------------------------------------------------------
# COMPUTE FEATURE IMPORTANCE
# -------------------------------------------------------

print("\n📌 Computing Feature Importance")

X = df.drop(columns=["Spending Score"])  # Predictors
y = df["Spending Score"]  # Target variable

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Rank features by importance
feature_importance = pd.DataFrame(model.feature_importances_, index=X.columns, columns=["Importance"]).sort_values(by="Importance", ascending=False)
print("\n📌 Feature Importance Ranking:\n", feature_importance)

# ✅ Save feature importance ranking
feature_importance_path = "outputs/feature_importance.csv"
feature_importance.to_csv(feature_importance_path)
print(f"✅ Feature importance saved as '{feature_importance_path}'")

# -------------------------------------------------------
# SELECT TOP FEATURES
# -------------------------------------------------------

top_features = feature_importance.index[:2]  # Select the top 2 most influential features
df_selected = df[top_features]

# ✅ Save selected features dataset
selected_features_path = "outputs/selected_features.csv"
df_selected.to_csv(selected_features_path, index=False)
print(f"✅ Selected features saved as '{selected_features_path}'")

# -------------------------------------------------------
# SCALE SELECTED FEATURES
# -------------------------------------------------------

print("\n📌 Scaling Selected Features")
scaler = StandardScaler()
df_selected_scaled = scaler.fit_transform(df_selected)

# -------------------------------------------------------
# FIND OPTIMAL NUMBER OF CLUSTERS (ELBOW & SILHOUETTE)
# -------------------------------------------------------

print("\n📌 Finding Optimal Clusters (Elbow & Silhouette Method)")

inertia = []
silhouette_scores = []
k_range = range(2, 10)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(df_selected_scaled)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(df_selected_scaled, kmeans.labels_))

# ✅ Save silhouette scores
silhouette_path = "outputs/elbow_silhouette_scores.csv"
np.savetxt(silhouette_path, np.column_stack((k_range, inertia, silhouette_scores)), delimiter=",", header="k,Inertia,Silhouette Score", comments="")
print(f"✅ Silhouette scores saved as '{silhouette_path}'")

# -------------------------------------------------------
# PLOT ELBOW & SILHOUETTE SCORES
# -------------------------------------------------------

plt.figure(figsize=(10, 5))
plt.plot(k_range, inertia, marker='o', linestyle='--', label="Inertia")
plt.plot(k_range, silhouette_scores, marker='s', linestyle='--', label="Silhouette Score", color="green")
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Metric')
plt.title('Elbow & Silhouette Method for Optimal k')
plt.legend()

# ✅ Save elbow & silhouette visualization
elbow_silhouette_path = "outputs/elbow_silhouette_method.png"
plt.savefig(elbow_silhouette_path)
plt.show()
print(f"✅ Elbow & Silhouette plot saved as '{elbow_silhouette_path}'")

# -------------------------------------------------------
# APPLY K-MEANS CLUSTERING
# -------------------------------------------------------

optimal_k = k_range[np.argmax(silhouette_scores)]
print(f"\n📌 Optimal number of clusters: {optimal_k}")

kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(df_selected_scaled)

# ✅ Save clustered data
segmented_path = "outputs/segmented_customers.csv"
df.to_csv(segmented_path, index=False)
print(f"✅ Segmented customer data saved as '{segmented_path}'")

# -------------------------------------------------------
# VISUALIZE OPTIMIZED CLUSTERS
# -------------------------------------------------------

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x=top_features[0], y=top_features[1], hue="Cluster", palette="viridis", edgecolor="k", s=100)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', label="Centroids", edgecolors="k")
plt.xlabel(top_features[0])
plt.ylabel(top_features[1])
plt.title("Optimized Customer Segmentation")
plt.legend()

# ✅ Save static visualization
optimized_cluster_path = "outputs/optimized_customer_segmentation.png"
plt.savefig(optimized_cluster_path)
plt.show()
print(f"✅ Optimized segmentation saved as '{optimized_cluster_path}'")

# -------------------------------------------------------
# GENERATE INTERACTIVE VISUALIZATION
# -------------------------------------------------------

interactive_path = "outputs/interactive_customer_segmentation.html"
fig = px.scatter(df, x=top_features[0], y=top_features[1], color=df["Cluster"], title="Interactive Customer Segmentation")
fig.write_html(interactive_path)
print(f"✅ Interactive segmentation saved as '{interactive_path}'")

print("\n📌 Final Segmented Data with Optimized Features:\n", df.head())


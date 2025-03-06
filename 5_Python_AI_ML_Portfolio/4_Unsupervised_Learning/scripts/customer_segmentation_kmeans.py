# -------------------------------------------------------
# CUSTOMER SEGMENTATION FEATURE SELECTION
# -------------------------------------------------------

# This script performs feature selection and clustering for customer segmentation. 
# It applies K-Means clustering to segment customers based on spending behavior.

import pandas as pd  # Data handling
import numpy as np  # Numerical operations
import matplotlib.pyplot as plt  # Visualization
import seaborn as sns  # Statistical visualizations
import plotly.express as px  # Interactive plots
from sklearn.cluster import KMeans  # K-Means clustering
from sklearn.preprocessing import StandardScaler  # Feature scaling
from sklearn.metrics import silhouette_score  # Clustering evaluation

import warnings
warnings.simplefilter("ignore", UserWarning)

# -------------------------------------------------------
# LOADING CUSTOMER DATA
# -------------------------------------------------------

print("\n📌 Loading Customer Data...")

# Load the customer dataset
df = pd.read_csv("../data/customer_data.csv")  

print(df.head())  # Confirm data loaded

# -------------------------------------------------------
# SCALING DATA FOR CLUSTERING
# -------------------------------------------------------

print("\n📌 Scaling Data for Clustering")

scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

df_scaled.to_csv("scaled_customer_data.csv", index=False)
print("✅ Scaled data saved as 'scaled_customer_data.csv'.")

# -------------------------------------------------------
# FINDING THE OPTIMAL NUMBER OF CLUSTERS
# -------------------------------------------------------

print("\n📌 Finding Optimal Clusters")

inertia, silhouette_scores = [], []
k_range = range(2, 10)  

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)  
    silhouette_scores.append(silhouette_score(df_scaled, kmeans.labels_))  

np.savetxt("elbow_silhouette_scores.csv", np.column_stack([k_range, inertia, silhouette_scores]),
           delimiter=",", header="k,Inertia,Silhouette", comments='')

print("✅ Elbow & Silhouette Scores saved as 'elbow_silhouette_scores.csv'.")

# -------------------------------------------------------
# VISUALIZING ELBOW & SILHOUETTE SCORES
# -------------------------------------------------------

plt.figure(figsize=(8, 5))
plt.plot(k_range, inertia, marker='o', linestyle='--', label="Inertia")
plt.plot(k_range, silhouette_scores, marker='s', linestyle='--', label="Silhouette Score", color="green")

plt.xlabel("Number of Clusters (K)")
plt.ylabel("Metric")
plt.title("Elbow & Silhouette Method for Optimal K")
plt.legend()
plt.grid()

plt.savefig("elbow_silhouette_method.png")  
plt.show()

print("✅ Elbow Method plot saved as 'elbow_silhouette_method.png'.")

# -------------------------------------------------------
# APPLYING K-MEANS CLUSTERING
# -------------------------------------------------------

optimal_k = k_range[np.argmax(silhouette_scores)]  
print(f"\n📌 Optimal number of clusters: {optimal_k}")

kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(df_scaled)  

df.to_csv("segmented_customers.csv", index=False)
print("✅ Clustered data saved as 'segmented_customers.csv'.")

# -------------------------------------------------------
# VISUALIZING CUSTOMER SEGMENTATION (FIXED)
# -------------------------------------------------------

print("\n📌 Generating Customer Segmentation Plot")

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Annual Income", y="Spending Score", hue="Cluster", palette="viridis", edgecolor="black", s=100)
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.legend()

plt.savefig("customer_segmentation.png")  
plt.show()

print("✅ Customer segmentation plot saved as 'customer_segmentation.png'.")

# -------------------------------------------------------
# INTERACTIVE HTML VISUALIZATION
# -------------------------------------------------------

print("\n📌 Creating Interactive Customer Segmentation Visualization")

fig = px.scatter(df, x="Annual Income", y="Spending Score", color=df["Cluster"],
                 title="Interactive Customer Segmentation")

fig.write_html("interactive_customer_segmentation.html")

print("✅ Interactive visualization saved as 'interactive_customer_segmentation.html'.")

# -------------------------------------------------------
# SAVING CLUSTER CENTROIDS
# -------------------------------------------------------

print("\n📌 Saving Cluster Centroids")

centroids = scaler.inverse_transform(kmeans.cluster_centers_)

np.savetxt("cluster_centroids.csv", centroids, delimiter=",",
           header="Annual Income,Spending Score", comments='')

print("✅ Cluster centroids saved as 'cluster_centroids.csv'.")

# -------------------------------------------------------
# GENERATING FINAL HTML REPORT (FIXED)
# -------------------------------------------------------

print("\n📌 Generating Final Customer Segmentation Report")

html_report = f"""
<html>
<head><title>Customer Segmentation Report</title></head>
<body>
<h1>Customer Segmentation Results</h1>
<p><strong>Optimal Number of Clusters:</strong> {optimal_k}</p>
<p><a href='customer_segmentation.png'>📊 View Cluster Plot</a></p>
<p><a href='interactive_customer_segmentation.html'>🌍 View Interactive Segmentation</a></p>
<p><a href='segmented_customers.csv'>📂 Download Clustered Data</a></p>
<p><a href='cluster_centroids.csv'>📌 Download Cluster Centroids</a></p>
</body>
</html>
"""

with open("customer_segmentation_report.html", "w") as f:
    f.write(html_report)

print("✅ Report saved as 'customer_segmentation_report.html'.")

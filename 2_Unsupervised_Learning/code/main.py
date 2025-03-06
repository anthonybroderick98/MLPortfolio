# ------------------------------------------------------------
# Titanic Passenger Clustering using K-Means
# ------------------------------------------------------------
# This script applies K-Means clustering to segment Titanic passengers
# into meaningful groups based on demographic and ticketing features.
#
# Steps:
# 1. Load and preprocess the dataset
# 2. Scale numerical features
# 3. Determine the optimal number of clusters using Silhouette Score
# 4. Apply K-Means clustering and analyze results
# 5. Reduce dimensions with PCA for visualization
# 6. Save the clustered dataset
# ------------------------------------------------------------

# 📌 Step 1: Import Required Libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

# ------------------------------------------------------------
# 📌 Step 2: Load the Titanic Dataset
# ------------------------------------------------------------

# Define dataset file path
file_path = r"C:\Users\antho\Documents\AI and ML Internship Projects\2_Unsupervised_Learning\data\raw\titanic.csv"

# Load dataset into a Pandas DataFrame
df = pd.read_csv(file_path)

print("\n✅ Dataset Loaded Successfully!")
print(df.info())  # Check dataset structure
print(df.head())  # Preview first few rows

# ------------------------------------------------------------
# 📌 Step 3: Data Preprocessing
# ------------------------------------------------------------

# Drop non-numeric and irrelevant columns
df.drop(columns=["Name", "Ticket", "Cabin"], inplace=True)

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())  # Replace missing Age with median
df["Fare"] = df["Fare"].fillna(df["Fare"].median())  # Replace missing Fare with median
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])  # Fill missing Embarked with most common value

# Encode categorical variables
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})  # Convert gender to numerical
df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)  # One-hot encode Embarked column

# Select features relevant for clustering
features = ["Pclass", "Sex", "Age", "Fare", "SibSp", "Parch"]
X = df[features]

# Standardize Features to improve clustering performance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\n✅ Data Preprocessing Completed!")
print(pd.DataFrame(X_scaled, columns=features).head())  # Preview standardized features

# ------------------------------------------------------------
# 📌 Step 4: Determine the Optimal Number of Clusters (K)
# ------------------------------------------------------------

print("\n🔍 Finding the optimal number of clusters using Silhouette Score...")

optimal_k = 2  # Default starting value
best_score = -1  # Initial value for silhouette score comparison

for k in range(2, 6):  # Evaluate K from 2 to 5 to find the most meaningful clusters
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels)

    print(f"Tested K={k}, Silhouette Score={score:.2f}")

    # Select the best K based on highest silhouette score
    if score > best_score:
        best_score = score
        optimal_k = k

print(f"\n✅ Best K Found: {optimal_k} with Silhouette Score: {best_score:.2f}")

# ------------------------------------------------------------
# 📌 Step 5: Apply K-Means Clustering
# ------------------------------------------------------------

# Apply K-Means clustering with optimal K
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)

print("\n✅ K-Means Clustering Completed with Optimal K!")
print(df[["Pclass", "Sex", "Age", "Fare", "Cluster"]].head())  # Preview clustering results

# ------------------------------------------------------------
# 📌 Step 6: Evaluate Clustering Performance
# ------------------------------------------------------------

# Compute silhouette score for final model
sil_score = silhouette_score(X_scaled, df["Cluster"])
print(f"\n✅ Final Silhouette Score: {sil_score:.2f} (Higher is better!)")

# ------------------------------------------------------------
# 📌 Step 7: Visualizing the Clusters (PCA Reduction)
# ------------------------------------------------------------

# Reduce feature dimensions for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Assign PCA components to the DataFrame
df["PCA1"] = X_pca[:, 0]
df["PCA2"] = X_pca[:, 1]

# Generate a PCA scatter plot
plt.figure(figsize=(8,6))
sns.scatterplot(x=df["PCA1"], y=df["PCA2"], hue=df["Cluster"], palette="viridis")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title(f"Titanic Passenger Clusters (Optimal K={optimal_k})")
plt.legend(title="Cluster")
plt.savefig("results/plots/titanic_cluster_pca.png")  # Save plot
plt.show()

# ------------------------------------------------------------
# 📌 Step 8: Save the Clustered Dataset
# ------------------------------------------------------------

# Define output directory and ensure it exists
output_path = r"C:\Users\antho\Documents\AI and ML Internship Projects\2_Unsupervised_Learning\results\output"
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Save the clustered dataset
df.to_csv(os.path.join(output_path, "titanic_clusters.csv"), index=False)

print(f"\n✅ Clustered Data Successfully Saved: {output_path}/titanic_clusters.csv")

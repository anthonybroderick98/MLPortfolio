# ---------------------------------------------------
# Titanic Passenger Clustering - Visualization Script
# ---------------------------------------------------
# This script generates key visualizations to analyze
# the clustering results of Titanic passengers using
# unsupervised learning techniques.
#
# Plots Included:
# 1. Elbow Method - Determine the optimal number of clusters (K)
# 2. Silhouette Scores - Measure cluster quality
# 3. PCA Visualization - Reduce dimensions for better interpretation
# 4. Feature Correlation Heatmap - Identify relationships between variables
# 5. Boxplots - Visualize distribution of key features
#
# All visualizations are saved in the 'results/plots/' directory.
# ---------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import pandas as pd
import numpy as np

# ---------------------------------------------------
# 1️⃣ Load the Dataset
# ---------------------------------------------------

# Define file path to Titanic dataset
file_path = r"C:\Users\antho\Documents\AI and ML Internship Projects\2_Unsupervised_Learning\data\raw\titanic.csv"

# Load dataset into a Pandas DataFrame
df = pd.read_csv(file_path)

# ---------------------------------------------------
# 2️⃣ Data Preprocessing
# ---------------------------------------------------

# Handle missing values
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Fare"].fillna(df["Fare"].median(), inplace=True)

# Encode categorical variables
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)

# Select features relevant for clustering (excluding 'Survived' or other labels)
features = ["Pclass", "Age", "Fare", "Sex", "SibSp", "Parch"]
X = df[features]

# ---------------------------------------------------
# 3️⃣ Visualization Functions
# ---------------------------------------------------

# 📌 Elbow Method - Determine optimal K
def plot_elbow_method(X):
    """
    Generates an Elbow Plot to help determine the best 
    number of clusters (K) using Within-Cluster Sum of Squares (WCSS).
    """
    distortions = []
    K_range = range(1, 10)

    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X)
        distortions.append(kmeans.inertia_)

    plt.figure(figsize=(8, 6))
    plt.plot(K_range, distortions, marker='o', linestyle='-')
    plt.xlabel('Number of Clusters (K)')
    plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
    plt.title('Elbow Method to Determine Optimal K')
    plt.savefig("results/plots/unsupervised_elbow_method.png")
    plt.close()

# 📌 Silhouette Score - Measure cluster quality
def plot_silhouette_score(X):
    """
    Generates a plot of Silhouette Scores for different values of K
    to evaluate how well clusters are separated.
    """
    silhouette_scores = []
    K_range = range(2, 10)

    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(X)
        silhouette_scores.append(silhouette_score(X, labels))

    plt.figure(figsize=(8, 6))
    plt.plot(K_range, silhouette_scores, marker='o', linestyle='-')
    plt.xlabel('Number of Clusters (K)')
    plt.ylabel('Silhouette Score')
    plt.title('Silhouette Scores for Clustering')
    plt.savefig("results/plots/unsupervised_silhouette_scores.png")
    plt.close()

# 📌 PCA Visualization - Reduce dimensions for clustering interpretation
def plot_pca_clusters(X):
    """
    Reduces feature dimensions using PCA and visualizes clusters 
    in 2D space.
    """
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=labels, palette='viridis')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('PCA Visualization of Clusters')
    plt.legend(title='Cluster')
    plt.savefig("results/plots/unsupervised_pca_clusters.png")
    plt.close()

# 📌 Feature Correlation Heatmap - Identify relationships between features
def plot_feature_heatmap(X):
    """
    Generates a heatmap showing correlation between features
    to help understand which attributes are strongly related.
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(pd.DataFrame(X).corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Feature Correlation Heatmap')
    plt.savefig("results/plots/unsupervised_feature_heatmap.png")
    plt.close()

# 📌 Boxplots - Visualize feature distribution across different groups
def plot_boxplot(df, feature, label="Pclass"):
    """
    Generates boxplots to visualize how a specific feature
    is distributed across different classes or groups.
    """
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x=label, y=feature, palette='Set2')
    plt.title(f'{feature} Distribution by {label}')
    plt.savefig(f"results/plots/{feature}_boxplot_by_{label}.png")
    plt.close()

# ---------------------------------------------------
# 4️⃣ Generate and Save Plots
# ---------------------------------------------------

plot_elbow_method(X)
plot_silhouette_score(X)
plot_pca_clusters(X)
plot_feature_heatmap(X)
plot_boxplot(df, "Age")
plot_boxplot(df, "Fare")

# Print completion message
print("✅ Unsupervised learning visualizations have been successfully generated! Check the 'results/plots' directory.")

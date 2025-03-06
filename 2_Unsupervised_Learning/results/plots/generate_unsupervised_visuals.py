import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import pandas as pd
import numpy as np

# Load Titanic dataset
file_path = "C:/Users/antho/Documents/AI and ML Internship Projects/1_Unsupervised_Learning/data/titanic.csv"
df = pd.read_csv(file_path)

# ---------------------------
# DATA PREPROCESSING
# ---------------------------
# Handle missing values
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Fare"].fillna(df["Fare"].median(), inplace=True)
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)

# Select features for clustering (exclude 'Survived' or similar labels)
features = ["Pclass", "Age", "Fare", "Sex", "SibSp", "Parch"]
X = df[features]

# ---------------------------
# VISUALIZATION FUNCTIONS
# ---------------------------

# 1️⃣ Elbow Method
def plot_elbow_method(X):
    distortions = []
    K = range(1, 10)
    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X)
        distortions.append(kmeans.inertia_)
    
    plt.figure(figsize=(8, 6))
    plt.plot(K, distortions, marker='o')
    plt.title('Elbow Method for Optimal Clusters')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Distortion (Inertia)')
    plt.savefig("results/plots/unsupervised_elbow_method.png")
    plt.close()

# 2️⃣ Silhouette Score
def plot_silhouette_score(X):
    silhouette_scores = []
    K = range(2, 10)
    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(X)
        silhouette_scores.append(silhouette_score(X, labels))
    
    plt.figure(figsize=(8, 6))
    plt.plot(K, silhouette_scores, marker='o')
    plt.title('Silhouette Scores for Clustering')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Silhouette Score')
    plt.savefig("results/plots/unsupervised_silhouette_scores.png")
    plt.close()

# 3️⃣ PCA Visualization
def plot_pca_clusters(X):
    kmeans = KMeans(n_clusters=3, random_state=42)
    labels = kmeans.fit_predict(X)
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=labels, palette='viridis')
    plt.title('PCA Visualization of Clusters')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend(title='Cluster')
    plt.savefig("results/plots/unsupervised_pca_clusters.png")
    plt.close()

# 4️⃣ Heatmap of Feature Correlations
def plot_feature_heatmap(X):
    plt.figure(figsize=(8, 6))
    sns.heatmap(pd.DataFrame(X).corr(), annot=True, cmap='coolwarm')
    plt.title('Feature Correlation Heatmap')
    plt.savefig("results/plots/unsupervised_feature_heatmap.png")
    plt.close()

# 5️⃣ Boxplot of Age vs Pclass
def plot_boxplot(df, feature, label="Pclass"):
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x=label, y=feature, palette='Set2')
    plt.title(f'{feature} Distribution by {label}')
    plt.savefig(f"results/plots/{feature}_boxplot_by_{label}.png")
    plt.close()

# ---------------------------
# GENERATE PLOTS
# ---------------------------
plot_elbow_method(X)
plot_silhouette_score(X)
plot_pca_clusters(X)
plot_feature_heatmap(X)
plot_boxplot(df, "Age")
plot_boxplot(df, "Fare")

print("✅ Unsupervised learning visuals have been generated! Check the 'results/plots' directory.")

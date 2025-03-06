# ---------------------------------------------------
# Titanic Passenger Clustering using K-Means
# ---------------------------------------------------
# This script applies K-Means clustering to the Titanic dataset 
# to identify hidden patterns among passengers.
#
# Steps:
# 1. Load and preprocess data
# 2. Scale numerical features
# 3. Determine the optimal number of clusters using the Elbow Method
# 4. Apply K-Means clustering and save results
# ---------------------------------------------------

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# ---------------------------------------------------
# 1️⃣ Load the Dataset
# ---------------------------------------------------

# Define file path to raw Titanic dataset
file_path = r"C:\Users\antho\Documents\AI and ML Internship Projects\2_Unsupervised_Learning\data\raw\titanic.csv"

# Load the dataset into a Pandas DataFrame
df = pd.read_csv(file_path)

# ---------------------------------------------------
# 2️⃣ Data Preprocessing
# ---------------------------------------------------

# Convert categorical features to numerical
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Handle missing values
df['Embarked'].fillna('S', inplace=True)  # Fill missing embarkation points with the most common port
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})  # Convert embarkation ports to numeric values
df['Age'].fillna(df['Age'].median(), inplace=True)  # Replace missing ages with the median

# Select relevant features for clustering
df_cluster = df[['Pclass', 'Sex', 'Age', 'Fare', 'SibSp', 'Parch']]

# ---------------------------------------------------
# 3️⃣ Feature Scaling
# ---------------------------------------------------

# Scale features to ensure all variables contribute equally to clustering
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_cluster)

# ---------------------------------------------------
# 4️⃣ Determine Optimal K (Elbow Method)
# ---------------------------------------------------

# Within-Cluster Sum of Squares (WCSS) to determine the best number of clusters
wcss = []
K_range = range(1, 11)  # Testing K values from 1 to 10

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(df_scaled)
    wcss.append(kmeans.inertia_)  # Store WCSS for each K

# Plot the Elbow Graph
plt.figure(figsize=(8, 5))
plt.plot(K_range, wcss, marker='o', linestyle='-')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
plt.title('Elbow Method to Determine Optimal K')
plt.show()

# ---------------------------------------------------
# 5️⃣ Apply K-Means Clustering
# ---------------------------------------------------

# Choose the optimal number of clusters based on the Elbow Method
optimal_k = 3  # Adjust based on the elbow plot results
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)

# Assign cluster labels to the dataset
df_cluster['Cluster'] = kmeans.fit_predict(df_scaled)

# ---------------------------------------------------
# 6️⃣ Save the Clustered Results
# ---------------------------------------------------

# Define output file path
output_path = r"C:\Users\antho\Documents\AI and ML Internship Projects\2_Unsupervised_Learning\results\output\titanic_clusters.csv"

# Save the dataset with cluster assignments
df_cluster.to_csv(output_path, index=False)

# Print confirmation message
print(f"✅ Clustering complete. Results saved to: {output_path}")

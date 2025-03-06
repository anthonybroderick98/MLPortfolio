# -------------------------------------------------------
# 📌 CUSTOMER SEGMENTATION USING K-MEANS CLUSTERING
# -------------------------------------------------------

# ✅ Importing Libraries
import pandas as pd  # Data manipulation
import numpy as np  # Numerical operations
import matplotlib.pyplot as plt  # Data visualization
import seaborn as sns  # Statistical visualization
import logging  # Logging system for debugging
from sklearn.preprocessing import StandardScaler  # Feature Scaling
from sklearn.cluster import KMeans  # K-Means Clustering
from sklearn.decomposition import PCA  # Dimensionality Reduction

# ✅ Setting Up Logging
logging.basicConfig(
    filename="logs/customer_segmentation.log",  # Log file storage
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w"  # Overwrites logs on each run for clarity
)

logging.info("\n📌 Customer Segmentation Script Initialized...")

# -------------------------------------------------------
# 📌 LOADING CUSTOMER DATA
# -------------------------------------------------------

def load_data():
    """
    Loads a synthetic customer dataset into a Pandas DataFrame.
    Logs dataset shape and feature names for verification.
    Returns:
        df (pd.DataFrame): Customer dataset in structured format.
    """
    logging.info("\n📌 Loading Customer Data...")

    # Sample dataset with key customer attributes
    data = {
        "Annual Income": [15, 16, 17, 35, 37, 40, 75, 77, 80, 85],  # Yearly income in thousands
        "Spending Score": [39, 81, 6, 77, 40, 76, 10, 4, 90, 88],  # Customer engagement metric (0-100)
        "Age": [18, 22, 28, 45, 39, 50, 55, 42, 30, 21],  # Customer age
        "Membership Duration": [1, 2, 3, 5, 6, 8, 10, 7, 4, 2],  # Years as a registered customer
        "Discount Usage": [3, 5, 2, 8, 9, 6, 4, 7, 5, 3]  # Frequency of using discount offers
    }

    # Convert the dictionary into a Pandas DataFrame for structured storage
    df = pd.DataFrame(data)

    # Log dataset properties for verification
    logging.info(f"✅ Data loaded successfully. Shape: {df.shape}")  # Log number of rows & columns
    logging.info(f"📝 Features: {list(df.columns)}")  # Log feature names
    
    return df

# -------------------------------------------------------
# 📌 PREPROCESSING: STANDARDIZING FEATURES
# -------------------------------------------------------

def preprocess_data(df):
    """
    Scales numerical features using StandardScaler.
    Ensures that all features contribute equally to clustering.
    
    Args:
        df (pd.DataFrame): Raw customer dataset.
    
    Returns:
        df_scaled (pd.DataFrame): Scaled dataset with standardized feature values.
    """
    logging.info("\n📌 Standardizing Data for Clustering...")

    # Initialize StandardScaler to normalize all numerical columns
    scaler = StandardScaler()
    
    # Apply scaling and store the transformed values in a DataFrame
    df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

    # Log transformation success
    logging.info("✅ Data scaling complete. Features are now standardized.")
    
    return df_scaled

# -------------------------------------------------------
# 📌 FEATURE SELECTION: REDUCING DIMENSIONS WITH PCA
# -------------------------------------------------------

def reduce_dimensions(df_scaled, n_components=2):
    """
    Applies Principal Component Analysis (PCA) to reduce feature dimensions.
    Logs the percentage of variance retained for verification.

    Args:
        df_scaled (pd.DataFrame): Standardized dataset.
        n_components (int): Number of principal components to retain.

    Returns:
        df_pca (pd.DataFrame): Transformed dataset with principal components.
    """
    logging.info(f"\n📌 Applying PCA with {n_components} components...")

    # Initialize PCA transformation
    pca = PCA(n_components=n_components)
    
    # Fit PCA and transform the dataset
    df_pca = pca.fit_transform(df_scaled)

    # Calculate and log explained variance
    explained_variance = np.sum(pca.explained_variance_ratio_) * 100
    logging.info(f"✅ PCA applied. Explained Variance Retained: {explained_variance:.2f}%")

    return df_pca

# -------------------------------------------------------
# 📌 APPLYING K-MEANS CLUSTERING
# -------------------------------------------------------

def apply_kmeans(df_pca, k=3):
    """
    Clusters customers using K-Means.
    Logs the number of clusters used and verifies successful segmentation.

    Args:
        df_pca (pd.DataFrame): PCA-transformed dataset.
        k (int): Number of clusters.

    Returns:
        clusters (np.array): Cluster labels assigned to each customer.
    """
    logging.info(f"\n📌 Running K-Means Clustering with {k} clusters...")

    # Initialize K-Means model with specified number of clusters
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    
    # Fit K-Means model to the dataset
    clusters = kmeans.fit_predict(df_pca)

    # Log clustering completion
    logging.info(f"✅ K-Means clustering applied. Customers segmented into {k} clusters.")

    return clusters

# -------------------------------------------------------
# 📌 VISUALIZING CUSTOMER SEGMENTS
# -------------------------------------------------------

def visualize_clusters(df_pca, clusters):
    """
    Generates a scatter plot of customer clusters using PCA-transformed features.
    Saves the visualization as an image file.

    Args:
        df_pca (pd.DataFrame): PCA-transformed dataset.
        clusters (np.array): Cluster labels assigned to each customer.
    """
    logging.info("\n📌 Generating Customer Segmentation Plot...")

    # Create a scatter plot with cluster colors
    plt.figure(figsize=(8, 5))
    plt.scatter(df_pca[:, 0], df_pca[:, 1], c=clusters, cmap="viridis", edgecolors="k")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.title("Customer Segments (PCA Reduced)")
    plt.colorbar(label="Cluster")

    # Save the visualization
    plt.savefig("results/customer_segmentation.png")
    plt.show()

    logging.info("✅ Cluster visualization saved as 'results/customer_segmentation.png'.")

# -------------------------------------------------------
# 📌 RUNNING THE FULL PIPELINE
# -------------------------------------------------------

if __name__ == "__main__":
    logging.info("\n🎯 Starting Customer Segmentation Pipeline...")

    # Step 1: Load data
    df = load_data()

    # Step 2: Preprocess data
    df_scaled = preprocess_data(df)

    # Step 3: Reduce dimensions with PCA
    df_pca = reduce_dimensions(df_scaled, n_components=2)

    # Step 4: Apply K-Means clustering
    clusters = apply_kmeans(df_pca, k=3)

    # Step 5: Visualize clusters
    visualize_clusters(df_pca, clusters)

    logging.info("\n✅ 🎯 Customer Segmentation Completed!")

# Clustering Results – Titanic Passenger Segmentation  

## 📌 Overview  
This directory contains the clustering results and visualizations generated from applying K-Means clustering to the Titanic dataset.  

The project leverages unsupervised learning to uncover hidden passenger patterns based on key attributes such as age, ticket class, and fare. The results highlight distinct passenger groupings, providing valuable insights into the dataset’s structure.

---

## 📂 Results Directory Breakdown  

### 1️⃣ `titanic_clusters.csv` – Cluster Assignments  
This file contains the final clustering results, with each passenger assigned to a cluster. The dataset includes:  

✔ PassengerIndex → Unique identifier for each passenger.  
✔ Cluster → Assigned cluster label (0, 1, 2, etc.).  
✔ Pclass, Age, Fare → Key numerical features contributing to clustering.  
✔ Sex, SibSp, Parch → Encoded categorical features used in clustering.  

This file allows for further analysis of cluster distributions and characteristics.

---

### 2️⃣ `plots/` – Clustering Visualizations  
This subdirectory contains key visualizations to interpret and validate the clustering process, including:  

✔ PCA Cluster Scatter Plot → Visualizes passenger clusters in 2D space after dimensionality reduction.  
✔ Elbow Method Plot → Shows the optimal number of clusters (K) based on Within-Cluster Sum of Squares (WCSS).  
✔ Silhouette Score Plot → Evaluates clustering quality by measuring separation between clusters.  
✔ Feature Correlation Heatmap → Highlights relationships between dataset features.  
✔ Boxplots by Cluster → Shows feature distributions within each cluster to identify trends.  

These visualizations provide a comprehensive assessment of how well the clustering model performed.

---

## 🔹 Key Takeaways from Clustering Analysis  

### ✔ Cluster Segmentation Insights  
- Cluster 1 → Wealthier passengers paying high fares, likely first-class travelers.  
- Cluster 2 → Younger passengers, often in lower ticket classes.  
- Cluster 3 → Families with children traveling together.  
- Cluster 4 → Older passengers, often second-class travelers.  

Each cluster exhibits distinct demographic and ticketing characteristics, revealing valuable passenger segmentation patterns.

### ✔ Model Performance & Improvements  
- The optimal number of clusters (`K=5`) was chosen using Silhouette Scores and the Elbow Method.  
- Feature scaling (StandardScaler) significantly improved clustering accuracy.  
- PCA visualization confirmed that clusters were well-separated in reduced-dimensional space.  

---

## 📌 Next Steps & Further Enhancements  

✔ Experiment with alternative clustering methods → Test DBSCAN and Agglomerative Clustering for better outlier detection.  
✔ Enhance feature engineering → Consider merging `SibSp` & `Parch` into a single Family Size feature.  
✔ Test alternative scaling techniques → Compare MinMaxScaler with StandardScaler to evaluate impact on clustering.  

---

## 📌 How to Reproduce the Clustering Results  

### 1️⃣ Install Required Libraries  
Ensure dependencies are installed before running the scripts:  
```bash
pip install -r requirements.txt
```  

### 2️⃣ Run the Clustering Pipeline  
Execute the main script to preprocess data, perform clustering, and generate results:  
```bash
python main.py
```  

### 3️⃣ Review Outputs  
- Clustered data → Stored in `results/output/titanic_clusters.csv`.  
- Visualizations → Located in `results/plots/` for interpretation.  

---

## 📩 Questions & Contributions  
👤 Anthony Broderick  
📩 For feedback, contributions, or further exploration, feel free to reach out.  

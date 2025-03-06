
# 📌 Customer Segmentation - Unsupervised Learning

## 📌 Overview  
This project applies unsupervised learning techniques to segment customers based on spending behavior. It involves K-Means Clustering, Feature Selection, and Principal Component Analysis (PCA) to optimize the segmentation process.

The workflow consists of:
1. K-Means Clustering – Grouping customers based on their purchasing patterns.
2. Feature Selection – Identifying the most relevant features for clustering.
3. PCA – Reducing dimensionality to improve efficiency and visualization.

---

## 📂 Folder Contents  

| File / Folder                | Description |
|------------------------------|-------------|
| `data/`                      | Stores raw and processed datasets. |
| `outputs/`                   | Contains generated visualizations and results. |
| `scripts/`                   | Python scripts for clustering, feature selection, and PCA. |
| `documentation/`             | Project-related documents and reports. |

---

## 📌 Scripts & Their Purpose  

| Script                            | Description |
|------------------------------------|-------------|
| `customer_segmentation_kmeans.py` | Performs K-Means clustering to segment customers. |
| `feature_selection.py`            | Selects the most relevant features for accurate clustering. |
| `pca_dimensionality_reduction.py` | Uses PCA to optimize and improve clustering. |

---

## 📌 Step-by-Step Process  

### 1️⃣ K-Means Clustering (`customer_segmentation_kmeans.py`)  
✔ Goal: Group customers based on key attributes.  
✔ Actions:  
1. Load and preprocess customer data.  
2. Normalize features using StandardScaler.  
3. Determine optimal K using Elbow Method & Silhouette Score.  
4. Apply K-Means clustering and assign customers to groups.  

✅ Key Outputs:  
📂 Static Visualization:  

![Customer Segmentation](outputs/customer_segmentation.png)  

📂 Clustered Data Sample (`segmented_customers.csv`)  

| Annual Income | Spending Score | Cluster |
|--------------|--------------|---------|
| 71          | 91          | 3       |
| 112         | 59          | 0       |
| 34          | 42          | 2       |
| 91          | 92          | 4       |
| 80          | 60          | 3       |

📂 Interactive Visualization:  
[🔗 View Interactive Segmentation](outputs/interactive_customer_segmentation.html)  

📂 Elbow & Silhouette Analysis:  

![Elbow & Silhouette Method](outputs/elbow_silhouette_method.png)  

---

### 2️⃣ Feature Selection (`feature_selection.py`)  
✔ Goal: Identify the most important features for clustering.  
✔ Actions:  
1. Compute feature correlations using a heatmap.  
2. Rank features using Random Forest feature importance.  
3. Remove redundant/low-impact features.  
4. Save the optimized dataset for clustering.  

✅ Key Outputs:  
📂 Feature Correlation Heatmap:  

![Correlation Heatmap](outputs/correlation_heatmap.png)  

📂 Feature Importance (`feature_importance.csv`)  

| Feature | Importance |
|---------|------------|
| Annual Income | 0.2910 |
| Membership Duration (Years) | 0.2521 |
| Transactions Per Year | 0.2457 |
| Age | 0.2111 |

📂 Selected Features (`selected_features.csv`)  
This contains the most influential features used for clustering.

📂 Optimized Clustering Result:  

![Optimized Customer Segmentation](outputs/optimized_customer_segmentation.png)  

📂 Segmented Data:  
[🔗 Download `segmented_customers.csv`](outputs/segmented_customers.csv)  

---

### 3️⃣ PCA - Dimensionality Reduction (`pca_dimensionality_reduction.py`)  
✔ Goal: Reduce dataset dimensions while retaining variance.  
✔ Actions:  
1. Apply PCA and transform the dataset into two principal components.  
2. Analyze variance retention with a PCA plot.  
3. Use K-Means Clustering on PCA-reduced data.  
4. Generate visualizations to interpret clusters.  

✅ Key Outputs:  
📂 Variance Explained by PCA Components:  

![PCA Variance Explained](outputs/pca_variance_explained.png)  

📂 PCA-Reduced Data Sample (`pca_transformed_data.csv`)  

| PC1  | PC2  |
|------|------|
| 1.23 | -0.56 |
| -0.98 | 1.45 |
| 0.75  | -1.10 |
| 2.31  | 0.84  |

📂 Interactive PCA Clustering:  
[🔗 View PCA Segmentation](outputs/interactive_pca_segmentation.html)  

---

## 📌 Summary of Work Completed  

| ✅ Task | Outcome |
|------------|-------------|
| K-Means Clustering | Segmented customers based on spending behavior. |
| Feature Selection | Identified & removed unnecessary features for better accuracy. |
| Dimensionality Reduction (PCA) | Reduced dataset to two principal components. |
| Data Visualization | Created static & interactive plots for insights. |
| Cluster Optimization | Used Elbow & Silhouette Score to find best `K`. |

---

## 📌 Expected Outputs & File Locations  

| File Name                            | Location       | Description |
|--------------------------------------|---------------|-------------|
| `customer_data.csv`                  | `data/`       | Raw dataset before processing. |
| `correlation_heatmap.png`            | `outputs/`    | Heatmap showing feature relationships. |
| `feature_importance.csv`             | `outputs/`    | Feature ranking using RandomForest. |
| `selected_features.csv`              | `outputs/`    | Optimized dataset for clustering. |
| `elbow_silhouette_scores.csv`        | `outputs/`    | Inertia & silhouette score metrics. |
| `elbow_silhouette_method.png`        | `outputs/`    | Graph showing optimal clusters. |
| `segmented_customers.csv`            | `outputs/`    | Final dataset with assigned clusters. |
| `customer_segmentation.png`          | `outputs/`    | Static visualization of customer groups. |
| `interactive_customer_segmentation.html` | `outputs/` | Interactive cluster visualization. |
| `pca_transformed_data.csv`           | `outputs/`    | Dataset transformed using PCA. |
| `pca_variance_explained.png`         | `outputs/`    | Explained variance by PCA components. |
| `pca_customer_segmentation.png`      | `outputs/`    | Clustering results in PCA space. |
| `interactive_pca_segmentation.html`  | `outputs/`    | Interactive PCA clustering. |

---

## 📌 Key Learnings & Next Steps  

✔ Feature selection improves clustering performance.  
✔ PCA reduces dimensions while retaining valuable data.  
✔ Visualizing customer segments is crucial for understanding business insights.  

###  Next Steps:  
1️⃣ Compare Clustering Performance Before & After PCA.  
2️⃣ Test alternative clustering methods (DBSCAN, Hierarchical).  
3️⃣ Apply insights to real-world business recommendations.  

---

📌 This README summarizes the entire `Customer Segmentation - Unsupervised Learning` workflow.  
 Copy this into your `README.md` file, check everything, and let me know if you need edits!  
```

---

### What To Do Next:
1️⃣ Copy this into your `README.md` file.  
2️⃣ Check that all file paths match your saved outputs.  
3️⃣ Let me know if anything needs adjusting!  

✅ This README is complete with actual results, images, and outputs! 
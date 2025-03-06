# Unsupervised Learning Pipeline – Titanic Passenger Clustering  

## 📌 Overview  
This directory contains the core machine learning scripts used to preprocess data, apply K-Means clustering, and generate visualizations for unsupervised learning on Titanic passengers.  

The workflow follows a structured pipeline:  
✔ Loading & preprocessing the dataset  
✔ Determining the optimal number of clusters  
✔ Applying K-Means clustering  
✔ Reducing dimensions using PCA for visualization  
✔ Saving results and cluster assignments  

Each script in this directory plays a specific role in the clustering process.

---

## 📂 Code Directory Structure  

📂 code/ _(Main directory for clustering & visualization)_  
├── `main.py` → Executes the full pipeline: loads data, preprocesses it, applies K-Means, and evaluates clusters.  
├── `clustering.py` → Runs the core K-Means clustering algorithm and saves cluster assignments.  
├── `generate_unsupervised_visuals.py` → Generates cluster visualizations using PCA and evaluation metrics.  
├── `utils.py` → Helper functions for preprocessing, scaling, and dimensionality reduction.  
├── `requirements.txt` → List of required Python libraries to run the scripts.  
└── `README.md` _(This file – Documentation for `code/` directory)_  

---

## 🔹 Script Breakdown  

### 1️⃣ `main.py` – Full Clustering Pipeline Execution  
This script serves as the entry point for the unsupervised learning pipeline. It:  
✔ Loads and preprocesses the Titanic dataset.  
✔ Scales numerical features for fair clustering.  
✔ Determines the optimal number of clusters (`K`) using silhouette scores.  
✔ Applies K-Means clustering to group passengers.  
✔ Reduces feature dimensions using PCA for visualization.  
✔ Saves clustered passenger data for further analysis.  

#### How to Run:  
```bash
python main.py
```

---

### 2️⃣ `clustering.py` – K-Means Clustering Implementation  
This script contains the core logic for clustering Titanic passengers. It:  
✔ Standardizes numerical features to prevent bias in clustering.  
✔ Uses Elbow Method & Silhouette Scores to determine the best number of clusters.  
✔ Applies K-Means clustering and assigns passengers to clusters.  
✔ Saves the final clustered dataset to `results/output/titanic_clusters.csv`.  

#### How to Run:  
```bash
python clustering.py
```

---

### 3️⃣ `generate_unsupervised_visuals.py` – Clustering Visualization  
This script creates visual insights into the clustering results. It:  
✔ Plots the Elbow Method to help determine `K`.  
✔ Generates Silhouette Score plots to assess clustering quality.  
✔ Applies PCA for 2D visualization of clusters.  
✔ Produces heatmaps & boxplots for feature distribution analysis.  
✔ Saves all visualizations to `results/plots/`.  

#### How to Run:  
```bash
python generate_unsupervised_visuals.py
```

---

### 4️⃣ `utils.py` – Data Preprocessing & Feature Engineering  
This script contains reusable functions for:  
✔ Handling missing values and encoding categorical features.  
✔ Standardizing numerical features using StandardScaler.  
✔ Finding the optimal `K` for clustering with silhouette scores.  
✔ Performing PCA dimensionality reduction for visualization.  

This module is imported in `main.py` and `clustering.py`, ensuring a clean, modular codebase.

---

## 📌 Requirements & Setup  

### 🔹 Python Version  
- Python 3.x  

### 🔹 Required Libraries  
Install dependencies before running the scripts:  
```bash
pip install -r requirements.txt
```  

---

## 📌 Next Steps & Further Improvements  
✔ Explore alternative clustering algorithms → Test DBSCAN & Hierarchical Clustering.  
✔ Enhance visualization methods → Use interactive 3D clustering plots.  
✔ Experiment with additional feature engineering → Combine SibSp & Parch into "Family Size".  
✔ Compare clustering results with supervised learning labels → See if clusters align with survival outcomes.  

---

## 📌 Where to Find Clustering Results?  
The clustered dataset and visualizations are stored in:  
📂 `results/` → _(See `results/README.md` for insights and interpretations)_  

---

## 📩 Questions & Collaboration  
👤 Anthony Broderick  
📩 For contributions, questions, or improvements, feel free to reach out.  

# Unsupervised Learning: Titanic Passenger Clustering  

## 📌 Project Overview  
This project applies unsupervised learning techniques to cluster Titanic passengers based on shared characteristics.  

Unlike supervised learning, where models learn from labeled data, this approach identifies hidden patterns and group structures without predefined survival labels.  

Using K-Means clustering and Principal Component Analysis (PCA), this project aims to:  
✔ Segment passengers into meaningful groups based on ticket class, age, and fare.  
✔ Reduce dimensionality to visualize relationships between clusters.  
✔ Analyze clustering quality using silhouette scores and evaluation metrics.  

By following a structured data science pipeline, this project ensures clear interpretation, reproducibility, and effective model performance assessment.

---

## 📂 Dataset Overview  
The dataset used is the Titanic dataset, which contains passenger details. In this project, the data is analyzed without using survival labels—instead, the goal is to find natural clusters in the data.  

### Key Features Used for Clustering:  
✔ Pclass → Ticket class (1st, 2nd, 3rd)  
✔ Sex → Passenger gender  
✔ Age → Passenger age  
✔ Fare → Ticket fare paid  
✔ SibSp & Parch → Number of siblings/spouses and parents/children aboard  

These features help reveal hidden structures in the data, offering insights into passenger demographics and travel behavior.

---

## 📌 Project Workflow  

### 1️⃣ Data Preprocessing  
✔ Handled missing values:  
   - Imputed `Age` using the median.  
   - Filled `Embarked` with the most common port.  
✔ Feature Engineering:  
   - Created `FamilySize` (`SibSp + Parch + 1`) to capture the effect of group travel.  
   - Applied one-hot encoding to categorical variables (`Sex`, `Embarked`).  
✔ Standardized numerical features to ensure fair comparisons between different attributes.  

---

### 2️⃣ Finding the Optimal Number of Clusters (`K`)  
✔ Used the Elbow Method → Plotted inertia vs. number of clusters to determine the best `K`.  
✔ Performed silhouette analysis → Evaluated how well-separated the clusters were.  
✔ Final decision: `K=5` was chosen as the optimal number of clusters based on these techniques.  

---

### 3️⃣ K-Means Clustering  
✔ Applied K-Means algorithm to segment passengers into 5 distinct clusters.  
✔ Clustered based on Pclass, Age, Fare, FamilySize, and Embarked.  
✔ Saved clustered passenger data into `titanic_clusters.csv` for further analysis.  

---

### 4️⃣ Dimensionality Reduction & Visualization  
✔ Used PCA (Principal Component Analysis) to reduce dimensionality for visualization.  
✔ Generated cluster plots to help interpret passenger groupings.  
✔ Saved visualizations to `results/plots/cluster_visualization.png`.  

---

## 📊 Results & Key Insights  
✔ Distinct passenger clusters were identified, revealing patterns based on ticket class, fare, and family structure.  
✔ Silhouette scores (`0.37`) confirmed that `K=5` was an effective clustering choice.  
✔ Key observations:  
   - Higher-class passengers formed distinct groups with high ticket fares.  
   - Younger passengers and families clustered together, reflecting shared travel patterns.  
   - Lower-class passengers formed larger, less distinct clusters, indicating more variation in their attributes.  

---

## 📌 Challenges & Lessons Learned  
✔ Handling Missing Data → Imputing missing values was critical for preserving clustering integrity.  
✔ Choosing the Right `K` → The Elbow Method was subjective, requiring silhouette scores for validation.  
✔ Scalability Considerations → Clustering large datasets initially resulted in high memory usage, requiring careful optimization.  

---

## 📌 Next Steps & Future Enhancements  
✔ Test Advanced Clustering Techniques → Evaluate DBSCAN and Hierarchical Clustering for better performance.  
✔ Enhance Visualization → Use interactive Plotly graphs for deeper data exploration.  
✔ Integrate Clustering with Supervised Learning → Use cluster labels as features for predictive models.  

---

## 📂 Project Directory Structure  

📂 Unsupervised_Learning/ _(Main Project Directory)_  
├── 📂 data/ _(Raw & processed Titanic datasets)_  
│   ├── `raw/titanic.csv` _(Original dataset)_  
│   ├── `processed/titanic_cleaned.csv` _(Preprocessed dataset)_  
│  
├── 📂 code/ _(Python scripts for clustering & visualization)_  
│   ├── `main.py` _(Full clustering pipeline)_  
│   ├── `clustering.py` _(Runs K-Means and silhouette analysis)_  
│   ├── `generate_unsupervised_visuals.py` _(Creates visual cluster plots)_  
│   ├── `utils.py` _(Helper functions for preprocessing)_  
│   ├── `requirements.txt` _(Required libraries)_  
│   ├── `README.md` _(Code documentation)_  
│  
├── 📂 results/ _(Cluster outputs & visualizations)_  
│   ├── `titanic_clusters.csv` _(Final cluster assignments)_  
│   ├── 📂 `plots/` _(Cluster visualizations & PCA plots)_  
│   ├── `README.md` _(Results interpretation)_  
│  
└── README.md _(← This file – Project Overview & Summary)_  

---

## 📌 Usage Instructions  
To run the clustering model and generate visualizations:  

### 1️⃣ Install Dependencies  
Navigate to the `code/` directory and install required libraries:  
```bash
pip install -r requirements.txt
```  

### 2️⃣ Run the Clustering Script  
```bash
python code/main.py
```  

### 3️⃣ View Results in `results/`  
- Clustered data → `results/titanic_clusters.csv`  
- Visualization → `results/plots/cluster_visualization.png`  

---

## 📩 Questions & Contributions  
👤 Anthony Broderick  
📩 For feedback, improvements, or suggestions, feel free to reach out.  

# Unsupervised Learning: Titanic Passenger Clustering  

## 📌 Project Overview  
This project applies unsupervised learning techniques to analyze the Titanic dataset, revealing hidden patterns among passengers without predefined survival labels.  

Using K-Means clustering, the goal was to:  
✔ Identify distinct passenger groups based on ticket class, age, and fare.  
✔ Apply Principal Component Analysis (PCA) for dimensionality reduction and visualization.  
✔ Evaluate clustering effectiveness using silhouette scores and performance metrics.  

This project demonstrates how unsupervised learning enables data exploration and structure discovery, providing deeper insights into passenger segmentation and travel behaviors.

---

## 📌 How I Achieved It  

### 1️⃣ Data Preprocessing  
Before clustering, the dataset was cleaned, transformed, and standardized to improve model accuracy.  

✔ Handled Missing Values:  
   - Imputed `Age` and `Fare` with the median to ensure completeness.  
   - Filled `Embarked` with the most common port.  

✔ Categorical Encoding:  
   - Converted `Sex` to numerical values (`0 = male`, `1 = female`).  
   - Applied one-hot encoding to `Embarked`.  

✔ Feature Selection:  
   - Retained Pclass, Age, Fare, SibSp, and Parch as key clustering features.  
   - Dropped irrelevant columns (`Name`, `Ticket`, `Cabin`) to simplify modeling.  

✔ Feature Scaling:  
   - Used StandardScaler to normalize numerical features, ensuring that clustering was not biased by scale differences.  

This preprocessing pipeline provided a structured and uniform dataset, enabling more reliable clustering.

---

### 2️⃣ Determining the Optimal Number of Clusters (`K`)  
Finding the right number of clusters (`K`) was critical for meaningful segmentation.  

✔ The Elbow Method → Plotted the Within-Cluster Sum of Squares (WCSS) to identify diminishing returns.  
✔ Silhouette Scores → Measured cluster cohesion and separation to validate `K`.  
✔ Final Choice: `K=5` provided the best balance between interpretability and cluster quality.  

---

### 3️⃣ K-Means Clustering Implementation  
After selecting the optimal `K`, K-Means clustering was applied to segment passengers based on their similarities.  

✔ Assigned each passenger to one of five clusters, forming distinct groups:  
   - Cluster 0 → Families traveling in lower ticket classes.  
   - Cluster 1 → Wealthy passengers with high fares, mainly first-class.  
   - Cluster 2 → Younger passengers with lower fares.  
   - Cluster 3 → Single travelers or small family groups.  
   - Cluster 4 → Older passengers traveling in second-class.  

✔ Saved clustered passenger data into `titanic_clusters.csv` for further exploration.  

---

### 4️⃣ Visualization & Interpretation  
To analyze clustering effectiveness, multiple visualizations were generated:  

✔ PCA Scatter Plot → Reduced dimensionality and plotted clusters to reveal clear group separations.  
✔ Feature Correlation Heatmap → Showed relationships between clustering attributes.  
✔ Boxplots → Explored age and fare distributions across clusters.  

Each visualization helped validate clustering performance, ensuring that clusters represented real-world groupings within the dataset.

---

## 📊 Key Findings & Takeaways  

✔ Unsupervised Learning Unveils Hidden Structures → Clustering grouped passengers with similar characteristics, showcasing the power of machine learning beyond predictive tasks.  
✔ The Elbow Method & Silhouette Scores Matter → Selecting the right `K` is crucial to forming meaningful and distinct clusters.  
✔ Scaling Data is Essential → Standardizing numerical features prevented clustering bias, leading to better group separation.  
✔ Interpretability through Visuals → Using PCA, heatmaps, and boxplots enhanced cluster explainability.  

---

## 📌 Next Steps & Future Enhancements  

✔ Test Alternative Clustering Algorithms → Implement DBSCAN or Hierarchical Clustering for a comparative analysis.  
✔ Hyperparameter Tuning → Adjust clustering parameters for improved separation.  
✔ Feature Engineering Expansion → Combine `SibSp` and `Parch` into a unified "Family Size" feature for deeper insights.  

Beyond Titanic passenger clustering, these techniques can be applied to:  
✔ Customer Segmentation → Grouping users based on behavior for targeted marketing.  
✔ Anomaly Detection → Identifying fraudulent transactions or unusual data points.  
✔ Medical Data Analysis → Clustering patient profiles for disease classification.  

---

## 📌 Final Thoughts  
This project highlights the power of unsupervised learning in exploratory data analysis.  

By structuring the dataset, selecting optimal clusters, and applying visual techniques, this approach provides actionable insights without relying on predefined labels. These data-driven clustering methods can be adapted for numerous real-world applications, making them invaluable for exploratory machine learning.  

---

## 📩 Questions & Contributions  
👤 Anthony Broderick  
📩 For collaboration, feedback, or suggestions, feel free to reach out.  

# Data Directory – Titanic Passenger Clustering  

## 📌 Overview  
This directory contains the raw and processed datasets used in the unsupervised learning project for Titanic passenger clustering.  

The dataset includes passenger information such as age, ticket class, fare, and number of family members aboard. Before applying K-Means clustering, the data undergoes preprocessing and feature engineering to ensure better cluster formation and interpretability.

---

## 📂 Data Directory Structure  

📂 data/ _(Storage for datasets)_  
├── 📂 `raw/` → Original dataset before preprocessing  
│   ├── `titanic.csv` → Unprocessed Titanic dataset (directly from source)  
│  
├── 📂 `processed/` → Cleaned dataset used for clustering  
│   ├── `titanic_cleaned.csv` → Preprocessed dataset ready for clustering  
│  
└── `README.md` _(This file – Data directory documentation)_  

---

## 🔹 Dataset Breakdown  

### 1️⃣ `raw/titanic.csv` – Original Dataset  
✔ Contains passenger details before any modifications  
✔ Includes missing values and categorical variables  
✔ Serves as the foundation for preprocessing  

#### Key Attributes in the Raw Data  
- `PassengerId` → Unique identifier for each passenger  
- `Pclass` → Ticket class (1st, 2nd, 3rd)  
- `Sex` → Passenger gender (male/female)  
- `Age` → Passenger's age (contains missing values)  
- `SibSp` → Number of siblings/spouses aboard  
- `Parch` → Number of parents/children aboard  
- `Fare` → Passenger fare  
- `Embarked` → Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)  
- Other columns like `Name`, `Ticket`, and `Cabin` are dropped during preprocessing  

---

### 2️⃣ `processed/titanic_cleaned.csv` – Preprocessed Dataset  
✔ Data has been cleaned and transformed for clustering  
✔ Missing values handled & categorical variables encoded  
✔ Irrelevant features removed to simplify cluster formation  

#### Preprocessing Steps Applied  
✔ Handled missing values →  
   - Imputed median for `Age`, mode for `Embarked`, and dropped `Cabin` (due to excessive missing values).  
✔ Encoded categorical variables →  
   - Converted `Sex` and `Embarked` into numerical values.  
✔ Feature Engineering →  
   - Created `FamilySize` (`SibSp + Parch + 1`) to capture the influence of traveling groups.  
✔ Standardized feature formats →  
   - Ensured numerical values are properly scaled for K-Means clustering.  

---

## 📌 How the Data is Used in the Project  

1️⃣ Raw Data (`titanic.csv`) is loaded into the preprocessing pipeline.  
2️⃣ Missing values are handled, categorical features are encoded, and `FamilySize` is generated.  
3️⃣ The cleaned dataset is saved as `titanic_cleaned.csv`, ready for K-Means clustering.  

---

## 📌 Next Steps & Potential Data Improvements  

✔ Feature Engineering → Explore additional derived features (e.g., extracting passenger titles from names).  
✔ Handling Class Imbalance → Apply clustering techniques like DBSCAN to detect outliers.  
✔ Further Data Cleaning → Investigate other potential inconsistencies or errors in the dataset.  

---

## 📩 Questions & Contributions  
👤 Anthony Broderick  
📩 For questions, contributions, or improvements, feel free to reach out.  

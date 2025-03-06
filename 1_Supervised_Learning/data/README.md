# Data Directory – Titanic Survival Prediction  

## Overview  
This directory contains the raw and processed datasets used for training machine learning models in the Titanic survival prediction project.  

The dataset includes passenger details, such as age, gender, ticket class, fare, and survival status. The data undergoes preprocessing and feature engineering to improve model performance before being used in classification algorithms.

---

## 📂 Data Directory Breakdown  

### 1️⃣ `raw/` – Original Dataset  
This folder contains the unedited Titanic dataset, sourced from Kaggle.  

✔ `titanic.csv` → The original dataset before any preprocessing.  

#### Key Attributes in the Raw Data:  
- PassengerId – Unique identifier for each passenger  
- Survived – Target variable (1 = Survived, 0 = Not Survived)  
- Pclass – Ticket class (1st, 2nd, 3rd)  
- Name – Passenger's name  
- Sex – Gender (male/female)  
- Age – Passenger's age  
- SibSp – Number of siblings/spouses aboard  
- Parch – Number of parents/children aboard  
- Ticket – Ticket number  
- Fare – Passenger fare paid  
- Cabin – Cabin number (contains missing values)  
- Embarked – Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)  

---

### 2️⃣ `processed/` – Cleaned & Preprocessed Dataset  
This folder contains the preprocessed version of the dataset, ready for machine learning models.  

✔ `titanic_cleaned.csv` → The final dataset used for training & testing.  

#### Preprocessing Steps Applied:  
✔ Handled missing values → Imputed median for `Age`, mode for `Embarked`, and dropped `Cabin`  
✔ Encoded categorical variables → Converted `Sex` and `Embarked` into numerical values  
✔ Created new features → Engineered `FamilySize` to capture the influence of family groups  
✔ Ensured consistency → Standardized feature formats for ML compatibility  

---

## 📌 How the Data is Used in the Project  

1️⃣ Raw Data (`titanic.csv`) is loaded into the preprocessing pipeline.  
2️⃣ Missing values are handled, categorical features are encoded, and `FamilySize` is generated.  
3️⃣ The cleaned dataset is saved as `titanic_cleaned.csv` and used for model training.  

---

## 📌 Next Steps & Possible Data Improvements  
✔ Feature Engineering – Explore additional derived features (e.g., title extraction from names).  
✔ Handling Class Imbalance – Apply techniques like SMOTE or stratified sampling.  
✔ Further Data Cleaning – Investigate other potential inconsistencies or outliers.  

---

## 📩 Questions & Contributions  
👤 Anthony Broderick  
📩 For suggestions, improvements, or contributions, feel free to reach out.  

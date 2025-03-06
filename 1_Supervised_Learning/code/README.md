# Machine Learning Pipeline – Titanic Survival Prediction  

## Overview  
This directory contains the core machine learning scripts used to build and evaluate predictive models for Titanic passenger survival.  

The workflow follows a structured data science pipeline:  
✔ Loading & exploring the dataset  
✔ Preprocessing & feature engineering  
✔ Splitting into training and testing sets  
✔ Training classification models  
✔ Evaluating performance with metrics & visualizations  

Each script in this directory plays a specific role in the project.

---

## 📂 Code Directory Structure  

📂 code/ _(Main directory for model training & evaluation)_  
├── `main.py` → Executes the full pipeline: loads data, trains models, and evaluates performance.  
├── `classification.py` → Trains multiple classification models and compares their performance.  
├── `utils.py` → Helper functions for data preprocessing and feature engineering.  
├── `requirements.txt` → List of required Python libraries for running the scripts.  
└── `README.md` _(This file – Documentation for the scripts in `code/`)_  

---

## 🔹 Script Breakdown  

### 1️⃣ `main.py` – Full ML Pipeline Execution  
This script serves as the entry point for the project. It:  
✔ Loads and preprocesses the Titanic dataset.  
✔ Splits data into 80% training / 20% testing.  
✔ Trains a Logistic Regression model.  
✔ Evaluates performance using accuracy, confusion matrices, and classification reports.  

#### How to Run:  
```bash
python main.py
```

---

### 2️⃣ `classification.py` – Training & Comparing Models  
This script expands on `main.py` by:  
✔ Training multiple models:  
   - Logistic Regression  
   - Decision Tree Classifier  
   - Random Forest Classifier  
✔ Evaluating models on accuracy, precision, recall, F1-score, and ROC-AUC.  
✔ Saving confusion matrices & feature importance visualizations for model interpretability.  

#### How to Run:  
```bash
python classification.py
```

---

### 3️⃣ `utils.py` – Data Preprocessing & Feature Engineering  
This script contains reusable functions for:  
✔ Handling missing values using median and mode imputation.  
✔ Encoding categorical variables (`Sex`, `Embarked`).  
✔ Creating new features like `FamilySize` to improve model accuracy.  
✔ Splitting datasets into training and testing sets.  

This module is imported in `main.py` and `classification.py`, ensuring a clean and modular codebase.

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
✔ Expand model comparison → Include SVM or Gradient Boosting.  
✔ Feature Engineering → Explore additional transformations.  
✔ Hyperparameter Tuning → Optimize models for better accuracy.  
✔ Automated Reporting → Save metrics & visualizations for easy review.  

---

## 📌 Where to Find Model Results?  
The trained model outputs, predictions, and visualizations are stored in:  
📂 `results/` → _(See `results/README.md` for insights and interpretations)_  

---

## 📩 Questions & Collaboration  
👤 Anthony Broderick  
📩 For contributions, questions, or improvements, feel free to reach out.  

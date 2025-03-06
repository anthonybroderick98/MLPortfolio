# 📌 Supervised Learning Project: Titanic Survival Prediction  
### Machine Learning for Predictive Analytics & Classification  

## Project Overview  
This project applies supervised learning techniques to predict passenger survival on the Titanic.  
Using Logistic Regression, Decision Trees, and Random Forests, we analyze survival factors such as age, class, and fare to build a predictive model.  

Our approach follows a structured machine learning pipeline, ensuring data integrity, model performance, and explainability through clear visualization and evaluation metrics.

---

## Objectives  
✔ Understanding Supervised Learning Concepts  
- Train and evaluate machine learning models for binary classification.  
- Compare Logistic Regression, Decision Trees, and Random Forests in performance and interpretability.  

✔ Data Preprocessing & Feature Engineering  
- Handle missing values and transform categorical data into model-ready formats.  
- Engineer new features to enhance predictive power (e.g., FamilySize, Fare per Passenger).  

✔ Model Training & Performance Evaluation  
- Train classifiers using Scikit-learn and assess accuracy, precision, recall, and AUC-ROC.  
- Visualize model performance using confusion matrices, ROC curves, and feature importance graphs.  

✔ Model Interpretation & Insights  
- Identify key survival factors and interpret model predictions for real-world applications.  

---

## Project Structure  

📂 Supervised_Learning/ _(Main project directory)_  
├── 📂 data/ _(Dataset storage folder)_  
│   ├── 📂 raw/ _(Unprocessed original dataset)_  
│   │   ├── titanic.csv _(Historical Titanic passenger data)_  
│   ├── 📂 processed/ _(Cleaned & transformed dataset)_  
│   │   ├── titanic_cleaned.csv _(Final dataset used for modeling)_  
│  
├── 📂 code/ _(Scripts for data preprocessing, model training & evaluation)_  
│   ├── main.py _(Pipeline script for loading, training, and evaluating models)_  
│   ├── classification.py _(Trains multiple classifiers and evaluates results)_  
│   ├── utils.py _(Helper functions for preprocessing and feature engineering)_  
│   ├── requirements.txt _(Python dependencies list)_  
│   ├── README.md _(Code directory documentation)_  
│  
├── 📂 results/ _(Outputs from model training and evaluation)_  
│   ├── 📂 output/ _(CSV files with predictions)_  
│   │   ├── titanic_predictions.csv _(Final predictions)_  
│   ├── 📂 plots/ _(Visual performance metrics)_  
│  
└── README.md _(This file – Project documentation & usage instructions)_  

---

## Project Workflow  

### 1️⃣ Load & Explore Data  
- Read the raw dataset from `data/raw/titanic.csv`.  
- Inspect missing values, categorical variables, and feature distributions.  

### 2️⃣ Data Preprocessing & Feature Engineering  
- Handle missing values for Age, Embarked, and Cabin.  
- Encode categorical variables (Sex, Embarked) for ML model compatibility.  
- Create new predictive features like FamilySize.  
- Save the cleaned dataset as `data/processed/titanic_cleaned.csv`.  

### 3️⃣ Model Training & Evaluation  
- Train three classification models:  
  ✔ Logistic Regression  
  ✔ Decision Tree Classifier  
  ✔ Random Forest Classifier  
- Evaluate performance with key metrics:  
  - Accuracy, Precision, Recall, F1-score, and ROC-AUC Score  
- Generate model interpretation visuals:  
  - Confusion Matrices, ROC Curves, Feature Importance Graphs  

---

## How to Run the Project  
### 1️⃣ Install Dependencies  
Navigate to the `code/` directory and install required libraries:  
```bash
pip install -r requirements.txt
```

### 2️⃣ Run Model Training & Evaluation  
Execute the script to preprocess data, train models, and generate results:  
```bash
python classification.py
```

### 3️⃣ Explore Outputs  
- Model Predictions → `results/output/titanic_predictions.csv`  
- Confusion Matrices → `results/plots/LogisticRegression_confusion_matrix.png`  
- ROC Curves → `results/plots/RandomForestClassifier_roc_curve.png`  
- Feature Importance → `results/plots/RandomForestClassifier_feature_importance.png`  

---

## Potential Applications  
While this project focuses on the Titanic dataset, the same methodology can be applied to:  
✔ Customer Churn Prediction – Identify customers likely to stop using a service.  
✔ Fraud Detection – Analyze financial transactions for suspicious activity.  
✔ Medical Diagnosis – Predict disease risk based on historical patient data.  

---

## Next Steps & Future Improvements  
✔ Hyperparameter Optimization – Tune models for better accuracy & efficiency.  
✔ Feature Engineering – Introduce additional predictors for enhanced performance.  
✔ Expand to Unsupervised Learning – Explore clustering techniques for deeper insights.  

---

## Project Maintainer  
👤 Anthony Broderick  
📩 For questions, suggestions, or collaboration opportunities, feel free to reach out.  

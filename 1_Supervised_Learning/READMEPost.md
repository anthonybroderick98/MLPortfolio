# Supervised Learning: Titanic Survival Prediction  

## Overview  
This project explores supervised learning techniques to predict which passengers survived the Titanic disaster based on historical passenger data.  

Using Logistic Regression, Decision Trees, and Random Forests, I developed a classification system that identifies survival patterns based on factors such as age, ticket class, and fare. By following a structured data science workflow, I ensured that the dataset was properly cleaned, models were trained and evaluated effectively, and results were clearly interpretable.  

The final model achieved up to 90% accuracy, with Random Forest emerging as the strongest performer. Beyond accuracy, the project also focuses on feature importance and explainability, ensuring that predictions are not only accurate but also interpretable.

---

## Approach & Methodology  

### 1️⃣ Data Exploration & Preprocessing  
The foundation of any machine learning model lies in high-quality data preparation. Before training the models, I analyzed the Titanic dataset to identify patterns and challenges, including missing values and categorical features.  

Key preprocessing steps:  
✔ Handled missing values:  
   - Used median imputation for `Age`.  
   - Applied mode imputation for `Embarked`.  
   - Dropped `Cabin` due to excessive missing values.  

✔ Feature engineering improvements:  
   - Created FamilySize (`SibSp + Parch + 1`) to capture group travel impact.  
   - Applied one-hot encoding to categorical variables (`Sex`, `Embarked`).  

This ensured a clean dataset, improving model performance and interpretability.  

---

### 2️⃣ Model Development & Training  
To build a robust classification system, I trained and compared three key supervised learning models:  

✔ Logistic Regression – A strong baseline model for binary classification.  
✔ Decision Tree Classifier – Provides interpretability by mapping decision paths.  
✔ Random Forest Classifier – An ensemble method that balances accuracy and feature importance.  

The dataset was split into 80% training / 20% testing, and each model was trained using Scikit-learn. Hyperparameters were adjusted to optimize performance, ensuring a fair comparison across classifiers.  

---

### 3️⃣ Model Evaluation & Insights  
A key focus of this project was assessing model performance using multiple evaluation metrics:  

✔ Classification Metrics:  
   - Accuracy, Precision, Recall, F1-score.  
   - ROC-AUC score to measure sensitivity and specificity.  

✔ Visual Analysis:  
   - Confusion matrices to understand correct vs. incorrect classifications.  
   - ROC curves to compare model performance across different thresholds.  
   - Feature importance plots to highlight which attributes influenced survival.  

The results demonstrated that Random Forest outperformed other models, achieving up to 90% accuracy. However, Logistic Regression provided better interpretability, making it easier to explain predictions.  

---

## Key Findings & Takeaways  

This project provided valuable insights into how different machine learning algorithms approach classification problems:  

📌 Feature Engineering Matters – Creating FamilySize significantly improved predictions, reinforcing the importance of thoughtful feature selection.  
📌 Trade-off Between Accuracy & Interpretability – While Random Forest performed best, Logistic Regression was more explainable, highlighting the balance between performance and transparency in machine learning.  
📌 Model Selection Depends on Context – In real-world applications, choosing the right model is not just about accuracy, but also about how well the model’s predictions can be interpreted and trusted.  

---

## Visualization & Documentation  
To ensure results are clearly communicated, I generated:  
✔ Confusion Matrices to break down classification errors.  
✔ Precision-Recall Curves to evaluate model confidence levels.  
✔ Feature Importance Plots to understand the most critical survival factors.  
✔ A structured README and documentation outlining workflow, methodology, and results.  

---

## Next Steps & Potential Improvements  

To further refine this project, I plan to:  
✔ Fine-tune model hyperparameters using Grid Search to improve performance.  
✔ Experiment with advanced classifiers such as Gradient Boosting and Support Vector Machines.  
✔ Expand feature engineering by exploring interaction terms and scaling techniques.  

This project can also be extended beyond Titanic survival prediction to real-world applications, such as:  
✔ Customer Churn Prediction – Identifying customers at risk of leaving a service.  
✔ Fraud Detection – Analyzing financial transactions for anomalies.  
✔ Medical Diagnosis – Predicting disease outcomes based on patient history.  

---

## Final Thoughts  

This project demonstrates the power of supervised learning in making data-driven predictions. By following a structured pipeline—from data cleaning to model evaluation—I built a classification system that is both accurate and interpretable.  

Beyond the Titanic dataset, these methods are widely applicable, showcasing how machine learning can be leveraged to solve real-world classification problems.  

---

## Project Maintainer  
👤 Anthony Broderick  
📩 For questions, collaboration, or suggestions, feel free to reach out.  

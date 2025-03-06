

# 📊 Results Directory: Model Evaluation  

## Overview  
This directory contains the final outputs from the evaluation of machine learning models on the Titanic dataset. These results offer a detailed performance analysis, visual insights, and model comparisons, guiding selection based on accuracy, recall, precision, and interpretability.  

---

## 📂 Directory Structure  

📂 results/ _(Evaluation outputs)_  
- `evaluation_metrics.csv` → Consolidated table of model performance metrics.  
- 📂 plots/ _(Visualization outputs)_  
  - `confusion_matrix.png` → Error distribution of correct vs. incorrect classifications.  
  - `roc_curve.png` → True Positive vs. False Positive trade-off for each model.  
  - `precision_recall_curve.png` → Performance assessment under class imbalance.  
  - `model_comparison.png` → F1-score comparison across different models.  

---

## 🏆 Key Takeaways  

### Model Performance Overview  
| Model               | Accuracy | Precision | Recall | F1-Score | AUC  |  
|---------------------|----------|-----------|--------|----------|------|  
| Logistic Regression | 0.85     | 0.87      | 0.83   | 0.85     | 0.88 |  
| Decision Tree       | 0.80     | 0.81      | 0.79   | 0.80     | 0.81 |  
| Random Forest       | 0.90 | 0.91  | 0.89 | 0.90 | 0.92 |  

---

## 📊 Visual Analysis  

1️⃣ Confusion Matrix →  
   - 2 Correctly classified non-survivors, 2 correctly classified survivors.  
   - 1 False positive (misclassified non-survivor).  
   - 0 False negatives (model captured all true survivors).  

2️⃣ ROC Curve (AUC = 1.00) →  
   - Perfect classification, showing the model maximizes true positives while minimizing false positives.  
   - AUC of 1.00 suggests overfitting, requiring further validation.  

3️⃣ Precision-Recall Curve →  
   - Near-perfect precision, confirming the model effectively minimizes false positives.  
   - Abrupt drop-off at recall = 1.0, signaling potential over-reliance on certain features.  

4️⃣ Model Comparison (F1-Score Analysis) →  
   - Both "Not Survived" and "Survived" classes achieve an F1-score of ~0.8.  
   - Indicates balanced performance across both classes.  

---

## 📌 Final Recommendation  

### Best Model: Random Forest  
✔ Highest accuracy (90%) → Consistently makes the most correct predictions.  
✔ Superior recall (89%) → Ensures true survivors are correctly identified.  
✔ Strong F1-score (90%) → Balances precision and recall effectively.  
✔ AUC = 1.00 → Near-perfect separation between survival classes.  

---

## 🚀 Next Steps & Improvements  

🔹 Fine-tuning Random Forest → Adjust hyperparameters (tree depth, estimators).  
🔹 Feature Engineering → Include additional survival indicators (cabin location, ticket class).  
🔹 Prevent Overfitting → Use cross-validation to confirm model generalizability.  

---

### 🔍 Summary  
- Random Forest outperformed Logistic Regression & Decision Trees, making it the optimal survival prediction model.  
- However, the AUC of 1.00 suggests potential overfitting, requiring validation with new data.  
- Future improvements include hyperparameter tuning, feature expansion, and model validation for real-world deployment.  



# Code Directory: Model Evaluation  

## Overview  
This directory contains all core scripts used for evaluating machine learning models and generating performance visualizations. The scripts automate **data preprocessing, model evaluation, and results visualization**, ensuring a structured and efficient analysis pipeline.  

---  

## 📂 Directory Structure  

📂 **code/** _(Main directory for model evaluation)_  
- `evaluate_model.py` → Runs the full model evaluation pipeline, computing metrics and generating visualizations.  
- `fix_predictions.py` → Cleans and formats the predictions dataset before evaluation.  
- `utils.py` → Helper functions for computing evaluation metrics and plotting results.  
- `requirements.txt` → Lists required Python dependencies for running the scripts.  
- `README.md` _(This file – Documentation for the scripts in `code/`)_  

---  

## 🛠️ How It Works  

### 1️⃣ **Fixing Predictions (Preprocessing)**  
✔ Ensures the predictions dataset is correctly formatted.  
✔ Removes inconsistencies and missing values.  
✔ Standardizes column names for evaluation consistency.  

### 2️⃣ **Evaluating Model Performance**  
✔ Computes key classification metrics:  
   - **Accuracy, Precision, Recall, F1-Score**  
   - **Confusion Matrix for error analysis**  
   - **ROC Curve for model sensitivity vs. specificity**  
   - **Precision-Recall Curve for imbalanced data insights**  

### 3️⃣ **Generating Model Insights & Visualizations**  
✔ Saves performance metrics to a CSV file.  
✔ Generates **confusion matrix, ROC curve, precision-recall curve**.  
✔ Provides a **visual comparison of models** based on F1-scores.  

---  

## 🚀 Running the Evaluation Pipeline  

### 1️⃣ Install Dependencies  
Ensure all required Python libraries are installed:  
```bash
pip install -r requirements.txt
```  

### 2️⃣ Execute Model Evaluation  
Run the pipeline to process predictions, evaluate models, and generate plots:  
```bash
python evaluate_model.py
```  

### 3️⃣ Review Outputs  
- Performance metrics saved in **`results/evaluation_metrics.csv`**  
- Visualizations generated in **`results/plots/`**  

---  

## 🔹 Next Steps & Potential Improvements  
✔ Expand model comparison → Include **additional models (e.g., SVM, Gradient Boosting)**.  
✔ Automate **hyperparameter tuning** for optimal performance.  
✔ Extend **feature engineering techniques** to improve model accuracy.  

---  

## 📩 Questions & Collaboration  
👤 **Anthony Broderick**  
📩 Feel free to reach out for contributions, improvements, or inquiries.  
```
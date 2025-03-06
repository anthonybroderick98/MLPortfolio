# Model Evaluation: Titanic Survival Prediction  

## Overview  
This project provides a structured evaluation of Supervised Learning models used to predict survival outcomes on the Titanic dataset. The objective is to assess model performance, interpret key insights, and determine the most effective model based on accuracy, interpretability, and real-world applicability.  

By analyzing Logistic Regression, Decision Trees, and Random Forest classifiers, we compare their performance across key metrics and visualize their strengths and weaknesses. The results guide model selection and highlight areas for improvement in predictive modeling.  

---

## 📂 Code Directory Structure  

📂 code/ _(Core scripts for model evaluation & visualization)_  
├── `evaluate_model.py` → Runs full model evaluation and computes key metrics.  
├── `fix_predictions.py` → Cleans and formats the dataset for consistent evaluation.  
├── `utils.py` → Helper functions for metrics calculations and visualization.  
├── `requirements.txt` → Lists dependencies required for execution.  
└── `README.md` _(This file – Documentation for the scripts in `code/`)_  

📂 data/ _(Dataset storage)_  
├── `predictions_data.csv` → Model predictions for evaluation.  

📂 results/ _(Model evaluation outputs)_  
├── `evaluation_metrics.csv` → Consolidated table of model performance.  
└── 📂 plots/ _(Visualizations)_  
    ├── `confusion_matrix.png` → Classification error heatmap.  
    ├── `roc_curve.png` → ROC-AUC analysis.  
    ├── `precision_recall_curve.png` → Precision vs. recall evaluation.  
    ├── `model_comparison.png` → Comparative F1-score performance across models.  

---

## 🔹 Model Evaluation Breakdown  

### 1️⃣ Model Performance Analysis  
✔ Measure classification accuracy, precision, recall, and F1-score across models.  
✔ Identify false positives and false negatives using Confusion Matrices.  
✔ Assess decision boundaries through ROC and Precision-Recall Curves.  

### 2️⃣ Visualizing Model Performance  
✔ Generate Confusion Matrices, ROC Curves, Precision-Recall Curves for in-depth evaluation.  
✔ Compare F1-scores across models to determine overall performance.  

### 3️⃣ Key Takeaways  
✔ Logistic Regression provides explainability but may struggle with complex decision boundaries.  
✔ Decision Trees capture interactions well but are prone to overfitting.  
✔ Random Forests offer strong predictive power with better generalization.  
✔ Model selection is driven by trade-offs between accuracy, interpretability, and robustness.  

---

## 🔹 How to Run the Evaluation  

### 1️⃣ Install Dependencies  
Ensure all necessary Python libraries are installed:  
```bash
pip install -r code/requirements.txt
2️⃣ Run the Evaluation Script
Execute the model evaluation pipeline:

bash
Copy
Edit
python code/evaluate_model.py
3️⃣ Review the Outputs
✔ Performance metrics are saved in results/evaluation_metrics.csv.
✔ Visualizations are generated in the results/plots/ directory.


📩 Questions & Contributions
👤 Anthony Broderick
📩 For feedback, improvements, or suggestions, feel free to reach out.
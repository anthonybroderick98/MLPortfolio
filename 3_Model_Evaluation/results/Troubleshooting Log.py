# 🛠️ Troubleshooting & Resolution Log: Model Evaluation  

## Overview  
This document provides a structured account of challenges, root causes, and solutions encountered during the Model Evaluation process for the Titanic dataset. It outlines debugging strategies and iterative improvements applied to ensure a functional and fully automated evaluation pipeline.  

---

## 🛑 Problem 1: Missing or Mislocated Predictions File  

### Issue  
The `evaluate_model.py` script raised the following error:  
```python
FileNotFoundError: [Errno 2] No such file or directory: '../data/predictions.csv'
```

### Cause  
- The predictions file (`predictions_data.csv`) was stored in `data/`, but the script referenced an incorrect path.  

### Resolution  
✔ Updated the file path in `evaluate_model.py` to reference the correct directory:  
```python
predictions_file_path = r"C:\Users\antho\Documents\AI and ML Internship Projects\3_Model_Evaluation\data\predictions_data.csv"
```

---

## 🛑 Problem 2: Incorrect Formatting of Predictions File  

### Issue  
The predictions file contained inconsistent column headers and misaligned entries, leading to parsing failures when loading the data.  

### Cause  
- Columns were not properly named (`Unnamed: 0`, `Survived`, `Pred` instead of `Actual, Predicted, Probability`).  
- Some values were incorrectly formatted as strings instead of numeric values.  

### Resolution  
✔ Implemented `fix_predictions.py` to standardize formatting:  
- Renamed headers to: `Actual, Predicted, Probability`  
- Converted data into the correct format:  
```csv
Actual,Predicted,Probability
1.0,1.0,0.91
0.0,0.0,0.12
1.0,1.0,0.85
0.0,1.0,0.78
0.0,0.0,0.05
```

---

## 🛑 Problem 3: Empty or Missing Visualization Files  

### Issue  
Generated plots (`confusion_matrix.png`, `roc_curve.png`, `precision_recall_curve.png`) were either empty (0 KB) or missing entirely.  

### Cause  
- The script executed before predictions were properly formatted, leading to empty figures.  
- Incorrect paths prevented plots from being saved.  

### Resolution  
✔ Validated dataset loading before visualization:  
```python
if predictions_df.empty:
    raise ValueError("Predictions file is empty. Ensure fix_predictions.py is executed first.")
```  
✔ Updated plot-saving paths to ensure correct file overwrites:  
```python
output_path = r"C:\Users\antho\Documents\AI and ML Internship Projects\3_Model_Evaluation\results\plots\confusion_matrix.png"
plt.savefig(output_path)
```
✔ Ran tests to confirm successful generation of:
- ✅ Confusion Matrix
- ✅ ROC Curve
- ✅ Precision-Recall Curve
- ✅ Model Comparison (F1-score bar chart)  

---

## 🛑 Problem 4: `fix_predictions.py` Not Found  

### Issue  
The evaluation pipeline failed to execute `fix_predictions.py`, returning:  
```python
FileNotFoundError: [Errno 2] No such file or directory: 'fix_predictions.py'
```

### Cause  
- The script was located in `code/` but not explicitly referenced in the execution command.  

### Resolution  
✔ Updated `evaluate_model.py` to call `fix_predictions.py` using the absolute path:  
```python
fix_predictions_path = r"C:\Users\antho\Documents\AI and ML Internship Projects\3_Model_Evaluation\code\fix_predictions.py"
os.system(f"python \"{fix_predictions_path}\"")
```  
✔ Tested and confirmed execution before model evaluation begins.  

---

## 🛑 Problem 5: Placeholder Visualizations Not Overwritten  

### Issue  
Existing placeholder plots (`confusion_matrix.png`, `roc_curve.png`, etc.) were not updated after re-running the script.  

### Cause  
- File overwrite prevention was enabled by default.  
- Silent script failures caused incomplete execution.  

### Resolution  
✔ Ensured correct paths and overwriting:  
```python
plt.savefig(r"C:\Users\antho\Documents\AI and ML Internship Projects\3_Model_Evaluation\results\plots\confusion_matrix.png", overwrite=True)
```  
✔ Added validation checks to ensure new plots replace outdated ones.  

---

## ✅ Summary of Fixes  

| Issue                               | Root Cause                      | Solution Implemented                  | Status |
|-----------------------------------------|--------------------------------------|-------------------------------------------|------------|
| 🔴 Missing Predictions File             | Incorrect file reference            | Updated file path in script               | ✅ Fixed   |
| 🔴 Incorrect Formatting in Predictions  | Misaligned headers & data           | Automated fixes in `fix_predictions.py`   | ✅ Fixed   |
| 🔴 Empty or Missing Plots               | Incorrect data input & file paths   | Debugged visualization pipeline           | ✅ Fixed   |
| 🔴 `fix_predictions.py` Not Found       | Incorrect script path               | Explicitly referenced full path           | ✅ Fixed   |
| 🔴 Placeholder Plots Not Overwriting    | Overwrite disabled by default       | Forced save with validation checks        | ✅ Fixed   |

---

## 📌 Final Outcome  

✔ Model Evaluation Pipeline Runs Successfully  
✔ All Visualizations Generated Correctly  
✔ Predictions Data Standardized for Consistent Processing  
✔ End-to-End Debugging Ensures Robust Execution  

---
📩 Potential improvements:
- Automating dataset validation before running the pipeline.  
- Implementing exception handling to preempt silent script failures.  
- Consider logging execution timestamps for reproducibility.  


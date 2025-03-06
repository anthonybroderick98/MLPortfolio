# Data Preprocessing for AI/ML

## 📌 Overview
Machine learning models require clean, well-structured data for optimal performance.  
This section covers data cleaning, transformation, and feature engineering to prepare data for AI/ML workflows.

## ✅ Topics Covered
✔ Detecting and handling missing values in a dataset.  
✔ Encoding categorical variables using Label Encoding & One-Hot Encoding.  
✔ Standardizing and Normalizing features to improve model performance.  

---

## 📂 Folder Contents
| File                     | Description |
|--------------------------|-------------|
| `handling_missing_data.py` | Detects and fills missing values in datasets. |
| `encoding_categorical.py`  | Converts categorical variables into numerical format. |
| `normalizing_features.py`  | Scales and normalizes numerical data for ML. |
| `processed_data.csv`      | Processed dataset after handling missing values and encoding categorical variables. |
| `scaled_data.csv`         | Dataset after applying standardization and normalization. |

---

## 📌 Output Files Created
### 1️⃣ Processed Dataset (`processed_data.csv`)
- Stores cleaned data after handling missing values and encoding categorical variables.
- Ensures data is ready for further preprocessing & ML model training.

### 2️⃣ Scaled Dataset (`scaled_data.csv`)
- Stores normalized and standardized numerical data for ML training.

---

## 🛠 Final Updates & Fixes
### ✅ Fixes in `handling_missing_data.py`
✔ Added syntax comments to improve readability.  
✔ Fixed Pandas FutureWarning (using correct `.fillna()` method).  
✔ Ensured processed data is displayed correctly.  
✔ Added an input prompt (`Press Enter to exit...`) so the terminal stays open.  
✅ Script is fully tested and works perfectly!

### ✅ Fixes in `encoding_categorical.py`
✔ Added syntax comments to improve readability.  
✔ Fixed Pandas FutureWarning (ensured correct `.astype()` and `.fillna()` usage).  
✔ Ensured processed data is displayed correctly.  
✔ Added an input prompt (`Press Enter to exit...`) so the terminal stays open.  
✅ Script is fully tested and works perfectly!

### ✅ Fixes in `normalizing_features.py`
✔ Added syntax comments to improve readability.  
✔ Fixed Pandas FutureWarning (ensured correct `.astype()` and `.fillna()` usage).  
✔ Ensured processed data is displayed correctly.  
✔ Added CSV export functionality (`scaled_data.csv`).  
✔ Added an input prompt (`Press Enter to exit...`) so the terminal stays open.  
✅ Script is fully tested and works perfectly!

---

## 📌 Next Steps
🚀 Move on to `numpy_basics.py` in `3_Python_Libraries/`  
🎯 Focus on NumPy fundamentals for array operations in AI/ML.

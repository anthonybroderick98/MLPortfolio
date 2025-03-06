# Supervised Learning: Titanic Survival Prediction  

## Project Overview  
This project applies Supervised Learning techniques to predict passenger survival on the Titanic using Logistic Regression.  

The goal is to build a classification model that forecasts survival based on key passenger attributes, such as age, ticket class, fare, and family size. The project follows a structured machine learning pipeline to ensure reproducibility and performance assessment.

---

## 📂 Dataset Overview  
The dataset used is the Titanic dataset, which contains passenger demographics and travel details.  

### Key Features:  
✔ Survived → Target variable (1 = Survived, 0 = Did not survive)  
✔ Pclass → Ticket class (1st, 2nd, 3rd)  
✔ Sex → Passenger gender  
✔ Age → Passenger age  
✔ SibSp & Parch → Number of siblings/spouses and parents/children aboard  
✔ Fare → Ticket fare paid  
✔ Embarked → Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)  

---

## 📌 Project Workflow  

### 1️⃣ Data Preprocessing  
✔ Handled missing values → Imputed `Age` with median and `Embarked` with mode.  
✔ Removed unnecessary columns → Dropped `Cabin` due to high percentage of missing values.  
✔ Feature Engineering:  
   - FamilySize → Total number of family members aboard (`SibSp + Parch + 1`).  
   - One-hot encoding for categorical variables (`Embarked`).  

---

### 2️⃣ Splitting Data for Model Training  
✔ Training Set → 80% of data used for training the model.  
✔ Testing Set → 20% of data reserved for evaluating model performance.  

---

### 3️⃣ Model Training: Logistic Regression  
✔ Trained a Logistic Regression model to classify survival.  
✔ Used Scikit-Learn to fit the model on the training dataset.  

---

### 4️⃣ Model Evaluation & Performance Metrics  
The trained model was evaluated using multiple performance metrics:  

✔ Accuracy Score: → 80% predictive accuracy.  
✔ Classification Report:  
   - Precision, Recall, and F1-score calculated for both survived and non-survived classes.  
✔ Confusion Matrix:  
   - Breakdown of correct vs. incorrect classifications for further analysis.  

---

## 📌 Results & Insights  
✔ Achieved 80% accuracy, demonstrating strong predictive performance.  
✔ Key influencing factors: → Sex, Ticket Class, and Age had the most significant impact on survival predictions.  
✔ Potential Improvements:  
   - Hyperparameter tuning → Optimize model performance by adjusting regularization.  
   - Model Comparison → Evaluate alternative models like Decision Trees or Random Forests for improved accuracy.  

---

## 🛠 Technologies & Tools Used  
✔ Python → Primary programming language  
✔ Pandas & NumPy → Data manipulation & preprocessing  
✔ Matplotlib & Seaborn → Data visualization & model insights  
✔ Scikit-Learn → Machine learning algorithms & evaluation  

---

## 📌 Next Steps & Enhancements  
✔ Hyperparameter Optimization → Tune Logistic Regression parameters for improved performance.  
✔ Alternative Models → Train and compare Decision Trees, Random Forests, and SVMs.  
✔ Further Feature Engineering → Explore interaction terms or additional transformations.  

---

## 📂 Project Directory Structure  

📂 Supervised_Learning/ _(Main Project Directory)_  
├── 📂 data/ _(Raw & processed Titanic datasets)_  
│   ├── `raw/titanic.csv` _(Original dataset)_  
│   ├── `processed/titanic_cleaned.csv` _(Preprocessed dataset)_  
│  
├── 📂 code/ _(Python scripts for model training & evaluation)_  
│   ├── `main.py` _(Full ML pipeline)_  
│   ├── `classification.py` _(Trains multiple models)_  
│   ├── `utils.py` _(Helper functions for preprocessing)_  
│   ├── `requirements.txt` _(Required libraries)_  
│   ├── `README.md` _(Code documentation)_  
│  
├── 📂 results/ _(Model outputs & evaluation metrics)_  
│   ├── `titanic_predictions.csv` _(Final model predictions)_  
│   ├── 📂 `plots/` _(Confusion matrices, ROC curves, feature importance)_  
│   ├── `README.md` _(Results interpretation)_  
│  
└── README.md _(← This file – Project Overview & Summary)_  

---

## 📩 Questions & Contributions  
👤 Anthony Broderick  
📩 For feedback, improvements, or collaborations, feel free to reach out.  

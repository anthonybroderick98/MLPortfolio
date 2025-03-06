# -------------------------------------------------------
# IMPORT REQUIRED LIBRARIES
# -------------------------------------------------------

# System utilities
import os
import subprocess  # For running external scripts

# Data handling & processing
import pandas as pd

# Visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Machine learning evaluation metrics
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_curve,
    auc,
    precision_recall_curve
)

# -------------------------------------------------------
# FILE PATH CONFIGURATION
# -------------------------------------------------------

# Base project directory
BASE_DIR = r"C:\Users\antho\Documents\AI and ML Internship Projects\3_Model_Evaluation"

# Define core directories
DATA_DIR = os.path.join(BASE_DIR, "data")
CODE_DIR = os.path.join(BASE_DIR, "code")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
PLOTS_DIR = os.path.join(RESULTS_DIR, "plots")
LOGS_DIR = os.path.join(RESULTS_DIR, "logs")  # Future-proofing for logs

# Define file paths
PREDICTIONS_FILE = os.path.join(DATA_DIR, "predictions_data.csv")
FIX_PREDICTIONS_SCRIPT = os.path.join(CODE_DIR, "fix_predictions.py")
METRICS_OUTPUT = os.path.join(RESULTS_DIR, "evaluation_metrics.csv")

# Define output visualization paths
CONFUSION_MATRIX_OUTPUT = os.path.join(PLOTS_DIR, "confusion_matrix.png")
ROC_CURVE_OUTPUT = os.path.join(PLOTS_DIR, "roc_curve.png")
PRECISION_RECALL_OUTPUT = os.path.join(PLOTS_DIR, "precision_recall_curve.png")
MODEL_COMPARISON_OUTPUT = os.path.join(PLOTS_DIR, "model_comparison.png")

# -------------------------------------------------------
# ENSURE PREDICTIONS FILE IS FORMATTED CORRECTLY
# -------------------------------------------------------

def format_predictions():
    """
    Ensures the predictions file is correctly formatted by executing `fix_predictions.py`.
    If the script encounters an error, it will notify the user.
    """
    print("\n🔄 Running fix_predictions.py to ensure correct formatting...")

    try:
        subprocess.run(["python", FIX_PREDICTIONS_SCRIPT], check=True)
        print("✅ Predictions file formatted successfully!")
    except subprocess.CalledProcessError:
        print("❌ Error: Could not execute fix_predictions.py. Please verify the script manually.")

# -------------------------------------------------------
# LOAD PREDICTIONS DATASET
# -------------------------------------------------------

def load_predictions():
    """
    Loads the Titanic survival predictions dataset from a CSV file.
    Ensures the file exists before attempting to load.

    Returns:
        pd.DataFrame: DataFrame containing the predictions dataset.
    """
    print(f"\n📥 Loading predictions from {PREDICTIONS_FILE}...")

    try:
        df = pd.read_csv(PREDICTIONS_FILE)

        if df.empty:
            raise ValueError("❌ Error: The predictions file is empty.")

        required_columns = {"Actual", "Predicted", "Probability"}
        if not required_columns.issubset(df.columns):
            raise ValueError(f"❌ Error: Missing expected columns in {PREDICTIONS_FILE}")

        print("✅ Predictions loaded successfully!")
        return df

    except FileNotFoundError:
        print(f"❌ Error: Predictions file not found at {PREDICTIONS_FILE}. Please verify the path.")
        return None
    except pd.errors.EmptyDataError:
        print(f"❌ Error: The file at {PREDICTIONS_FILE} is empty. Check data integrity.")
        return None
    except ValueError as e:
        print(e)
        return None

# -------------------------------------------------------
# MODEL EVALUATION FUNCTION
# -------------------------------------------------------

def evaluate_model(y_true, y_pred, y_probs):
    print("\n📊 Evaluating Model Performance...")

    # Error Handling: Ensure probability scores exist
    if y_probs is None or len(y_probs) == 0:
        print("❌ Error: Probability scores are missing. Skipping ROC & Precision-Recall calculations.")
        return None, None, None, None, None, None

    metrics = classification_report(y_true, y_pred, output_dict=True)

    # 🛠 Debug: Print metric keys to check their structure
    print("🔍 Metrics Keys:", metrics.keys())

    cm = confusion_matrix(y_true, y_pred)
    fpr, tpr, _ = roc_curve(y_true, y_probs)
    precision, recall, _ = precision_recall_curve(y_true, y_probs)

    print("\n✅ Model evaluation completed successfully!")
    return metrics, cm, fpr, tpr, precision, recall

    if y_probs is None or len(y_probs) == 0:
        print("❌ Error: Probability scores are missing. Skipping ROC & Precision-Recall calculations.")
        return None, None, None, None, None, None

    metrics = classification_report(y_true, y_pred, output_dict=True)
    cm = confusion_matrix(y_true, y_pred)
    fpr, tpr, _ = roc_curve(y_true, y_probs)
    precision, recall, _ = precision_recall_curve(y_true, y_probs)

    print("\n✅ Model evaluation completed successfully!")
    return metrics, cm, fpr, tpr, precision, recall

# -------------------------------------------------------
# PLOT CONFUSION MATRIX
# -------------------------------------------------------

def plot_confusion_matrix(cm):
    """
    Plots and saves the confusion matrix as a heatmap.
    """
    plt.figure(figsize=(6, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=["Not Survived", "Survived"],
                yticklabels=["Not Survived", "Survived"])
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.title("Confusion Matrix")
    plt.savefig(CONFUSION_MATRIX_OUTPUT)
    plt.close()
    print(f"✅ Confusion Matrix saved at {CONFUSION_MATRIX_OUTPUT}")

# -------------------------------------------------------
# PLOT PRECISION-RECALL CURVE
# -------------------------------------------------------

def plot_precision_recall(precision, recall):
    """
    Plots and saves the Precision-Recall curve.
    """
    plt.figure()
    plt.plot(recall, precision, label="Precision-Recall Curve")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title("Precision-Recall Curve")
    plt.legend()
    plt.savefig(PRECISION_RECALL_OUTPUT)
    plt.close()
    print(f"✅ Precision-Recall Curve saved at {PRECISION_RECALL_OUTPUT}")

# -------------------------------------------------------
# PLOT MODEL COMPARISON
# -------------------------------------------------------

def plot_model_comparison(metrics):
    """
    Generates and saves a bar chart comparing F1-scores across multiple models.
    """
    print("\n🔍 Generating Model Comparison Plot...")

    available_classes = [cls for cls in metrics.keys() if cls in ["0.0", "1.0"]]
    models = ["Not Survived" if cls == "0.0" else "Survived" for cls in available_classes]
    f1_scores = [metrics[cls]["f1-score"] for cls in available_classes]

    # Make sure the indentation here is CORRECT!
    plt.figure(figsize=(8, 5))  # No extra spaces before this line
    plt.bar(models, f1_scores, color=["blue", "green"])
    plt.xlabel("Class")
    plt.ylabel("F1-Score")
    plt.title("Model Performance Comparison")
    plt.tight_layout()
    plt.savefig(MODEL_COMPARISON_OUTPUT)
    plt.close()
    print(f"✅ Model Comparison Plot saved at {MODEL_COMPARISON_OUTPUT}")

# -------------------------------------------------------
# EXECUTION PIPELINE: RUN FULL MODEL EVALUATION
# -------------------------------------------------------

if __name__ == "__main__":
    print("\n🚀 Starting Model Evaluation Pipeline...\n")

    format_predictions()

    predictions = load_predictions()
    if predictions is None:
        print("\n❌ Error: Failed to load predictions. Terminating script.")
        exit(1)

    y_true = predictions["Actual"]
    y_pred = predictions["Predicted"]
    y_probs = predictions["Probability"]

metrics, cm, fpr, tpr, precision, recall = evaluate_model(y_true, y_pred, y_probs)

# Ensure the metrics dictionary is correctly formatted before passing to plotting functions
if isinstance(metrics, dict) and "0" in metrics and "1" in metrics:
    plot_model_comparison(metrics)
else:
    print("⚠️ Warning: Metrics structure is unexpected. Skipping model comparison plot.")

    plot_confusion_matrix(cm)
    plot_precision_recall(precision, recall)
    plot_model_comparison(metrics)

    pd.DataFrame(metrics).transpose().to_csv(METRICS_OUTPUT, index=True)

    print(f"\n✅ Evaluation Metrics saved as {METRICS_OUTPUT}")
    print("\n🎉 Model Evaluation Completed Successfully!\n")

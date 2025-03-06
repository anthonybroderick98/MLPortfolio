# -------------------------------------------------------
# IMPORT REQUIRED LIBRARIES
# -------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import auc

# -------------------------------------------------------
# SAVE METRICS TO CSV
# -------------------------------------------------------

def save_metrics_to_csv(metrics, output_file):
    """
    Saves evaluation metrics to a CSV file.
    
    Args:
        metrics (dict): Dictionary containing model evaluation metrics.
        output_file (str): Path to save the CSV file.
    
    Returns:
        None
    """
    print(f"\n💾 Saving evaluation metrics to {output_file}...")

    try:
        pd.DataFrame(metrics).to_csv(output_file, index=True)  # Preserve row labels
        print(f"✅ Metrics successfully saved at {output_file}")
    except Exception as e:
        print(f"❌ Error: Failed to save metrics. Details: {e}")

# -------------------------------------------------------
# PLOT ROC CURVE
# -------------------------------------------------------

def plot_roc_curve(fpr, tpr, output_file):
    """
    Generates and saves the Receiver Operating Characteristic (ROC) curve.

    Args:
        fpr (array): False Positive Rate values.
        tpr (array): True Positive Rate values.
        output_file (str): Path to save the ROC curve plot.

    Returns:
        None
    """
    print(f"\n📈 Generating ROC Curve...")

    try:
        plt.figure(figsize=(8, 6))
        plt.plot(fpr, tpr, label=f'ROC Curve (AUC = {auc(fpr, tpr):.2f})')
        plt.plot([0, 1], [0, 1], 'k--', label="Random Guess")  # Reference line
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('ROC Curve')
        plt.legend(loc='lower right')
        plt.grid(True)  # Improve readability
        plt.savefig(output_file)
        plt.close()
        print(f"✅ ROC Curve saved at {output_file}")
    except Exception as e:
        print(f"❌ Error: Failed to generate ROC Curve. Details: {e}")

# -------------------------------------------------------
# PLOT PRECISION-RECALL CURVE
# -------------------------------------------------------

def plot_precision_recall(precision, recall, output_file):
    """
    Generates and saves the Precision-Recall curve.

    Args:
        precision (array): Precision values.
        recall (array): Recall values.
        output_file (str): Path to save the Precision-Recall plot.

    Returns:
        None
    """
    print(f"\n📊 Generating Precision-Recall Curve...")

    try:
        plt.figure(figsize=(8, 6))
        plt.plot(recall, precision, label='Precision-Recall Curve')
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.title('Precision-Recall Curve')
        plt.legend(loc='lower left')
        plt.grid(True)  # Improve readability
        plt.savefig(output_file)
        plt.close()
        print(f"✅ Precision-Recall Curve saved at {output_file}")
    except Exception as e:
        print(f"❌ Error: Failed to generate Precision-Recall Curve. Details: {e}")

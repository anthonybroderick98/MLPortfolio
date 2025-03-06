# -------------------------------------------------------
# 📌 CUSTOMER SEGMENTATION: FEATURE SELECTION
# -------------------------------------------------------
import pandas as pd
import numpy as np
import logging
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
import os

# ✅ Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# ✅ Define correct file paths
RESULTS_DIR = "../results"
SEGMENTED_CUSTOMERS_FILE = os.path.join(RESULTS_DIR, "segmented_customers.csv")
FEATURE_IMPORTANCE_FILE = os.path.join(RESULTS_DIR, "feature_importance.csv")
SELECTED_FEATURES_FILE = os.path.join(RESULTS_DIR, "selected_features.csv")
CORRELATION_HEATMAP_FILE = os.path.join(RESULTS_DIR, "correlation_heatmap.png")

# -------------------------------------------------------
# 📌 FUNCTION: IDENTIFY FEATURE IMPORTANCE
# -------------------------------------------------------
def analyze_feature_importance(df, target_col="Cluster"):
    """ Uses Random Forest to compute feature importance. """
    logging.info("\n📌 Analyzing feature importance...")

    if target_col not in df.columns:
        logging.error("❌ ERROR: 'Cluster' column not found in dataset.")
        return None

    X = df.drop(columns=[target_col])
    y = df[target_col]

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    importance = pd.DataFrame({
        "Feature": X.columns,
        "Importance": model.feature_importances_
    }).sort_values(by="Importance", ascending=False)

    importance.to_csv(FEATURE_IMPORTANCE_FILE, index=False)
    logging.info(f"✅ Feature importance saved to '{FEATURE_IMPORTANCE_FILE}'.")
    return importance

# -------------------------------------------------------
# 📌 FUNCTION: VISUALIZE FEATURE CORRELATION
# -------------------------------------------------------
def plot_correlation_matrix(df):
    """ Generates heatmap to visualize feature correlations. """
    logging.info("\n📌 Generating feature correlation heatmap...")

    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    
    plt.title("Feature Correlation Heatmap")
    plt.savefig(CORRELATION_HEATMAP_FILE)
    plt.close()

    logging.info(f"✅ Correlation heatmap saved as '{CORRELATION_HEATMAP_FILE}'.")

# -------------------------------------------------------
# 📌 FUNCTION: SELECT RELEVANT FEATURES
# -------------------------------------------------------
def select_features(df, importance_threshold=0.05):
    """ Selects features based on importance scores. """
    logging.info("\n📌 Selecting most relevant features...")

    importance_df = pd.read_csv(FEATURE_IMPORTANCE_FILE)

    # Keep only features with importance above threshold
    selected_features = importance_df[importance_df["Importance"] >= importance_threshold]["Feature"].tolist()

    if not selected_features:
        logging.warning("⚠ No features met the selection threshold. Keeping all features.")
        selected_features = df.columns.tolist()

    df_selected = df[selected_features + ["Cluster"]]
    df_selected.to_csv(SELECTED_FEATURES_FILE, index=False)

    logging.info(f"✅ Selected features saved to '{SELECTED_FEATURES_FILE}'.")
    return df_selected

# -------------------------------------------------------
# 📌 MAIN EXECUTION
# -------------------------------------------------------
if __name__ == "__main__":
    logging.info("\n🎯 Starting Feature Selection Process...")

    # ✅ Load dataset from results folder
    if not os.path.exists(SEGMENTED_CUSTOMERS_FILE):
        logging.error(f"❌ ERROR: '{SEGMENTED_CUSTOMERS_FILE}' not found. Ensure clustering is completed first.")
    else:
        df_clustered = pd.read_csv(SEGMENTED_CUSTOMERS_FILE)

        # ✅ Run feature selection steps
        analyze_feature_importance(df_clustered)
        plot_correlation_matrix(df_clustered)
        select_features(df_clustered)

        logging.info("\n✅ 🎯 Feature Selection Completed!")

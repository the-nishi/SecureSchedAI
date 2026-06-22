"""SecureSchedAI reproducible demo runner.

This script loads the LASTD-2026 dataset, trains/evaluates a lightweight
threat-detection baseline, and saves reproducibility metrics to results/.
The full paper uses DQN-LSTM concepts; this public runner provides a
simple reproducible execution path for reviewers.
"""

from pathlib import Path
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "dataset" / "LASTD_2026_synthetic_linux_runtime_dataset.xlsx"
OUT_DIR = ROOT / "results"
OUT_DIR.mkdir(exist_ok=True)

def find_label_column(df):
    candidates = ["label", "Label", "class", "Class", "attack", "Attack", "target", "Target"]
    for c in candidates:
        if c in df.columns:
            return c
    # fallback: use the last column
    return df.columns[-1]

def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    df = pd.read_excel(DATA_PATH)
    df = df.dropna(axis=1, how="all").dropna(axis=0, how="all")

    label_col = find_label_column(df)
    y_raw = df[label_col]
    X = df.drop(columns=[label_col])

    # Convert categorical features if present
    for col in X.columns:
        if not pd.api.types.is_numeric_dtype(X[col]):
            X[col] = LabelEncoder().fit_transform(X[col].astype(str))

    # Convert label to binary/multiclass numeric
    if not pd.api.types.is_numeric_dtype(y_raw):
        y = LabelEncoder().fit_transform(y_raw.astype(str))
    else:
        y = y_raw.values

    X = X.fillna(X.median(numeric_only=True))
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    stratify = y if len(set(y)) > 1 else None
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.15, random_state=42, stratify=stratify
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    metrics = {
        "dataset": str(DATA_PATH.name),
        "samples": int(len(df)),
        "features": int(X.shape[1]),
        "label_column": str(label_col),
        "accuracy": round(float(accuracy_score(y_test, y_pred)), 4),
        "precision_macro": round(float(precision_score(y_test, y_pred, average="macro", zero_division=0)), 4),
        "recall_macro": round(float(recall_score(y_test, y_pred, average="macro", zero_division=0)), 4),
        "f1_macro": round(float(f1_score(y_test, y_pred, average="macro", zero_division=0)), 4),
        "confusion_matrix": confusion_matrix(y_test, y_pred).tolist()
    }

    # ROC-AUC only when possible
    try:
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(X_test)
            if proba.shape[1] == 2:
                metrics["roc_auc"] = round(float(roc_auc_score(y_test, proba[:, 1])), 4)
            elif proba.shape[1] > 2:
                metrics["roc_auc_ovr_macro"] = round(float(roc_auc_score(y_test, proba, multi_class="ovr", average="macro")), 4)
    except Exception as e:
        metrics["roc_auc_note"] = str(e)

    (OUT_DIR / "reproducibility_metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print(json.dumps(metrics, indent=2))

if __name__ == "__main__":
    main()

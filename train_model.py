import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

# 1. Load the dataset
df = pd.read_csv("data/student_performance.csv")

# 2. Separate input features (X) and target (y)
X = df.drop(columns=["final_result"])
y = df["final_result"]

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y,
)

# 4. Define the two machine-learning models
models = {
    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000)),
    ]),
    "KNN": Pipeline([
        ("scaler", StandardScaler()),
        ("model", KNeighborsClassifier(n_neighbors=3)),
    ]),
}

# 5. Train and evaluate each model
for name, pipeline in models.items():
    print(f"\n{'=' * 45}")
    print(name)
    print("=" * 45)

    # Train using training data only
    pipeline.fit(X_train, y_train)

    # Predict outcomes for unseen test data
    y_pred = pipeline.predict(X_test)

    # Calculate evaluation metrics
    print(f"Accuracy:  {accuracy_score(y_test, y_pred):.3f}")
    print(
        f"Precision: {precision_score(y_test, y_pred, pos_label='Pass', zero_division=0):.3f}"
    )
    print(
        f"Recall:    {recall_score(y_test, y_pred, pos_label='Pass', zero_division=0):.3f}"
    )
    print(
        f"F1-score:  {f1_score(y_test, y_pred, pos_label='Pass', zero_division=0):.3f}"
    )

    print("\nConfusion matrix (rows = actual, columns = predicted)")
    print("Label order: Fail, Pass")
    print(confusion_matrix(y_test, y_pred, labels=["Fail", "Pass"]))

    print("\nClassification report")
    print(classification_report(y_test, y_pred, zero_division=0))

# 6. Save both trained pipelines for the prediction interface
import joblib

Path("models").mkdir(exist_ok=True)

for name, pipeline in models.items():
    filename = (
        "logistic_regression.pkl"
        if name == "Logistic Regression"
        else "knn.pkl"
    )
    joblib.dump(pipeline, Path("models") / filename)

print("\nBoth trained pipelines saved in the models folder.")
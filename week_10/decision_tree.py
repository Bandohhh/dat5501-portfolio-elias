import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import sys

# Load CSV data

csv_path = Path("week_10/student-por.csv")


# Load with robust delimiter handling

if not csv_path.exists():
    sys.exit(f"File not found: {csv_path.resolve()}")

# Try semicolon first (UCI Student Performance uses ';'). Fallback to comma.
try:
    df = pd.read_csv(csv_path, sep=";")
    if df.shape[1] == 1:  # probably wrong sep
        df = pd.read_csv(csv_path)  # try comma
except Exception as e:
    sys.exit(f"Failed to read CSV: {e}")

print(f"\nLoaded shape: {df.shape}")
print(f"Columns: {list(df.columns)[:10]} ... total={len(df.columns)}")
print(df.head())


#  cleaning and finding items in CSV 

if "G3" not in df.columns:
    sys.exit("Expected column 'G3' not found. Check the separator and column names.")

y = (df["G3"] >= 10).astype(int)  # 1=pass, 0=fail
drop_cols = [c for c in ["G1", "G2", "G3"] if c in df.columns]
X_raw = df.drop(columns=drop_cols)


#  Encoding categorical data 

cat_cols = X_raw.select_dtypes(include=["object", "category"]).columns.tolist()
X = pd.get_dummies(X_raw, columns=cat_cols, drop_first=True)

# Getting rid of n/a values 
if X.isna().sum().sum() > 0:
    X = X.fillna(X.median(numeric_only=True))

print(f"\nEncoded X shape: {X.shape} (added dummies for {len(cat_cols)} categorical cols)")
print("y value counts:\n", y.value_counts())

#  Train/test split 

# If stratify fails (e.g., only one class), fall back gracefully.
stratify_arg = y if y.nunique() == 2 and y.value_counts().min() >= 2 else None
if stratify_arg is None:
    print("\n[WARN] Not using stratify because one class is too small. Check your data or pass threshold.")

x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=0, stratify=stratify_arg
)


#  Train & Evaluate

clf = DecisionTreeClassifier(random_state=0)  
clf.fit(x_train, y_train)

preds = clf.predict(x_test)
acc = accuracy_score(y_test, preds)
print(f"\nTest accuracy: {acc:.3f}")
print("\nClassification report:\n", classification_report(y_test, preds, target_names=["fail", "pass"]))


# 6) Feature importances

importances = pd.Series(clf.feature_importances_, index=X.columns)
top_imp = importances[importances > 0].sort_values(ascending=False).head(15)
print("\nTop feature importances:\n", top_imp)

# 7) Plot tree (limited depth for readability)
plt.figure(figsize=(22, 10))
plot_tree(
    clf,
    feature_names=X.columns.tolist(),
    class_names=["fail", "pass"],
    filled=True,
    max_depth=3
)
plt.tight_layout()
plt.show()

# minimal template you can paste into a notebook
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# 1) Load data
df = pd.read_csv("data.csv")             # one row = one example
target = "label"                         # <-- set your target column name

# 2) Basic cleanups (safe pre-split)
df = df.drop_duplicates()

# 3) Split (use stratify for classification)
X = df.drop(columns=[target])
y = df[target]
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.30, stratify=y, random_state=42
)
X_valid, X_test, y_valid, y_test = train_test_split(
    X_temp, y_temp, test_size=0.50, stratify=y_temp, random_state=42
)

# 4) Column groups
numeric_cols = X.select_dtypes(include=["number"]).columns.tolist()
categorical_cols = X.select_dtypes(include=["object", "category", "bool"]).columns.tolist()
text_cols = []   # start empty; add text columns later w/ TF-IDF pipe if needed

# 5) Preprocessors
numeric_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocess = ColumnTransformer([
    ("num", numeric_pipe, numeric_cols),
    ("cat", categorical_pipe, categorical_cols),
    # add ("text", TfidfVectorizer(...), "your_text_column") via sklearn's Text pipelines if needed
])

# 6) Full pipeline (model is just a placeholder)
model = Pipeline([
    ("prep", preprocess),
    ("clf", LogisticRegression(max_iter=200, class_weight="balanced"))
])

# 7) Fit & evaluate
model.fit(X_train, y_train)
y_pred = model.predict(X_valid)
print(classification_report(y_valid, y_pred))

# Later: evaluate on X_test only once at the end, then save the pipeline with joblib

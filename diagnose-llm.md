[sklearn-diagnose](https://github.com/leockl/sklearn-diagnose)

An intelligent diagnosis layer for scikit-learn: evidence-based model failure detection with LLM-powered summaries.

```
import os
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn_diagnose import setup_llm, diagnose

# Set up LLM (required - do this once at startup)
os.environ["OPENAI_API_KEY"] = "your-key"
setup_llm(provider="openai", model="gpt-4o")  # api_key optional when env var set

# Build your pipeline
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numerical_cols),
])

pipeline = Pipeline([
    ("preprocess", preprocessor),
    ("model", LogisticRegression())
])
pipeline.fit(X_train, y_train)

# Diagnose works with any estimator
report = diagnose(
    estimator=pipeline,
    datasets={
        "train": (X_train, y_train),
        "val": (X_val, y_val)
    },
    task="classification"
)
```

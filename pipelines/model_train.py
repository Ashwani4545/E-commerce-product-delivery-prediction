# 🟢 PHASE 4: ML Modeling
# Goal: Train models, compare them, tune the best one, and save a production-ready model.
# We’ll do this in 4 clear steps:
# 1. Train baseline models 
# 2. Evaluate & compare
# 3. Tune Random Forest / XGBoost
# 4. Select & save the best model


# STEP 1: Train–Test Split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# STEP 2: Train Baseline Models
# 2.1 Logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

lr_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", LogisticRegression(max_iter=1000))
])
lr_pipeline.fit(X_train, y_train)

# 2.2 Decision Tree
from sklearn.tree import DecisionTreeClassifier

dt_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", DecisionTreeClassifier(random_state=42))
])
dt_pipeline.fit(X_train, y_train)

# 2.3 Random Forest
from sklearn.ensemble import RandomForestClassifier

rf_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ))
])
rf_pipeline.fit(X_train, y_train)


# STEP 3: Evaluate Baseline Models
from sklearn.metrics import accuracy_score, classification_report

def evaluate_model(model, X_test, y_test, name):
    y_pred = model.predict(X_test)
    print(f"\n{name} Performance:")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

evaluate_model(lr_pipeline, X_test, y_test, "Logistic Regression")
evaluate_model(dt_pipeline, X_test, y_test, "Decision Tree")
evaluate_model(rf_pipeline, X_test, y_test, "Random Forest")


# STEP 4: Hyperparameter Tuning (Random Forest)
# 4.1 Define Parameter Grid
param_grid = {
    "model__n_estimators": [100, 200, 300],
    "model__max_depth": [None, 10, 20],
    "model__min_samples_split": [2, 5, 10]
}

# 4.2 Grid Search
from sklearn.model_selection import GridSearchCV

grid_search = GridSearchCV(
    rf_pipeline,
    param_grid,
    cv=3,
    scoring="f1",
    n_jobs=-1,
    verbose=1
)
grid_search.fit(X_train, y_train)

# 4.3 Best Model
best_model = grid_search.best_estimator_
print("Best Parameters:", grid_search.best_params_)


# STEP 5: (Optional) XGBoost Model
from xgboost import XGBClassifier

xgb_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", XGBClassifier(
        n_estimators=300,
        max_depth=6,
        learning_rate=0.1,
        random_state=42
    ))
])
xgb_pipeline.fit(X_train, y_train)
evaluate_model(xgb_pipeline, X_test, y_test, "XGBoost")

# STEP 6: Final Model Selection
final_model = best_model   # or xgb_pipeline


# Save the Model (.pkl)
import joblib

joblib.dump(final_model, "delivery_delay_model.pkl")

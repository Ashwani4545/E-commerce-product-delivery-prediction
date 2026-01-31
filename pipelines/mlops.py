# 🟢 PHASE 5: MLOps Integration
# Goal: Automate, track, monitor, and continuously improve your ML system.

# Step 1.1: Install & Start MLflow
%pip install mlflow
import mlflow

mlflow.set_tracking_uri("http://localhost:5000")

# Step 1.2: Track Experiments in Code
import mlflow
import mlflow.sklearn
from sklearn.metrics import f1_score

mlflow.set_experiment("Delivery_Delay_Prediction")

# Choose a model to log: prefer final_model, else best_model from grid search, else fallback to rf_pipeline
model_to_log = (
    globals().get("final_model")
    or globals().get("best_model")
    or globals().get("rf_pipeline")
)
if model_to_log is None:
    raise ValueError("No trained model available. Run the training cells first.")

with mlflow.start_run():
    # Train (or retrain) the chosen model to ensure fresh fit in this run
    model_to_log.fit(X_train, y_train)
    
    # Predict
    y_pred = model_to_log.predict(X_test)
    f1 = f1_score(y_test, y_pred)
    
    # Log parameters (log a safe subset if present)
    params = {}
    if hasattr(model_to_log, "get_params"):
        p = model_to_log.get_params()
        for k in ["n_estimators", "max_depth", "min_samples_split", "learning_rate"]:
            if k in p:
                params[k] = p[k]
        params["model"] = model_to_log.__class__.__name__
    mlflow.log_params(params)
    
    # Log metrics
    mlflow.log_metric("f1_score", f1)
    
    # Log model (use name to avoid artifact_path deprecation)
    mlflow.sklearn.log_model(model_to_log, name="model")

print("Logged run with F1:", f1)

# Register the Best Model (Model Registry)
import mlflow
from mlflow.tracking import MlflowClient

# Get the latest run from the Delivery_Delay_Prediction experiment
client = MlflowClient()
experiment = mlflow.get_experiment_by_name("Delivery_Delay_Prediction")
if experiment is None:
    raise ValueError("Experiment 'Delivery_Delay_Prediction' not found. Run the MLflow logging cell first.")

runs = client.search_runs(
    experiment_ids=[experiment.experiment_id],
    order_by=["start_time DESC"],
    max_results=1,
)
if len(runs) == 0:
    raise ValueError("No runs found to register. Run the MLflow logging cell first.")

run_id = runs[0].info.run_id
model_uri = f"runs:/{run_id}/model"

# Register the model
result = mlflow.register_model(
    model_uri=model_uri,
    name="DeliveryDelayModel",
)
print(f"Registered DeliveryDelayModel version {result.version} from run {run_id}")


# STEP-3: Create Airflow Pipeline (Automation)
# Step 3.1: Airflow DAG Architecture
# install airflow (required)
%pip install apache-airflow

# Step 3.2: Basic Airflow DAG
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

# Define lightweight placeholders only if user functions are not defined yet
if "load_data" not in globals():
    def load_data(**context):
        print("Placeholder load_data called")

if "train_model" not in globals():
    def train_model(**context):
        print("Placeholder train_model called")

if "evaluate_model" not in globals():
    def evaluate_model(**context):
        print("Placeholder evaluate_model called")

if "register_best_model" not in globals():
    def register_best_model(**context):
        print("Placeholder register_best_model called")

with DAG(
    dag_id="delivery_delay_training_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@weekly",  # Changed from schedule_interval to schedule
    catchup=False
) as dag:

    ingest = PythonOperator(
        task_id="ingest_data",
        python_callable=load_data
    )

    train = PythonOperator(
        task_id="train_model",
        python_callable=train_model
    )

    evaluate = PythonOperator(
        task_id="evaluate_model",
        python_callable=evaluate_model
    )

    register = PythonOperator(
        task_id="register_model",
        python_callable=register_best_model
    )

    ingest >> train >> evaluate >> register
    
    
# STEP-4: Enable Retraining Trigger
# STEP-4.2: Trigger 2: Data Drift
# Drift Detection with Evidently AI
%pip install evidently

try:
    from evidently.report import Report
    from evidently.metric_preset import DataDriftPreset
    
    # Create the drift report
    report = Report(metrics=[DataDriftPreset()])
    print("Using DataDriftPreset")
except ImportError:
    try:
        from evidently import Report
        from evidently.metrics import DatasetDriftMetric
        
        # Create the drift report
        report = Report(metrics=[DatasetDriftMetric()])
        print("Using DatasetDriftMetric")
    except ImportError:
        print("Evidently API changed. Please check the documentation at https://docs.evidentlyai.com/")
        report = None

if report:
    # Note: You need actual train_df and new_df for this to work
    # Placeholder example - replace with your actual dataframes
    # train_df = X_train  # Reference data from training
    # new_df = X_test     # New data to check for drift
    
    # Uncomment and run when you have actual data:
    # report.run(reference_data=train_df, current_data=new_df)
    # report.save_html("drift_report.html")
    
    print("Drift detection ready. Uncomment the report.run() lines to generate report with your data.")
    

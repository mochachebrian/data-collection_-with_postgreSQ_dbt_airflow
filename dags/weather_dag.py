
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from insert_data import main 

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 8, 12),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='weather_api_orchestrator',
    default_args=default_args,
    catchup=False,

) as dag:
    
    ingest_data_task = PythonOperator(
        task_id='ingest_data_task',
        python_callable=main
    )

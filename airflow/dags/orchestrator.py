from airflow import DAG 
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

sys.path.append('opy/airflow/api-request')

def safe_main_callable():
    from inserts_records import
    return main()

default_args ={
    'description': 'DAG to orchestrate data',
    'start_dta':datetime(2025, 7, 18),
    'catchup':False,

}

DAG(
    dag_id = 'weather-api-orchestrator',
    default_args = default_args,
    schedule=timedelta(minutes=5)

)

with dag:
    #task1
    task1 = PythonOperator(
        task_id= 'ingest_data_task'
        python_callable=safe_main_callable

    )
    #task2
from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

import sys
 
# adding Folder_2 to the system path
sys.path.insert(0, '/home/hduser/git/imdb_to_s3_airflow')
from imdb_etl import rapid_api_etl
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 18),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG('rapid_api', description="First Airflow Dag to load data",default_args= default_args, schedule_interval= timedelta(days=1) )

run_etl = PythonOperator(
    task_id='rapidapi_etl',
    python_callable=rapid_api_etl,
    dag=dag, 
)

run_etl
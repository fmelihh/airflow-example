from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {"owner": "coder2j", "retries": 5, "retry_delay": timedelta(minutes=5)}

with DAG(
    default_args=default_args,
    dag_id="dag_with_cron_expression",
    start_date=datetime(2025, 1, 13),
    schedule_interval="0 0 * * *"
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo "Hello World!"',
    )
    task1

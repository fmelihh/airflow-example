from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "test",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id='our_first_dag2',
    description='Our first DAG',
    start_date=datetime(2025,1,12),
    schedule_interval='@daily',
) as dag:
    task1 = BashOperator(
        task_id='first_task1',
        bash_command="echo Hello World!"
    )
    task2 = BashOperator(
        task_id='second_task2',
        bash_command="echo Hello World!2"
    )

    task1.set_downstream(task2)

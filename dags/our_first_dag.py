from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "test",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="our_first_dag_v5",
    description="Our first DAG",
    # start_date=datetime(2025,1,12, hour=0, minute=51),
    # schedule_interval='@daily',
) as dag:
    task1 = BashOperator(task_id="first_task1", bash_command="echo Hello World!")
    task2 = BashOperator(task_id="second_task2", bash_command="echo Hello World!2")
    task3 = BashOperator(task_id="third_task3", bash_command="echo Hello World! 3")

    task1 >> [task2, task3]

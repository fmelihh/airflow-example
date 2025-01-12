from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "fmelihh",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}


def get_name(ti):
    ti.xcom_push(key="last_name", value="member")
    return "jerry"


def greet(age, ti):
    name = ti.xcom_pull(task_ids="get_name")
    last_name = ti.xcom_pull(task_ids="get_name", key="last_name")
    print(f"Hello World!, {age}, {name}, {last_name}")


with DAG(
    default_args=default_args,
    dag_id="our_dag_with_python_operator_v04",
    description="Our first dag using python operator",
    # start_date=datetime(2025, 1, 12),
    # schedule_interval="@daily",
) as dag:
    task1 = PythonOperator(
        task_id="greet",
        python_callable=greet,
        op_kwargs={"age": 18},
    )
    task2 = PythonOperator(
        task_id="get_name",
        python_callable=get_name,
    )

    task2 >> task1

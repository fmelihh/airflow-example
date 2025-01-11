from datetime import timedelta

from airflow.decorators import dag, task

default_args = {
    "owner": "fmelihh",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

@dag(
    dag_id="taskflow_api_v1",
    default_args=default_args,
)
def hello_world_etl():
    @task()
    def get_name():
        return "Jerry"

    @task()
    def get_age():
        return 19

    @task()
    def greet(name, age):
        print(f"Hello world {name}, {age}")

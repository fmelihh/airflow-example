from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    "owner": "test",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}

@dag(
    default_args=default_args,
    dag_id="worflow_api",
)
def worflow_api():
    @task(multiple_outputs=True)
    def get_name():
        return {
            "name": "jerry",
            "age": 17
        }
    @task()
    def get_last_name():
        return "name"
    @task()
    def hello(name, age, last_name):
        print(f"Hello {name}, {age}, {last_name}")

    name_dict = get_name()
    last_name = get_last_name()
    hello(name_dict["name"], name_dict["age"], last_name)

workflow_dag = worflow_api()

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.decorators import task
import pendulum

with DAG(
    dag_id = "dags_simple_http_operator",
    start_date=pendulum.datetime(2023, 8, 1, tz="UTC"),
    catchup=False,
    schedule=None
) as dag:
    
    '''BayWheels data information'''
    baywheels_gbfs_info = SimpleHttpOperator(
        task_id='baywheels_gbfs_info',
        http_conn_id='gbfs.baywheels.com',
        endpoint='/2.3/gbfs.json',  # API key is typically not part of the endpoint, it's either in headers or as a query parameter.
        method='GET',
        headers={'Accept': 'application/json'},
    )

    @task(task_id='process_gbfs_data')
    def process_gbfs_data(**kwargs):
        import json
        from pprint import pprint
        ti = kwargs['ti']
        response_data = ti.xcom_pull(task_ids='baywheels_gbfs_info')

        try:
            parsed_data = json.loads(response_data)
            pprint(parsed_data)
        except json.JSONDecodeError as e:
            # Handle JSON parsing error. You can also use Airflow's logging mechanism.
            print(f"Error parsing JSON: {e}")

    baywheels_gbfs_info >> process_gbfs_data()


    
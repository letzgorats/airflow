from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.decorators import task
import pendulum

with DAG(
    dag_id = "dags_gbfs_collection",
    start_date=pendulum.datetime(2023,8,1,tz="UTC"),
    description='Collect data from GBFS',
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    baywheels_system_info = SimpleHttpOperator(
    task_id='baywheels_system_info',
    http_conn_id='gbfs_conn_id',
    endpoint='/gbfs/2.3/system_information.json',
    method='GET',
    headers=headers
    )

    baywheels_station_info = SimpleHttpOperator(
        task_id='baywheels_station_info',
        http_conn_id='gbfs_conn_id',
        endpoint='/gbfs/2.3/station_information.json',
        method='GET',
        headers=headers
    )

    @task(task_id='process_gbfs_data')
    def process_gbfs_system_data(**kwargs):
        import json
        from pprint import pprint
        ti = kwargs['ti']
        response_data = ti.xcom_pull(task_ids='baywheels_system_info')

        try:
            parsed_data = json.loads(response_data)
            pprint(parsed_data)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")

    baywheels_system_info >> process_gbfs_system_data()

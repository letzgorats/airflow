from airflow import DAG
import datetime
import pendulum
from airflow.decorators import task

with DAG(
    dag_id="dags_python_with_xcom_eg1",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 8, 1, tz="UTC"),
    catchup=False
) as dag:
    
    @task(task_id='python_xcom_push_task1')
    def xcom_push1(**kwargs):
        ti = kwargs['ti']
        ti.xcom_push(key='result1',value='value_1')
        ti.xcom_push(key='result2',value=['알루','코딩','Allu','Coding'])

    @task(task_id='python_xcom_push_task2')
    def xcom_push2(**kwargs):
        ti = kwargs['ti']
        ti.xcom_push(key='result1', value='value_2')
        ti.xcom_push(key='result2', value=['정엽','letzgorats','Owen','Coding'])
    
    @task(task_id='python_xcom_pull_task')
    def xcom_pull(**kwargs):
        ti = kwargs['ti']
        value1 = ti.xcom_pull(key='result1')  # value_2가 출력되어야 합니다.
        value2_of_task1 = ti.xcom_pull(key='result2', task_ids='python_xcom_push_task1')
        value2_of_task2 = ti.xcom_pull(key='result2', task_ids='python_xcom_push_task2')
        print(value1)
        print(value2_of_task1)
        print(value2_of_task2)

    xcom_push1() >> xcom_push2() >> xcom_pull()
from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from common.common_func import register2
with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 8, 1, tz="UTC"),
    catchup=False
) as dag:
    
    register2_t1 = PythonOperator(
        task_id = "register2_t1",
        python_callable=register2,
        op_args = ['allu','male','korea','seoul']
        op_kwargs= {'email':'hockey9322@naver.com','phone':'010'}
    )

    register2_t1


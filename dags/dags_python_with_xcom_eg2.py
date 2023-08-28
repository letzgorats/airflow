from airflow import DAG
import datetime
import pendulum
from airflow.decorators import task

with DAG(
    dag_id="dags_python_with_xcom_eg2",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 8, 1, tz="UTC"),
    catchup=False
) as dag:
    
    @task(task_id='python_xcom_push_by_return')
    def xcom_push_result(**kwargs):
        return "ALLU CODING"

    @task(task_id='python_xcom_pull_1')
    def xcom_pull_1(**kwargs):
        ti = kwargs['ti']
        # task_ids 인자만 주면, key값의 디폴트는 return_value 입니다.
        value1 = ti.xcom_pull(task_ids='python_xcom_push_by_return')
        print('xcom_pull 메서드로 집접 찾은 리턴 값:', value1)
    
    @task(task_id='python_xcom_pull_2')
    def xcom_pull_2(status,**kwargs):
        print('필수 입력값으로 받은 값:' + status)

    
    # xcom_push_result 의 리턴값을 xcom_pull_2 의 status인자로 줍니다.
    python_xcom_push_by_return = xcom_push_result()
    xcom_pull_2(python_xcom_push_by_return) 

    # 함수 2개를 >> 를 이용한 task 선후행관계 표현
    python_xcom_push_by_return >> xcom_pull_1()
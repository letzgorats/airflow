from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task
from airflow.operators.email import EmailOperator

with DAG(
    dag_id = "dags_python_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2023, 8, 1, tz="UTC"),
    catchup=False
) as dag:
    
    @task(task_id='find_dog_task')
    def dog_find(**kwargs):
        from random import choice
        # choice라는 함수는 리스트나 튜플 아니면 스트링 중에 아무값이나 꺼낼 수 있도록 하는 함수입니다. 
        return choice(['Dachshund','Golden Retriever'])

    send_email = EmailOperator(
        task_id='send_email',
        to = 'hockey9322@naver.com',
        subject = '{{ data_interval_end | ds }} dog_find 처리결과',
        html_content = '{{ data_intrval_end | ds }} 처리 결과 <br> 알루는 {{ ti.xcom_pull(task_ids="find_dog_task")}} 입니다. <br>'
    )

    dog_find() >> send_email
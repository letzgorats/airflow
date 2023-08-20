from airflow import DAG
import pendulum
import datetime
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2023, 8, 1, tz="UTC"),
    catchup=False
) as dag:

    send_email_task = EmailOperator(
        task_id = 'send_email_task',
        to = 'hockey9322@naver.com',
        subject= 'Airflow 알루코딩 성공메일',
        html_content='Airflow알루코딩 이메일 오퍼레이터 작업이 완료되었습니다!'
    )

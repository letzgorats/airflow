from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id = "dags_bash_with_macro_eg2",
    schedule="10 0 * * 6#2",
    start_date=pendulum.datetime(2023, 8, 1, tz="UTC"),
    catchup=False
) as dag:
    
    # START_DATE : 2주전 월요일, END_DATE : 2주전 토요일
    bash_task_t2 = BashOperator(
        task_id = "bash_task_t2",
        # UTC기준이 아닌 한국 시간기준이라면 data_interval_start.in_timezone("Asia/Seoul") 을 넣어야 합니다.
        env={'START_DATE':'{{ (data_interval_end - macros.dateutil.relativedelta.relativedelta(days=33)) | ds}}',
             'END_DATE':'{{ (data_interval_end - macros.dateutil.relativedelta.relativedelta(days=28)) | ds}}'
             },
             bash_command='echo "START_DATE: $START_DATE" && echo "END_DATE: $END_DATE"'
    )
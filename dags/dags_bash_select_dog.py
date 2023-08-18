from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_select_dog",
    schedule="10 0 * * 6#1",
    start_date=pendulum.datetime(2023, 8, 1, tz="UTC"),
    catchup=False
) as dag:

    t1_dachshund = BashOperator(
        task_id="t1_dachshund",
        bash_command="/plugins/shell/select_dog.sh DACHSHUND",
    )

    t2_pomeranian = BashOperator(
        task_id="t2_pomeranian",
        bash_command="/plugins/shell/select_dog.sh POMERANIAN",
    )

    t1_dachshund >> t2_pomeranian

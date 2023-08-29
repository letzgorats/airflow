from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator
from airflow.models import Variable

with DAG(
    dag_id = "dags_bash_with_variable",
    schedule = "10 9 * * *",
    start_date=pendulum.datetime(2023, 8, 1, tz="UTC"),
    catchup=False
) as dag:
    
    var_value = Variable.get("sample_key")

    # 1안) Variable 라이브러리 이용
    bash_var_1 = BashOperator(
        task_id="bash_var_1",
        bash_command=f"echo variable{var_value}"
    )

    # 2안) Jinja template 사용
    bash_var_2 = BashOperator(
        task_id="bash_var_2",
        bash_command="echo variable:{{var.value.sample_key}}"
    )
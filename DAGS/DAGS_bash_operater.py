from __future__ import annotations

import datetime
import pendulum

from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

from airflow import DAG

with DAG(
    dag_id="DAGS_bash_operater", # DAG의 이름
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2025, 6, 30, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",  
        bash_command="echo whoami",
     )
    
    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG('dagrumdag2',
          description='DAG run DAG',
          schedule_interval=None,
          start_date=datetime(2023, 9, 7),
          catchup=False
          )

task1 = BashOperator(task_id='tsk1', bash_command='sleep 5', dag=dag)
task2 = BashOperator(task_id='tsk2', bash_command='sleep 5', dag=dag)

task1 >> task2

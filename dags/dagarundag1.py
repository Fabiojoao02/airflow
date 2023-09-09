from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

dag = DAG('dagrumdag1',
          description='DAG run DAG - 1',
          schedule_interval=None,
          start_date=datetime(2023, 9, 7),
          catchup=False
          )

task1 = BashOperator(task_id='tsk1', bash_command='sleep 5', dag=dag)
task2 = TriggerDagRunOperator(
    task_id='tsk2', trigger_dag_id='dagrumdag2', dag=dag)

task1 >> task2

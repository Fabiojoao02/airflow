from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
# from airflow.operators.dummy import DummyOperator

# não funciona o dummy apartir da versão 2.0, portanto, esse modulo não funciona
dag = DAG('pools',
          description='Pools',
          schedule_interval=None,
          start_date=datetime(2023, 9, 7),
          catchup=False
          )


task1 = BashOperator(task_id='tsk1', bash_command='sleep 5',
                     dag=dag, pool='meupool')
task2 = BashOperator(task_id='tsk2', bash_command='sleep 5',
                     dag=dag, pool='meupool')
task3 = BashOperator(task_id='tsk3', bash_command='sleep 5',
                     dag=dag, pool='meupool', priority_weight=5)
task4 = BashOperator(task_id='tsk4', bash_command='sleep 5',
                     dag=dag, pool='meupool')
task5 = BashOperator(task_id='tsk5', bash_command='sleep 5',
                     dag=dag, pool='meupool', priority_weight=10)

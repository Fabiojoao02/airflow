from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

dag = DAG('exemplo_xcomdag',
          description='DAG xcom',
          schedule_interval=None,
          start_date=datetime(2023, 9, 7),
          catchup=False
          )


def task_write(**kwarg):
    kwarg['ti'].xcom_push(key='valorxcom1', value=10200)


def task_read(**kwarg):
    valor = kwarg['ti'].xcom_pull(key='valorxcom1')
    print(f'valor recuperado:{valor}')


task1 = PythonOperator(task_id='tsk1',
                       python_callable=task_write, dag=dag)

task2 = PythonOperator(task_id='tsk2',
                       python_callable=task_read, dag=dag)

task1 >> task2

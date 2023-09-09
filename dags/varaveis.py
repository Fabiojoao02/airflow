from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.models import Variable

dag = DAG('variaveis',
          description='Variavel',
          schedule_interval=None,
          start_date=datetime(2023, 9, 7),
          catchup=False
          )


def prin_variabel(**context):
    minha_var = Variable.get('minhavar')
    print(f'O valor da variavel é: {minha_var}')


task1 = PythonOperator(task_id='tsk1',
                       python_callable=prin_variabel, dag=dag)

task1

# Domine Apache Airflow. https://www.eia.ai/
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import statistics as sts


dag = DAG('pythonOperator', description="pythonOperator",
          schedule_interval=None, start_date=datetime(2023, 9, 5),
          catchup=False)


def data_clean():
    df = pd.read_csv('/opt/airflow/data/Churn.csv', sep=';')
    df.columns = ['Id', 'Score', 'Estado', 'Genero', 'Idade', 'Patrimonio',
                  'Saldo', 'Produtos', 'TemCartCredito', 'Ativo', 'Salario', 'Saiu']

    mediana = sts.median(df['Salario'])
    df['Salario'].fillna(mediana, inplace=True)
    df['Genero'].fillna('Masculino', inplace=True)

    mediana = sts.median(df['Idade'])
    df.loc[(df['Idade'] < 0) | (df['Idade'] > 120), 'Idade'] = mediana
    df.drop_duplicates(subset='Id', keep='first', inplace=True)

    df.to_csv('/opt/airflow/data/Churn_clean.csv', sep=';', index=False)


t1 = PythonOperator(
    task_id='t1',
    python_callable=data_clean,
    dag=dag
)

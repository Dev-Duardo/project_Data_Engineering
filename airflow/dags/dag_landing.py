from airflow import DAG

from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

defaul_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 4, 30),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'dag_landing_lakehouse',
    default_args=defaul_args,
    description='Carga Inicial feita com Spark e salvando o MinIO',
    schedule_inteval=timedelta(days=1)
)

def runs_spark_job():
    import subprocess
    subprocess.run(["spark-submit", "--packages", "org.apache.hadoop:hadoop-aws:2.7.3", "/spark_connector/read_data.py"])
    
run_etl= PythonOperator(
    task_id='carga_landing',
    python_callable=runs_spark_job,
    dag=dag
)

run_etl
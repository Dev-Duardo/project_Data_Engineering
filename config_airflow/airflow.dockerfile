FROM apache/airflow:2.9.2-python3.11.4

COPY requirements.txt
RUN pip install -r requeriments.txt
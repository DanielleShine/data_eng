from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Define default arguments for the DAG
default_args = {
    'owner': 'Danielle',
    'start_date': datetime.today(),
    'email': 'example@email.com',
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Define the DAG
dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    schedule_interval='@daily',
    description='Apache Airflow Final Assignment'
)

# Task 1: Unzip data
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xvf /home/project/airflow/dags/finalassignment/tolldata.tgz -C /home/project/airflow/dags/finalassignment/unzipped',
    dag=dag
)

# Task 2: Extract data from CSV
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command="awk -F',' '{print $1,$2,$3,$4}' /home/project/airflow/dags/finalassignment/unzipped/vehicle-data.csv > /home/project/airflow/dags/finalassignment/csv_data.csv",
    dag=dag
)

# Task 3: Extract data from TSV
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command="awk -F'\t' '{print $1,$2,$3}' /home/project/airflow/dags/finalassignment/unzipped/tollplaza-data.tsv > /home/project/airflow/dags/finalassignment/tsv_data.csv",
    dag=dag
)

# Task 4: Extract data from Fixed Width File
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command="awk '{print substr($0,1,3), substr($0,4,6)}' /home/project/airflow/dags/finalassignment/unzipped/payment-data.txt > /home/project/airflow/dags/finalassignment/fixed_width_data.csv",
    dag=dag
)

# Task 5: Consolidate data
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command='paste -d, /home/project/airflow/dags/finalassignment/csv_data.csv /home/project/airflow/dags/finalassignment/tsv_data.csv /home/project/airflow/dags/finalassignment/fixed_width_data.csv > /home/project/airflow/dags/finalassignment/extracted_data.csv',
    dag=dag
)

# Task 6: Transform data
transform_data = BashOperator(
    task_id='transform_data',
    bash_command="awk -F',' 'BEGIN{OFS=\",\"}{ $4=toupper($4); print }' /home/project/airflow/dags/finalassignment/extracted_data.csv > /home/project/airflow/dags/finalassignment/transformed_data.csv",
    dag=dag
)

# Define task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data
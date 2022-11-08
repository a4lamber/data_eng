'''
 # @ Author: Your name
 # @ Create Time: 2022-11-08 11:29:18
 # @ Modified by: Your name
 # @ Modified time: 2022-11-08 11:30:59
 # @ Description:
 This script create a DAG that print hello world for Apache Airflow/
 Keep in mind the list of module you need in sequence for creating a DAG
 1. import modules
 2. DAG argument 
 3. Instaniate a DAG
 4. Task definition (Node)
 5. Task dependencies (Edge with direction)
 '''


from airflow import DAG
import datetime as dt
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2022,11,8),
    'retries':1,
    'retry_delay':dt.timedelta(minutes=5)
}

# instantiate a dag instance
dag = DAG('hello_world',
          description='A simple hello world DAG',
          default_args = default_args,
          schedule=dt.timedelta(seconds=5)
          )

# define tasks
task1 = BashOperator(
    task_id = 'print_hello',
    bash_command='echo \'Greeting. My name is \'',
    dag = dag,
)

# 
task2 = BashOperator(
    task_id = 'print_name',
    bash_command='whoami',
    dag = dag,
)

task3 = BashOperator(
    task_id = '3',
    bash_command='echo The date and time right now are ',
    dag = dag,
)

task4 = BashOperator(
    task_id = '4',
    bash_command='date',
    dag = dag,
)

# define sequence
task1 >> task2 >> task3 >> task4















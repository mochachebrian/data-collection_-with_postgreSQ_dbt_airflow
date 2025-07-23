#this file contains instrutions for postgres to create airflow use

CREATE USER airflow WITH PASSWORD 'airflow'
CREATE DATABASE airflow_db OWNER airflow;
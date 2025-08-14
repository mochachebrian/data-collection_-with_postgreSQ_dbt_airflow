# Weather Data Collection & Transformation Project

## Overview
This project automates the collection, storage, transformation, and analysis of weather data using **Airflow**, **PostgreSQL**, **dbt**, and **Docker**.  
It is designed to demonstrate a modern **data engineering pipeline** from data ingestion to analytics-ready tables.

---

## 🛠️ Tech Stack
- **Python** – for data ingestion from the Weather API
- **PostgreSQL** – database for storing raw and transformed data
- **dbt** – for SQL-based data transformations and modeling
- **Apache Airflow** – for workflow orchestration
- **Docker** – to containerize all services for easy deployment
- **Docker Compose** – for managing multi-container setup

---

##  Project Structure
weather-data-project/
│
├── airflow/ # Airflow DAGs, logs, and config
│ ├── dags/ # DAG scripts
│ └── plugins/ # Custom operators/hooks (if any)
│
├── dbt/ # dbt project folder
│ ├── models/ # dbt models (staging, marts, etc.)
│ └── profiles.yml # dbt connection settings
│
├── scripts/ # Python ingestion scripts
│ └── insert_data.py
│
├── docker-compose.yml # Docker services configuration
├── requirements.txt # Python dependencies
└── README.md # Project documentation

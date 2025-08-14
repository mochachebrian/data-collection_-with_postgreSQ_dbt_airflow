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

weather-data-project/
│
├── dags/                      # Airflow DAG definitions
│   ├── weather_api_orchestrator.py
│
├── dbt/                       # dbt project folder
│   ├── my_project/
│       ├── models/            # dbt models
│       ├── snapshots/         # dbt snapshots
│       ├── tests/             
│       ├── dbt_project.yml
│
├── scripts/                   # Data ingestion and utility scripts
│   ├── insert_data.py
│   ├── main.py
│
├── docker-compose.yml         # Docker setup for the project
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .env                       # Environment variables

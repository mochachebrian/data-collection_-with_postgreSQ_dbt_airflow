import psycopg2

from api_request import our_data
from datetime import datetime


def connect_to_db():
    print("connecrting to postgres database...")
    try:
        conn = psycopg2.connect(
            host = 'db',
            port = 5432,
            dbname = 'mochache_demo',
            password = 'brian56',
            user = 'postgres'
        )

        return conn

    except psycopg2.Error as e:
        print(f'database connection failed: {e}')
        raise 


def create_table(conn): 
    print(" creating id it does not exist...")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            
            CREATE SCHEMA IF NOT EXISTS dev;
                       
            CREATE TABLE IF NOT EXISTS dev.data (
        
              id SERIAL PRIMARY KEY,
              city VARCHAR(100),
              country VARCHAR(100),
              region VARCHAR(100),
              lat DECIMAL(8,5),
              lon DECIMAL(8,5),
              
              temperature INT,
              weather_desc VARCHAR(100),
              wind_speed INT,
              wind_degree INT,
              wind_dir VARCHAR(10),
              pressure INT,
              humidity INT,
    
              inserted_at TIMESTAMP DEFAULT NOW()      
            );
        """)
        conn.commit()       

    except psycopg2.Error as e:
        print(f"failed to create table: {e}")
        raise
        

conn = connect_to_db()
create_table(conn)

def insert_data(conn, data):
    print("inserting data into database...")

    if not data or "location" not in data or "current" not in data:
        print("Missing expected keys in API response:", data)
        return  
 
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dev.data(
                city,
                country,        
                region,
                lat, 
                lon,
                temperature,
                weather_desc,
                wind_speed,
                wind_degree,
                wind_dir,
                pressure,
                humidity,
                inserted_at             
                       
            )VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)


        """,(
            
            data["location"]["name"],
            data["location"]["country"],
            data["location"]["region"],
            data["location"]["lat"],
            data["location"]["lon"],
            data["current"]["temperature"],
            data["current"]["weather_descriptions"][0],
            data["current"]["wind_speed"],
            data["current"]["wind_degree"],
            data["current"]["wind_dir"],
            data["current"]["pressure"],
            data["current"]["humidity"],
            datetime.now()
))

        conn.commit()
        print("data succesfully inserted")

    except psycopg2.Error as e:
        print("error inserting data")
        raise

conn = connect_to_db()
create_table(conn)
insert_data(conn, our_data)


#packaging everything together

def main():
    try:
        data = our_data()
        conn= connect_to_db()
        create_table(conn)
        conn.close()
        insert_data(conn, data)

    except Exception as e:
        print(f"An error occured: {e}")

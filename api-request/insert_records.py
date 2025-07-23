import psycopg2
from api_request import mock_fetch_data  # Assuming mock_fetch_data exists and returns the expected structure


def connect_to_db():
    print("Connecting to PostgreSQL database...")
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            dbname="mochache_demo",
            user="postgres",
            password="brian56"
        )
        return conn
    except psycopg2.Error as e:
        print(f"Database connection failed: {e}")
        raise


def create_table(conn):
    print("Creating schema and table...")
    try:
        cursor = conn.cursor()

        # Create schema if it doesn't exist
        cursor.execute("CREATE SCHEMA IF NOT EXISTS dev")

        # Correct table creation with city column
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                weather_descriptions TEXT,
                wind_speed FLOAT,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT NOW(),
                utc_offset TEXT
            );
        """)

        conn.commit()
        print("Table created successfully.")
    except psycopg2.Error as e:
        print(f"Failed to create table: {e}")
        conn.rollback()


def insert_records(conn, data):
    print("Inserting weather data into database...")
    try:
        cursor = conn.cursor()

        # Now includes city in both the column list and the values
        cursor.execute("""
            INSERT INTO dev.raw_weather_data (
                city,
                temperature,
                weather_descriptions,
                wind_speed,
                time,
                utc_offset
            ) VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            data['location']['name'],
            data['current']['temperature'],
            ', '.join(data['current']['weather_descriptions']),
            data['current']['wind_speed'],
            data['location']['localtime'],
            data['location']['utc_offset']
        ))

        conn.commit()
        print("Data inserted successfully.")
        cursor.close()

    except Exception as e:
        print(f"Failed to insert data: {e}")
        conn.rollback()


# --- RUN ---
if __name__ == "__main__":
    print("Fetching weather data from weatherstack API...")
    data = mock_fetch_data()
    print("API response received successfully")

    conn = None
    try:
        conn = connect_to_db()
        create_table(conn)
        insert_records(conn, data)
    except Exception as e:
        print(f"An error occurred during the process: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")




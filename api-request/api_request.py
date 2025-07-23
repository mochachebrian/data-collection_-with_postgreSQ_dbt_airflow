import requests
api_key ="77aa880289fbb0e29eb46800388262fd"

api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

def fetch_data():
    print("fetching weather data from weatherstack API...")
    try: 
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received sucessfully")
        return response.json()
    except requests.exceptions.RequestsException as e:
        print(f"An error occurred: {e}")
        raise

fetch_data()

#now after writing the above code, create its mock thta we will use in the insert_records_py to load data into postgres

def mock_fetch_data():  
   return {
    'request': {
        'type': 'City',
        'query': 'New York, United States of America',
        'language': 'en',
        'unit': 'm'
    },
    'location': {
        'name': 'New York',
        'country': 'United States of America',
        'region': 'New York',
        'lat': '40.714',
        'lon': '-74.006',
        'timezone_id': 'America/New_York',
        'localtime': '2025-07-11 08:45',
        'localtime_epoch': 1752223500,
        'utc_offset': '-4.0'
    },
    'current': {
        'observation_time': '12:45 PM',
        'temperature': 24,
        'weather_code': 122,
        'weather_icons': [
            'https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png'
        ],
        'weather_descriptions': ['Overcast'],
        'astro': {
            'sunrise': '05:35 AM',
            'sunset': '08:28 PM',
            'moonrise': '09:31 PM',
            'moonset': '05:58 AM',
            'moon_phase': 'Waning Gibbous',
            'moon_illumination': 100
        },
        'air_quality': {
            'co': '540.2',
            'no2': '35.335',
            'o3': '198',
            'so2': '23.31',
            'pm2_5': '56.61',
            'pm10': '57.72',
            'us-epa-index': '3',
            'gb-defra-index': '3'
        },
        'wind_speed': 9,
        'wind_degree': 99,
        'wind_dir': 'E',
        'pressure': 1017,
        'precip': 0,
        'humidity': 77,
        'cloudcover': 100,
        'feelslike': 27,
        'uv_index': 1,
        'visibility': 14,
        'is_day': 'yes'
    }
}


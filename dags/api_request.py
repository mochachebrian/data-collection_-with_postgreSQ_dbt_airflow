import requests

api_url = 'http://api.weatherstack.com/current?access_key=44bd263872c7bd7c94b0d0cd87a2be41&query=New York'

def fetch_data():
    response = requests.get(api_url)
    data = response.json()
    return data
    print(response.json())

our_data = fetch_data()

print(our_data)
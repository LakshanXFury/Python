import requests

def get_weather(city):
    response = requests.get(f"http://api.weather.com/v1/{city}")
    if response.status_code == 200:
        return response.json()
    else:
        return ValueError("Could not fetch weather data")
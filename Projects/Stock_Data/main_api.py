"""
Stock Data
"""
import os
import requests


api_key = "API_KEY"

url = 'https://www.alphavantage.co/query?' # Endpoint
params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'IBM',
    'apikey': api_key

}

response = requests.get(url, params=params)
print(response.status_code)
print(response.json())

"""
Stock Data from API
"""

import requests
import os
from dotenv import load_dotenv

load_dotenv(override=True)

api_key = os.getenv('MARKET_DATA')

parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'IBM',
    'apikey': api_key
}

response = requests.get('https://www.alphavantage.co/query',params=parameters)

data = response.json()

time_series = data['Time Series (Daily)']

for date, value in time_series.items():
    print(f"The date : {date}")
    print(f"It opened with : {value["1. open"]}")
    print(f"Today's high : {value["2. high"]}" )
    print(f"Today's low :{value["3. low"]}")
    print(f"It closed with : {value["4. close"]}")
    print("------------------------- This is the End for the Day ------------------------")


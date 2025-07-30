import requests
from dotenv import load_dotenv
import os

load_dotenv()  # This loads variables from the .env file

base_url = "https://api.marketstack.com/v1/eod"
ACCESS_KEY = os.getenv("API_ACCESS_KEY")

data = input("The stock data that you want to search ? ").upper()

stock_params = {
    "access_key": ACCESS_KEY,
    "symbols": data
}


response = requests.get(base_url, params=stock_params)
request_post = response.json()

# Get the yesterday /recent data
recent_data = request_post["data"][0]
print(recent_data)
open_data = recent_data["open"]
print(f"The recent open data is : {open_data}")


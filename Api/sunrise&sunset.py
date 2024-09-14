import requests
from datetime import datetime

MY_Lat = 51.507351
MY_LONG = -0.127758

parameters = {
    "lat": MY_Lat,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters, verify=False)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(f"Sunrise: {sunrise}\nSunset: {sunset}")   #Split Fn

time_now = datetime.now()
print(time_now.hour)
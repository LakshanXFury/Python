import requests
from twilio.rest import Client

api_key = "c0166e8128426bebd74cdf87e6cf955b"
LATITUDE = "12.971599"
LONGITUDE = "77.594566"

#Twilio
account_sid = "AC0eb0a44ca659cef628808e4262923b27"
auth_token = "b03ac6827ea0fbb98c8d93478cfeb39d"


parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        # print("It is raining, carry an umbrella")
        will_rain = True

if will_rain:  #This is will the print statement only once
    # print("Bring an umbrella")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It is raining, carry an umbrella :) ",
        from_="+19498354575",
        to="+918277228628",
    )

    print(message.status)




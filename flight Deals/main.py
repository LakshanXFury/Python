#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager
#
# API_KEY = "kW3WNBl6QngjFdzdQpGtUryrky7BFvwg"
# API_SECRET = "EQqY4f1sLGifCbMz"
#
# google_sheet_endpoint = "https://api.sheety.co/3ef69424dbbb56c9ccb847e97298068c/flightDeals/prices"
#
# response = requests.get(url=google_sheet_endpoint)
#
# # print(response.json())
# pprint(response.json())
#
# sheet_data = response.json()["prices"]
# print(sheet_data)
#
# for entry in sheet_data:
#     entry['iataCode'] = 'Testing'
#
#     modify = requests.put(url=f"{google_sheet_endpoint}/iataCode", json=entry)


# -------------------------#

import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# API endpoint
google_sheet_endpoint = "https://api.sheety.co/3ef69424dbbb56c9ccb847e97298068c/flightDeals/prices"
Token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
search_city_endpoint = "https://api.amadeus.com/v1/reference-data/locations/cities"


# # Get the data from the Google Sheet using Sheety API
# response = requests.get(url=google_sheet_endpoint)
# sheet_data = response.json()["prices"]
#
# # Print the retrieved data
# pprint(sheet_data)

# Loop through the data and update the IATA code
# for entry in sheet_data:
#     # Update the 'iataCode' field with 'Testing'
#     entry['iataCode'] = 'Nigga'
#
#     # Create the PUT URL with the specific object ID
#     modify_url = f"{google_sheet_endpoint}/{entry['id']}"
#
#     # Prepare the data to be updated
#     data_to_update = {
#         "price": {
#             # "city": entry['city'],
#             "iataCode": entry['iataCode'],
#             # "lowestPrice": entry['lowestPrice']
#         }
#     }
#
#     # Make the PUT request to update the IATA code
#     modify_response = requests.put(url=modify_url, json=data_to_update)
#
#     # Check if the request was successful
#     if modify_response.status_code == 200:
#         print(f"Successfully updated {entry['city']} with IATA code.")
#     else:
#         print(f"Failed to update {entry['city']}. Error: {modify_response.status_code}")

# ---- Flight
# class FlightSearch:
#
#     def __init__(self):
#         self._api_key = API_KEY  # Replace with actual key
#         self._api_secret = API_SECRET  # Replace with actual secret
#         self._token = self._get_new_token()
#
#         # Now that we have a token, we can use it for subsequent requests
#         self.search_city()
#
#     def _get_new_token(self):
#         """
#         Generates the authentication token used for accessing the Amadeus API and returns it.
#         """
#         header = {
#             'Content-Type': 'application/x-www-form-urlencoded'
#         }
#         body = {
#             'grant_type': 'client_credentials',
#             'client_id': self._api_key,
#             'client_secret': self._api_secret
#         }
#         # Using test environment for token generation
#         response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", headers=header, data=body)
#
#         if response.status_code != 200:
#             raise Exception(f"Failed to get token: {response.status_code} {response.text}")
#
#         token = response.json().get('access_token')
#         expires_in = response.json().get('expires_in')
#
#         if token:
#             print(f"Your token is {token}")
#             print(f"Your token expires in {expires_in} seconds")
#         else:
#             raise Exception("No token found in the response")
#
#         return token
#
#     def search_city(self):
#         """
#         Searches for a city using the token.
#         """
#         headers = {"Authorization": f"Bearer {self._token}"}
#         parameters_endpoint = {
#             "keyword": "Frankfurt",
#             "max": "2",
#             "include": "AIRPORTS",
#         }
#
#         # Use the test environment for the city search as well
#         # search_city_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations"
#
#         city_response = requests.get(url=search_city_endpoint, params=parameters_endpoint, headers=headers)
#
#         if city_response.status_code == 200:
#             print(city_response.text)
#         else:
#             print(f"Failed to search city: {city_response.status_code} {city_response.text}")
#
#     # Example usage
# flight_search = FlightSearch()

#
# headers = {"Authorization": f"Bearer kp04NTyuilLEmNFyhDAAAHeAHzbD"}
#
# parameters_endpoint = {
#     "keyword": "Frankfurt",
#     "max": "2",
#     "include": "AIRPORTS",
# }
#
# city_response = requests.get(url=search_city_endpoint, params=parameters_endpoint, headers=)
# print(city_response.text)



#-------------------------------------------------------------------------------------------------------------------#

# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Set your origin airport
ORIGIN_CITY_IATA = "LON"

# ==================== Update the Airport Codes in Google Sheet ====================

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# ==================== Search for Flights and Send Notifications ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        # notification_manager.send_sms(
        #     message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
        #                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        # )
        # SMS not working? Try whatsapp instead.
        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )



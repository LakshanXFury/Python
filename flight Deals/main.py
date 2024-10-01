#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# import requests
# from pprint import pprint
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

# API endpoint
google_sheet_endpoint = "https://api.sheety.co/3ef69424dbbb56c9ccb847e97298068c/flightDeals/prices"

# Get the data from the Google Sheet using Sheety API
response = requests.get(url=google_sheet_endpoint)
sheet_data = response.json()["prices"]

# Print the retrieved data
pprint(sheet_data)

# Loop through the data and update the IATA code
for entry in sheet_data:
    # Update the 'iataCode' field with 'Testing'
    entry['iataCode'] = 'Nigga'

    # Create the PUT URL with the specific object ID
    modify_url = f"{google_sheet_endpoint}/{entry['id']}"

    # Prepare the data to be updated
    data_to_update = {
        "price": {
            # "city": entry['city'],
            "iataCode": entry['iataCode'],
            # "lowestPrice": entry['lowestPrice']
        }
    }

    # Make the PUT request to update the IATA code
    modify_response = requests.put(url=modify_url, json=data_to_update)

    # Check if the request was successful
    if modify_response.status_code == 200:
        print(f"Successfully updated {entry['city']} with IATA code.")
    else:
        print(f"Failed to update {entry['city']}. Error: {modify_response.status_code}")
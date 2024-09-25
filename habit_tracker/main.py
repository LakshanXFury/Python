import requests
from datetime import datetime

TOKEN = "sdadadadfdfsd"
USERNAME = "lakshan"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Hours spent on Coding :)",
    "unit": "min",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response_2 = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response_2.text)

## URL:- https://pixe.la/v1/users/lakshan/graphs/graph1.html

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
today_date = today.strftime("%Y%m%d")

brain_storm = input("How many hours did you code today nigga ? ")

pixel_creation_config = {
    "date": today_date,
    "quantity": brain_storm,
}

response_3 = requests.post(url=pixel_creation_endpoint, json=pixel_creation_config, headers=headers)
print(response_3.text)


#Put method to modify

# modify_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date}"
#
# modify_data = {
#     "quantity": "60.5"
# }
#
# modify_response = requests.put(url=modify_pixel, json=modify_data, headers=headers)
# print(modify_response.text)

#Delete method to delete pixel

# delete_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date}"
# delete_response = requests.delete(url=delete_pixel, headers=headers)
# print(delete_response)


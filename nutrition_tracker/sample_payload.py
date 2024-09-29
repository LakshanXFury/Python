import requests

# # Replace with your actual Bearer token
# auth_token = "dadasndnasdniwkjasasoa"
#
# # Authorization header
# headers = {
#     "Authorization": f"Bearer {auth_token}"
# }

# Sheety API endpoint for the "My Workouts" Google Sheet
google_sheet_endpoint = "https://api.sheety.co/3ef69424dbbb56c9ccb847e97298068c/myWorkouts/workouts"

# Sample data to post
sheet_config = {
    "workout":
    {
        "Date": "29/09/2024",
        "Time": "20:27:43",
        "Exercise": "running",
        "Duration": 12.43,
        "Calories": 142.12
    }
}


# Make the POST request
response = requests.post(url=google_sheet_endpoint, json=sheet_config)

# Print the response status code and text for debugging
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
print(f"Full Response: {response.json()}")


# Post second entry
# response2 = requests.post(url=google_sheet_endpoint, json=sheet_config2)
# print(response2.text)

import requests
from datetime import datetime

APP_ID = "6ebd5120"
API_KEY = "d9e1444f2cc9666987245cde121131e8"

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

workout_did = input("Tell me which exercise did you do ?\n")

parameters = {
    "query": workout_did
}

google_sheet_endpoint = "https://api.sheety.co/3ef69424dbbb56c9ccb847e97298068c/myWorkouts/sheet1"

response = requests.post(url=nutrition_endpoint, headers=headers, json=parameters)
print(response.text)

get_json_response = response.json()

today_time = datetime.now()

date_format = today_time.strftime("%d/%m/%Y")
print(date_format)

time_format = today_time.strftime("%H:%M:%S")
print(time_format)

for exercise_data in get_json_response["exercises"]:
    activity_done = exercise_data["name"]
    print(f"Activity done: {activity_done}")

    duration_min = exercise_data["duration_min"]
    print(f"Duration in min: {duration_min}")

    nf_calories = exercise_data["nf_calories"]
    print(f"Calories Burnt: {nf_calories}")

    sheet_config = {
        "sheet1": {
            "Date": date_format,
            "Time": time_format,
            "Exercise": activity_done,
            "Duration": duration_min,
            "Calories": nf_calories
        }
    }

    post_into_sheet = requests.post(url=google_sheet_endpoint, json=sheet_config)
    print(post_into_sheet.text)

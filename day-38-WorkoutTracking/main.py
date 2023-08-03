import requests
from datetime import datetime

APP_ID = "3b1fb559"
API_KEY = "3c00cdc3487d313648530e846bbebf49"

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/4109f017e74c092056c932eaf5943d9c/workout/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

exercise_params = {
    "query": input("Tell me which exercise you did: ")
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=headers)

exercises = response.json()["exercises"]
print(exercises)

sheety_headers = {
    "Authorization": "Basic c2FtdWVsOmExMjcyNzU2Mjg="
}

for item in exercises:
    now = datetime.now()
    body = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%X"),
            "exercise": item["name"].title(),
            "duration": item["duration_min"],
            "calories": item["nf_calories"]
        }
    }
    print(body)
    response = requests.post(url=SHEETY_ENDPOINT, json=body, headers=sheety_headers)
    print(response.json())




import requests
from datetime import datetime

APP_ID = "your api id"
API_KEY = "your api key"
GENDER = "male"
WEIGHT = 75
HEIGHT = 178
AGE = 20

workout_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/6269ffb9015b3f62777511618f58d006/workoutTracking/workouts"
sheety_token = "your token"

workout_params = {
    "query": input("Tell me which exercise you did "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

today = datetime.now()

response = requests.post(url=workout_endpoint, json=workout_params, headers=headers)
data = response.json()

sheety_headers = {
    "Authorization": sheety_token
}


for exercise in data["exercises"]:
    sheet_data = {
        "workout":{
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


    sheety_response = requests.post(url=sheety_endpoint, json=sheet_data, headers=sheety_headers)
    print(sheety_response.text)

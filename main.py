import requests
from datetime import datetime

GENDER = "female"
WEIGHT_KG = 56
HEIGHT_CM = 166
AGE = 29

APP_ID = "d6c9347c"
API_KEY = "3b704bbc9c6d7001fc59526aa4851ccc"

EXRCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did today: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=EXRCISE_ENDPOINT, headers=headers, json=parameters)
response.raise_for_status()
result = response.json()
print(result)

sheety_endpoint = "https://api.sheety.co/37597c231b5d892dd2ae1e2873e3bc46/workoutTracking/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)

    print(sheet_response.text)
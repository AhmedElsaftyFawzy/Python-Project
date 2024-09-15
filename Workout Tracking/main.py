import requests
import datetime as dt
import os


APP_ID = "b9c1033f"
API_KEY = "451491533601597e6bac5c55c22e0e97"
TOKEN = "EB&3PUg2hDn^7eK7KVau"
GENDER = "male"
WEIGHT_KG = 81.6
HEIGHT_CM = 172
AGE = 28

exercies_para={
    "query": input("Tell Me Which Exercies You Did ?? "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

header = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}

respond = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", json=exercies_para, headers=header)
respond.raise_for_status()
result = respond.json()

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")


header_bear = {
    
    "Authorization": f"Bearer {TOKEN}"

}

for exercise in result["exercises"]:
    sheet_para = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


    workout_post = requests.post(url="https://api.sheety.co/1679cb9a0fc7413c3757d2208d36b9d2/myWorkouts/workouts", json=sheet_para, headers=header_bear)
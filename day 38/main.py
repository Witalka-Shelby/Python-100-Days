import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os

def nutri_part():
    APP_ID = "test"
    API_KEY = "test"

    # try:
    #     with open("../api.txt") as key:
    #         API_KEY = key.readline()
    # except:
    #     print("No API file")


    nutri_header = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY
    }

    user_input = {
    "query": input("Tell me which workout did you do?: "),
    "gender":"male",
    "weight_kg":90.0,
    "height_cm":185.00,
    "age":35
    }

    nutri_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

    response = requests.post(url=nutri_url, headers=nutri_header, json=user_input)
    sheety_part(response.json())

def sheety_part(excercises_list):
    today = datetime.now()
    basic = HTTPBasicAuth('test', 'test')
    # print(today.strftime("%d/%m/%Y"))
    for excercise in excercises_list["exercises"]:
        body = {
            "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": excercise["name"].title(),
        "duration": excercise["duration_min"],
        "calories": excercise["nf_calories"],
        }
        }
        


        sheety_url = "https://api.sheety.co/895dca4bdfsdfsdf91/workoutTracking/workouts"
        response = requests.post(sheety_url, json=body, auth=basic)

        print(response.text)


nutri_part()
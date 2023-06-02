import requests
from datetime import datetime

try:
    with open("../api.txt") as key:
        api_key = key.readline()
except:
    print("No API file")


location_lat = "27.964157"
location_lon = "-82.452606"

url = f"http://api.openweathermap.org/data/2.5/forecast?lat={location_lat}&lon={location_lon}&appid={api_key}"

today = datetime.now()


response = requests.get(url)
print(response.status_code)
response.raise_for_status()
weather_data_json = response.json()
for weather in weather_data_json['list']:
    weather_date = weather['dt_txt'].split(" ")[0].split("-")[2]
    if (today.day + 2) == int(weather_date):
        print("48h !!!")


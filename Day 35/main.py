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
# print(response.status_code)
response.raise_for_status()
weather_data_json = response.json()['list']

for i in range(4):
    weather_date = int(weather_data_json[i]["dt_txt"].split(" ")[0].split("-")[2])
    weather_date_time = int(weather_data_json[i]["dt_txt"].split(" ")[1].split(":")[0])
    weather_id = weather_data_json[i]["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True
        print("Bring an umbrella")
        print(weather_data_json[i]["weather"][0]["description"])
        print(weather_data_json[i]["dt_txt"])

# for weather in weather_data_json:
#     weather_date = int(weather['dt_txt'].split(" ")[0].split("-")[2])
#     weather_date_time = int(weather['dt_txt'].split(" ")[1].split(":")[0])
#     if (weather_date_time-1)  <= (today.hour + 12) <= (weather_date_time+1) and weather_date == today.day:
#         print(weather["weather"][0]["description"])
#         print("~12h !!!")

# Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client


# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)
# message = client.messages \
#                 .create(
#                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                     from_='+133333336',
#                     to='+133333337'
#                 )
# if will_rain:
#     print(message.sid)
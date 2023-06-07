from datetime import datetime
from datetime import timedelta
import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
TELEGRAM_TOKEN = config['TELEGRAM']
CHAT_ID = config['TELE_ID']
SPACER = "\n"

class NotificationManager:
    def __init__(self, flight_list, telegram_id) -> None:
        TELEGRAM_TOKEN = telegram_id
        stop_over = ""
        price = flight_list["price"]
        departure_city = flight_list["cityFrom"]
        departure_code = flight_list["cityCodeFrom"]
        arrival_city = flight_list["cityTo"]
        arrival_code = flight_list["cityCodeTo"]
        # nights_stay = flight_list["nightsInDest"]
        flight_route = flight_list["route"]
        outbound_date = flight_route[0]["local_departure"].split("T")[0]
        inbound_date = flight_route[-1]["local_departure"].split("T")[0]
        if len(flight_route) > 2:
            inbound_date = flight_list["route"][int(len(flight_route) / 2)]["local_departure"].split("T")[0]
            stop_over = flight_route[0]["cityTo"]
        # string_date = datetime.strptime(outbound_date, "%Y-%m-%d")
        # inbound_date2 = string_date + timedelta(days=nights_stay)
        

        message = f"Sent from your Telegram Bot Account - Low price alert! Only {'${}'.format(price)} to fly from{SPACER}{departure_city}-{departure_code} to {arrival_city}-{arrival_code}, from {outbound_date} to {inbound_date}"

        if stop_over != "":
            message = message + f"{SPACER} Flight has 1 stop over, via {stop_over}."
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"

        # print(requests.get(url).json()) # this sends the message
        print(message)
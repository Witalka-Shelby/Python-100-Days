from datetime import datetime
from datetime import timedelta
from dotenv import dotenv_values

config = dotenv_values(".env")
GOOGLE_API = config['GOOGLE_API']

class NotificationManager:
    def __init__(self, flight_list) -> None:
        price = flight_list["price"]
        departure_city = flight_list["cityFrom"]
        departure_code = flight_list["cityCodeFrom"]
        arrival_city = flight_list["cityTo"]
        arrival_code = flight_list["cityCodeTo"]
        nights_stay = flight_list["nightsInDest"]
        outbound_date = flight_list["local_departure"].split("T")[0]
        string_date = datetime.strptime(outbound_date, "%Y-%m-%d")
        inbound_date = string_date + timedelta(days=nights_stay)
        inbound_date = inbound_date.strftime("%Y-%m-%d")

        message = f"""Sent from your Email Account - Low price alert! Only {'${}'.format(price)} to fly from 
        {departure_city}-{departure_code} to {arrival_city}-{arrival_code}, from {outbound_date} to {inbound_date}"""
        print(message)
from dotenv import dotenv_values
import requests
from datetime import datetime
from datetime import timedelta

config = dotenv_values(".env")
KIWI_API = config['KIWI_API']

class FlightData:

    def __init__(self) -> None:
        self.header = {"apikey": KIWI_API}
        today = datetime.today()
        self.tomorrow = today + timedelta(days= 1)
        self.half_year = self.tomorrow + timedelta(days=180)
        # print(self.tomorrow.strftime("%d/%m/%Y"))
        # "01/11/2023"
    
    def search_fligh(self, departure_airport_code, fly_to, lowest_price):
        config = {
            "fly_from": departure_airport_code,
            "fly_to": fly_to,
            "date_from": self.tomorrow.strftime("%d/%m/%Y"),
            "date_to": self.half_year.strftime("%d/%m/%Y"),
            "max_stopovers": 0,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "USD"
        }

        kiwi_url = "https://api.tequila.kiwi.com/v2/search"
        response = requests.get(url=kiwi_url, headers=self.header, params=config)
        response.raise_for_status()
        # flights = response.json()["data"]
        try:
            cheapest_fligt = response.json()["data"][0]
            airport = cheapest_fligt["cityTo"]
            price = cheapest_fligt["price"]
            if price <= lowest_price:
                return cheapest_fligt
                # print(f"{airport}: {'${}'.format(price)}")
        except IndexError:
            try:
                config = {
                    "fly_from": departure_airport_code,
                    "fly_to": fly_to,
                    "date_from": self.tomorrow.strftime("%d/%m/%Y"),
                    "date_to": self.half_year.strftime("%d/%m/%Y"),
                    "max_stopovers": 2,
                    "nights_in_dst_from": 7,
                    "nights_in_dst_to": 28,
                    "curr": "USD"
                }
                kiwi_url = "https://api.tequila.kiwi.com/v2/search"
                response = requests.get(url=kiwi_url, headers=self.header, params=config)
                response.raise_for_status()
                cheapest_fligt = response.json()["data"][0]
                airport = cheapest_fligt["cityTo"]
                price = cheapest_fligt["price"]
                if price <= lowest_price:
                    return cheapest_fligt
            except IndexError:
                return None
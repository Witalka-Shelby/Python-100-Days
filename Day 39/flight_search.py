#This class is responsible for talking to the Flight Search API.
from dotenv import dotenv_values
import requests

config = dotenv_values(".env")
KIWI_API = config['KIWI_API']

class FlightSearch:

    def __init__(self):
        self.header = {"apikey": KIWI_API}

    def iata_code(self, city_to_search):
        body = {
            "term": city_to_search
        }

        kiwi_url = "https://api.tequila.kiwi.com/locations/query"

        response = requests.get(url=kiwi_url, headers=self.header, params=body)

        response.raise_for_status()
        airports = response.json()
        for airport in airports["locations"]:
            airport_name = airport["name"]
            if airport_name.lower() == city_to_search.lower():
                return airport["code"]

        return False
    
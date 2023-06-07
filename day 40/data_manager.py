from dotenv import dotenv_values
import requests
from requests.auth import HTTPBasicAuth


config = dotenv_values(".env")
ACCOUNT = config['SHEETY_USERNAME']
PASSWORD = config['SHEETY_PASSWORD']

class DataManager:

    def __init__(self) -> None:
        self.basic = HTTPBasicAuth(ACCOUNT, PASSWORD)

    def update_iata_codes(self, id, iata):
        doc_url = f"https://api.sheety.co/895dca4b428381080aae4e9eb3482891/flightDeals/prices/{id}"
        body = {
            "price": {
                "iataCode": iata
            }
        }
        response = requests.put(doc_url, auth=self.basic, json=body)
        response.raise_for_status()

    def get_destenations(self):
        sheety_url = "https://api.sheety.co/895dca4b428381080aae4e9eb3482891/flightDeals/prices"
        response = requests.get(sheety_url, auth=self.basic)
        response.raise_for_status()
        places = response.json()
        return places["prices"]
        # for place in places["prices"]:
        #     print(place["city"])

# DataManager().get_destenations()
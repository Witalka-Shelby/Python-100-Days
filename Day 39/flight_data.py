from dotenv import dotenv_values
import requests

config = dotenv_values(".env")
KIWI_API = config['KIWI_API']

class FlightData:

    def __init__(self) -> None:
        header = {"apikey": KIWI_API}
        kiwi_config = {
            "fly_from": "LGA",
            "fly_to": "MIA",
            "date_from": "01/11/2023",
            "date_to": "24/11/2023",
            "curr": "USD"
        }
    
        kiwi_url = "https://api.tequila.kiwi.com/v2/search"
        response = requests.get(url=kiwi_url, headers=header, params=kiwi_config)

        response.raise_for_status()
        # print(response.text)

FlightData()
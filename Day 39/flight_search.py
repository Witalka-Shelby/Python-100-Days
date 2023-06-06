#This class is responsible for talking to the Flight Search API.
from dotenv import dotenv_values
import requests

config = dotenv_values(".env")
KIWI_API = config['KIWI_API']

class FlightSearch:

    def __init__(self):
        self.header = {"apikey": KIWI_API}

    def iata_code(self):
        iata_code = "TESTING"
        return iata_code
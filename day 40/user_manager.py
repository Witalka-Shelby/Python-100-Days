from dotenv import dotenv_values
from requests.auth import HTTPBasicAuth
import requests


config = dotenv_values(".env")
ACCOUNT = config['SHEETY_USERNAME']
PASSWORD = config['SHEETY_PASSWORD']


basic = HTTPBasicAuth(ACCOUNT, PASSWORD)

class User:
    def __init__(self) -> None:
              pass
       
    def add_user():
            print("Welcome to Witalka's Flight Club.")
            print("We find the best flight deals and email you.")
            first_name = input("What is your first name? ")
            last_name = input("What is your last name? ")
            email = input("What is your email? ")
            email_confirm = input("Type your email again. ")
            doc_url = f"https://api.sheety.co/895dca4b428381080aae4e9eb3482891/flightDeals/users"

            if email == email_confirm:
                body = {
                    "user": {
                "firstName": first_name.title(),
                "lastName": last_name.title(),
                "email": email.lower()
                }
                }
                response = requests.post(doc_url, auth=basic, json=body)
                response.raise_for_status()
            else:
                print("Email not equal")


    def get_user():
            doc_url = f"https://api.sheety.co/895dca4b428381080aae4e9eb3482891/flightDeals/users"
            response = requests.get(doc_url, auth=basic)
            response.raise_for_status()
            return response.json()

# add_user()
# get_user()

import requests

api_url = "https://opentdb.com/api.php?amount=10&type=boolean"

response = requests.get(api_url)

question_data = response.json()["results"]
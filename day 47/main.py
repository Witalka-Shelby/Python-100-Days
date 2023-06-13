import requests
from bs4 import BeautifulSoup
from dotenv import dotenv_values

config = dotenv_values(".env")
TELEGRAM_TOKEN = config['TELEGRAM']
CHAT_ID = config['TELE_ID']

URL = "https://www.amazon.com/Soundcore-Cancelling-Headphones-Multiple-Comfortable/dp/B08NP4CBBM/ref=sr_1_4?crid=DYLLSZONDBFL&keywords=soundcore%2Bq30%2Bheadphones&qid=1686659512&sprefix=soundcore%2Bq30%2Bheadphones%2Caps%2C107&sr=8-4&th=1"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
    "Accept-Language": "en-US,en;q=0.5"
}


response = requests.get(URL, headers=header)
response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

price = float(soup.find(name="span", class_="a-offscreen").text.replace("$", ""))

if price <= 60:
    message = f"Price alert!! Headphones price is {price} buy now !"
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"

    print(requests.get(telegram_url).json())
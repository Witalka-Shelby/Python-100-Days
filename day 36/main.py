import requests
from datetime import datetime
from datetime import timedelta
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

try:
    with open("../api.txt") as key:
        alpha_api_key = key.readline()
except:
    print("No API file")

try:
    with open("../news.txt") as key:
        news_api_key = key.readline()
except:
    print("No API file")


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def alpha_stock():
    today = datetime.today()
    yesterday = today - timedelta(days = 1)
    yesterday = yesterday.strftime("%Y-%m-%d")
    day_before_yesterday = today - timedelta(days = 2)
    day_before_yesterday = day_before_yesterday.strftime("%Y-%m-%d")
    alpha_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&outputsize=compact&apikey={alpha_api_key}"
    response = requests.get(alpha_url)
    response.raise_for_status()
    response = response.json()["Time Series (Daily)"]
    opening_yesterday = float(response[yesterday]["1. open"])
    opening_before_yesterday = float(response[day_before_yesterday]["1. open"])
    calc_percent = ((float(opening_yesterday)-opening_before_yesterday)/opening_before_yesterday)*100
    # print(opening_before_yesterday)
    # print(opening_before_yesterday * 1.05)
    # print(opening_before_yesterday * 0.95)
    # print(opening_yesterday)
    if opening_yesterday > opening_before_yesterday * 1.05 or opening_yesterday < opening_before_yesterday * 0.95:
        print(calc_percent)
        news_list = get_news()
        # sms_message(news_list)
        for news in news_list:
            print(news["title"])
        
        

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def get_news():

    news_url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={news_api_key}"
    response = requests.get(news_url)
    response.raise_for_status
    response_json = response.json()['articles']
    news_list = []
    for i in  range(3):
        news_list.append(response_json[i])
    
    return news_list


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

def sms_message(news_list):
    pass
    # I SKIP THE SMS PART
    # account_sid = os.environ['TWILIO_ACCOUNT_SID']
    # auth_token = os.environ['TWILIO_AUTH_TOKEN']
    # client = Client(account_sid, auth_token)

    # for news in news_list:
    #     print("Test")
    #     message = client.messages \
    #                     .create(
    #                         body=news["title"],
    #                         from_='+133333336',
    #                         to='+133333337'
    #                     )
    #     print(message.sid)

alpha_stock()
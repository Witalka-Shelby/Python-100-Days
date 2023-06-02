import requests
from datetime import datetime
from datetime import timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

try:
    with open("../api.txt") as key:
        alpha_api_key = key.readline()
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
    stock_name = "TSLA"
    alpha_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={stock_name}&outputsize=compact&apikey={alpha_api_key}"
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
        print("Get NEWS")

alpha_stock()
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


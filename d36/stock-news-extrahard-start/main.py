import requests
import datetime
import os
from twilio.rest import Client
import html

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
THRESHOLD = 0.04

api_key_stock = os.getenv("API_KEY_STOCK")
api_key_news = os.getenv("API_KEY_NEWS")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
my_verified_number = os.getenv("MY_VERIFIED_NUMBER")

client = Client(account_sid, auth_token)

stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key_stock
}

news_param = {
    "q":COMPANY_NAME,
    "from":"2024-08-20",
    "sortBy":"publishedAt",
    "apiKey": api_key_news
}

stock_url = "https://www.alphavantage.co/query"
news_url = "https://newsapi.org/v2/everything"

stock_response = requests.get(stock_url, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()['Time Series (Daily)']

stock_data_dt = [key for key,value in stock_data.items()]
stock_data_dt[:2]
#this is not having the date of today and yesterday coz today is Monday and surprise! these peeps dont trade on weekends
#for purpose of this script it would need proper date extracted --> parsed into the news api so that we gather it properly

stock_data_closing = [float(value['4. close']) for key,value in stock_data.items()]
stock_data_closing[:2]
daily_diff = stock_data_closing[1] / stock_data_closing[0] - 1
if daily_diff > 0:
    daily_diff_text = f"🔺{daily_diff}%"
else:
    daily_diff_text = f"🔻{daily_diff}%"

if abs(daily_diff) >= THRESHOLD:
    news_response = requests.get(news_url,news_param)
    news_response.raise_for_status()
    news_data = news_response.json()['articles'][:3]
    to_send_msg = html.unescape(f"""{STOCK}: {daily_diff_text}
        Headline: {news_data[-1]['title']}
        Brief: {news_data[-1]['content']}
    """)
else:
    to_send_msg = f"Not to worry, {stock_data_closing[:2], daily_diff}"

message = client.messages.create(
    from_='+12568575370',
    to=my_verified_number,
    body=to_send_msg
    )

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

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


import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
api_key = os.getenv("API_KEY_OPEN_WEATHER") #https://openweathermap.org/full-price#current
my_verified_number = os.getenv("MY_VERIFIED_NUMBER")
location = "hanoi"
forecast_days = 4

parameters = {
    "q": location,
    "appid": api_key,
    "cnt": forecast_days
}

api_url = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(api_url,params=parameters)
response.raise_for_status()
data = response.json()


proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
client = Client(account_sid, auth_token, http_client=proxy_client)

for x in range(0,len(data['list'])-1):
    if data['list'][x]['weather'][0]['id'] < 700:
        message = client.messages.create(
        from_='+12568575370',
        to=my_verified_number,
        body=f"""Houston we got rain ☔️,
            expected at {data['list'][x]['dt_txt']},
            {data['list'][x]['weather'][0]['description']}"""
        )

print(message.sid)

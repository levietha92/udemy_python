import requests
import os
from twilio.rest import Client

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

# api_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
api_url = f"https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(api_url,params=parameters)
response.raise_for_status()
data = response.json()

#list of dict!
# forecast = []
# for x in range(0,len(data['list'])-1):
#     record = {}
#     record['dt'] = data['list'][x]['dt_txt']
#     record['id'] = data['list'][x]['weather'][0]['id']
#     record['desc'] = data['list'][x]['weather'][0]['description']
#     # check if rain in the next 12 hours
#     if data['list'][x]['weather'][0]['id'] <700:
#         record['need_umbrella'] = True
#     else:
#         record['need_umbrella'] = False
#     forecast.append(record)

# forecast

#use twilio to send noti if rains

client = Client(account_sid, auth_token)

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

# using twilio <> whatsapp
message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Yoohoo rains!',
  to=f'whatsapp:{my_verified_number}'
)
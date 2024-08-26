import requests
import os

api_key = os.getenv("API_KEY_OPEN_WEATHER")
location = "taipei,taiwan"

# api_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
api_url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}"

response = requests.get(api_url)
response.raise_for_status()
data = response.json()
print(data['cod'])
for x in range(0,len(data['list'])-1):
    print([data['list'][x]['weather'][0]['id'],data['list'][x]['weather'][0]['description']])

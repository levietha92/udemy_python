import requests
import os
import datetime as dt
from dotenv import load_dotenv

env_path = "/Users/ha.le/Github/udemy_course/.env"
load_dotenv(dotenv_path=env_path)

"""What we do here?
- We basically use 2 APIs
- Natural lang Nutritionix API allows us to convert a human sentence that describes an exercise into json-output data
    -type of exercise
    -duration
    -calories etc.
- We need to output this somewhere overtime for tracking purpose (imagine an app)
- Sheety API allows us to update records into tabular form into Google Sheet
- So we need to use the Nutri output --> turn into df --> output into Google Sheet using Sheety.
"""
# Nutritionix --> llm
APP_ID_NUTRITIONIX = os.getenv("APP_ID_NUTRITIONIX")
APP_KEY_NUTRITIONIX = os.getenv("APP_KEY_NUTRITIONIX")

host_domain = "https://trackapi.nutritionix.com"
nat_lang_endpoint = "/v2/natural/exercise"
nat_lang_url = f"{host_domain}{nat_lang_endpoint}"

nat_lang_params = {
    "query": input("What did you exercise today?")
}

headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID_NUTRITIONIX,
    'x-app-key': APP_KEY_NUTRITIONIX
}

response = requests.post(url=nat_lang_url,json=nat_lang_params,headers=headers)
response.text
response.json()

# Sheety
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
sheety_endpoint = "https://api.sheety.co/c52d2b5144f9da103eda087455f6d349/udemyD38Workouts/workouts"

latest_record_count = len(requests.get(url=sheety_endpoint).json())

sheety_new_record = {
    'workout': {
        'date': dt.datetime.today().strftime("%d/%m/%Y"),
        'time': dt.datetime.now().strftime("%H:%M:%S"),
        'exercise': response.json()['exercises'][0]['name'].title(),
        'duration': int(response.json()['exercises'][0]['duration_min']),
        'calories': int(response.json()['exercises'][0]['nf_calories']),
        'id': latest_record_count+1}
}
sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}
sheety = requests.post(url=sheety_endpoint,json=sheety_new_record,headers=sheety_headers)
sheety.text

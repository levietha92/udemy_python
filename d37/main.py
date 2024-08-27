import requests
import os
from dotenv import load_dotenv
import datetime as dt

env_path = "/Users/hanna/GitHub/udemy_course/.env"
load_dotenv(dotenv_path=env_path)

# Create a user
user_endpoint = "https://pixe.la/v1/users"

user_name_pixela = os.getenv("USER_NAME_PIXELA")
token_pixela = os.getenv("TOKEN_PIXELA")

#token is basically password and is made up
user_params = {
    "token":token_pixela, 
    "username":user_name_pixela, 
    "agreeTermsOfService":"yes", 
    "notMinor":"yes"
}

user_response = requests.post(url=user_endpoint,json=user_params)
user_response.json()

# Create a graph
graph_endpoint = f"{user_endpoint}/{user_name_pixela}/graphs"

graph_params = {
    "id":"graph1",
    "name":"python-tracker",
    "unit":"days",
    "type":"int",
    "color":"ichou"
    }

headers = {
    "X-USER-TOKEN": token_pixela
}
graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
graph_response.text

# Create a pixel in that graph
pixel_endpoint = f"{graph_endpoint}/graph1"
today = dt.datetime(2024,6,1)
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "20"
}

pixel_response = requests.post(url=pixel_endpoint,json=pixel_params,headers=headers)
pixel_response.text
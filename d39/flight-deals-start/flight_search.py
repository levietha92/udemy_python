from dotenv import load_dotenv
import os
import requests
import datetime as dt
from pprint import pprint
# Load environment variables
env_path = "/Users/ha.le/Github/udemy_course/.env"
load_dotenv(dotenv_path=env_path)

class FlightSearch:
    def __init__(self):
        self.client_id = os.getenv("API_KEY_FLIGHT")
        self.client_secret = os.getenv("API_SECRET_FLIGHT")
        self.host_domain = "https://test.api.amadeus.com"
        self.token_url = f"{self.host_domain}/v1/security/oauth2/token"
        self.access_token = self.get_access_token()
        self.headers = {"Authorization": f"Bearer {self.access_token}"}
        print("Headers", self.headers)
        print(f"ClientID:{self.client_id}, client secret: {self.client_secret}")
        
    def get_access_token(self):
        print("Getting access token")
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        response = requests.post(url=self.token_url, data=data) 
        #apparently all this time it failed because I used json param, but should be data! also confused post with get
        response.raise_for_status()
        print("Token response", response.json())
        return response.json()["access_token"]

    def get_flights(self,origin: str,destination: str,adults=1,departure_date="2024-08-01"):# departure_date=dt.datetime.today().strftime("%Y-%m-%d")
        print(f"Getting Flight info for {origin}>{destination}, {departure_date}")
        endpoint = "v2/shopping/flight-offers"
        url = f"{self.host_domain}/{endpoint}"
        self.parameters = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": departure_date,
            "adults": adults
        }
        try:
            response = requests.get(url=url, params=self.parameters, headers=self.headers)
            return response.json()
        except KeyError as e:
            return e
    
    def get_iata_code(self, city_name:str):
        print(f"Getting IATA Code for {city_name}")
        iata_endpoint = f"{self.host_domain}/v1/reference-data/locations/cities?keyword={city_name}&include=AIRPORTS"
        try:
            response = requests.get(url=iata_endpoint,headers=self.headers)
            return response.json()['data'][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        # response.raise_for_status()
        
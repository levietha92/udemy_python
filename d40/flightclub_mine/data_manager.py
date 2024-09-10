import requests
from pprint import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        """Retrieve data found in Google Sheet via Sheety API
        """
        self.endpoint = "https://api.sheety.co/c52d2b5144f9da103eda087455f6d349/udemyD39Flights/prices"
        
    def get_sheet_data(self):
        self.get_response = requests.get(url=self.endpoint)
        self.get_response.raise_for_status()
        sheet_data = self.get_response.json()['prices']
        return sheet_data

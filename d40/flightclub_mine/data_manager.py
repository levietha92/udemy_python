import requests
from pprint import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        """Retrieve data found in Google Sheet via Sheety API
        """
        self.price_endpoint = "https://api.sheety.co/c52d2b5144f9da103eda087455f6d349/udemyD39Flights/prices"
        self.user_endpoint = "https://api.sheety.co/c52d2b5144f9da103eda087455f6d349/udemyD39Flights/formResponses"
        self.user_data = self.get_user_data()
        self.price_data = self.get_price_data()

    def get_price_data(self):
        get_response = requests.get(url=self.price_endpoint)
        get_response.raise_for_status()
        price_data = get_response.json()['prices']
        return price_data

    def get_user_data(self):
        get_response = requests.get(url=self.user_endpoint)
        get_response.raise_for_status()
        user_data = get_response.json()['formResponses']
        return user_data

    def get_user_dict(self):
        email_list = [self.user_data[i]['yourEmailPlease?'] for i in range(0, len(self.user_data))]
        first_name = [self.user_data[i]['firstName'] for i in range(0, len(self.user_data))]
        return dict(zip(first_name, email_list))

# user_endpoint = "https://api.sheety.co/c52d2b5144f9da103eda087455f6d349/udemyD39Flights/formResponses"
# test = requests.get(url=user_endpoint)
# test.json()
# user_data = test.json()['formResponses']
# email_list = [test.json()['formResponses'][i]['yourEmailPlease?'] for i in range(0, len(test.json()['formResponses']))]
# email_list
# len(test.json()['formResponses'])
# first_name = [user_data[i]['firstName'] for i in range(0, len(user_data))]
# first_name
# to_send_dict = dict(zip(first_name, email_list))
# to_send_dict


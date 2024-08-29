from data_manager import DataManager
# from flight_data import FlightData
from flight_search import FlightSearch
# from notification_manager import NotificationManager
import requests
from pprint import pprint

data = DataManager()
sheet_data = data.get_sheet_data()
print(sheet_data)


flight_search = FlightSearch()
flight_search.get_iata_code("HANOI")

for i in range(0, len(sheet_data)):
    if len(sheet_data[i]['iataCode'])==0:
        new_record = {
            'price': {
                'iataCode': flight_search.get_iata_code()[i]
            }}
        put_response = requests.put(url=f"{endpoint}/{i+2}",json=new_record)

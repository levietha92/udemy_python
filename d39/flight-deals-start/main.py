from data_manager import DataManager
# from flight_data import FlightData
from flight_search import FlightSearch
# from notification_manager import NotificationManager
import requests
from pprint import pprint

data = DataManager()
sheet_data = data.get_sheet_data()
flight_search = FlightSearch()

#writing IATACode into the sheet
for i in range(0, len(sheet_data)):
    if len(sheet_data[i]['iataCode'])==0:
        new_record = {
            'price': {
                'iataCode': flight_search.get_iata_code(sheet_data[i]['city'])
            }}
        put_response = requests.put(url=f"{data.endpoint}/{i+2}",json=new_record)
        destination_code = put_response.json()['price']['iataCode']
        print(destination_code)

        # Getting flight info
        flight_response = flight_search.get_flights(
            origin="HAN",
            destination=destination_code,
            departure_date="2024-10-01",
            adults=1
            )

        flight_response_price = float(flight_response['data'][0]['price']['total'])
        if flight_response_price < sheet_data[i]['lowestPrice']:
            print("send Twilio")
        else:
            print("Price not good")

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
import requests
import json

""" What we need to update:
- Instead of just sending the message to my phone number --> send message to User list based on Google Form list
- Some more details around non-stop flight to be added to the FlightData class, so that users can choose the best for themselves
"""

data = DataManager()
sheet_data = data.get_price_data()
flight_search = FlightSearch()
origin_code = "HAN"
departure_date = "2024-10-11"
#writing IATACode into the sheet
for i in range(0, len(sheet_data)):
    if len(sheet_data[i]['iataCode'])==0:
        new_record = {
            'price': {
                'iataCode': flight_search.get_iata_code(sheet_data[i]['city'])
            }}
        put_response = requests.put(url=f"{data.endpoint}/{i+2}",json=new_record)
        destination_code = put_response.json()['price']['iataCode']
    else:
        destination_code = sheet_data[i]['iataCode']
    print(destination_code)

    # Getting flight info
    flight_response = flight_search.get_flights(
        origin=origin_code,
        destination=destination_code,
        departure_date=departure_date,
        adults=1
        )
    
    filepath = f"output/{origin_code}_{destination_code}.txt"
    
    # outputing the json data
    with open(file=filepath, mode='w') as f:
        json.dump(flight_response, f, indent=4)

    # Find the lowest price itinerary from the json output
    flight_data = FlightData(filepath)
    lowest_price = flight_data.lowest_price()
    
    # send noti if it is lower price 
    if lowest_price < sheet_data[i]['lowestPrice']:
        print("send Noti")
        noti = NotificationManager()
        # noti.send_message(flight_data.chosen_flight(origin_code=origin_code,destination_code=destination_code))
        noti.send_email(
            to_send_dict=data.get_user_dict(),
            body=flight_data.chosen_flight(origin_code=origin_code,destination_code=destination_code)
        )

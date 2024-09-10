import json
import pandas as pd
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, filepath):
        self.filepath = filepath
        with open(file=filepath) as file:
            self.content = json.load(file)
        self.data = self.content['data']
        self.data_length = len(self.data)

        self.output = []
        for i in range(0, self.data_length):
            record = {}
            record['id'] = self.data[i]['itineraries'][0]['segments'][0]['carrierCode'] + self.data[i]['itineraries'][0]['segments'][0]['number'] #flight number
            record['stops'] = len(self.data[i]['itineraries'][0]['segments']) - 1
            record['transit_at'] = self.data[i]['itineraries'][0]['segments'][0]['arrival']['iataCode']
            record['lastTicketingDateTime'] = self.data[i]['lastTicketingDateTime']
            record['duration'] = self.data[i]['itineraries'][0]['duration']
            record['grandTotal'] = float(self.data[i]['price']['grandTotal'])
            record['currency'] = self.data[i]['price']['currency']
            self.output.append(record)
        self.output_df = pd.DataFrame(self.output)
        self.stop_count = 0

    def filter_data(self):
        #ideally want to rank this result based on: shortest duration + lowest cost
        try:
            if len(self.output_df[self.output_df['stops']==self.stop_count]) == 0:
                self.stop_count+=1
            self.filtered_df = self.output_df[self.output_df['stops']==self.stop_count]
            self.filtered_df.reset_index(inplace=True)
        except:
            print("There is no data found")
            self.filtered_df = self.output_df
        return self.filtered_df
            

    def lowest_price(self):
        self.filter_data()
        try:
            min_price = self.filtered_df['grandTotal'].min()
            print(f"Lowest Price is {min_price}")
        except KeyError:
            min_price = 9999
            print("There is no data found")
        finally:
            return min_price

    def chosen_flight(self,origin_code, destination_code):
        self.filter_data()
        min_price = self.lowest_price()
        for i in range(0, len(self.filtered_df)):
            if min_price == self.filtered_df['grandTotal'][i]:
                to_send_msg = f"""
                Best choice: Flight {self.filtered_df['id'][i]}
                Flight {origin_code} to {destination_code}
                Number of stops:  {self.filtered_df['stops'][i]}
                Duration: {self.filtered_df['duration'][i]}
                Transit/Land at {self.filtered_df['transit_at'][i]}
                
                Cost: {min_price} {self.filtered_df['currency'][i]}
                """
        print(to_send_msg)
        return to_send_msg

# flightdata = FlightData('/Users/hanna/GitHub/udemy_course/d40/flightclub_mine/output/HAN_TYO.txt')
# flightdata.output_df
# filtered_df = flightdata.filter_data()
# filtered_df.reset_index(inplace=True)
# min_price=flightdata.lowest_price()
# # flightdata.chosen_flight(origin_code="HAN",destination_code="TYO")
# for i in range(0, len(filtered_df)):
    
#     # if min_price == filtered_df['grandTotal'][i]:
#         print(filtered_df['grandTotal'][i])
#         # to_send_msg = f"""Best choice: ✈️ Flight {filtered_df['id'][i]}
#         # Flight "HAN" to "TYO"
#         # Number of stops:  {filtered_df['stops'][i]}
#         # Duration: {filtered_df['duration'][i]}
#         # Transit/Land at {filtered_df['transit_at'][i]}
        
#         # Cost: {min_price} {filtered_df['currency'][i]}
#         # """

# filtered_df['grandTotal']        
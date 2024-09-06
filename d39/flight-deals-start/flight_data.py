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
            record['id'] = self.data[i]['id']
            record['transit_at'] = self.data[i]['itineraries'][0]['segments'][0]['arrival']['iataCode']
            record['lastTicketingDateTime'] = self.data[i]['lastTicketingDateTime']
            record['duration'] = self.data[i]['itineraries'][0]['duration']
            record['grandTotal'] = float(self.data[i]['price']['grandTotal'])
            record['currency'] = self.data[i]['price']['currency']
            self.output.append(record)

    def lowest_price(self):
        self.output_df = pd.DataFrame(self.output)
        try:
            min_price = self.output_df['grandTotal'].min()
            print(f"Lowest Price is {min_price}")
        except KeyError:
            min_price = 9999
            print("There is no data found")
        finally:
            return min_price

    def chosen_flight(self,origin_code, destination_code):
        min_price = self.lowest_price()
        for i in range(0, len(self.output_df)):
            if min_price == self.output_df['grandTotal'][i]:
                to_send_msg = f"""Best choice is No.{self.output_df['id'][i]} 
                Flight {origin_code} to {destination_code} 
                transit at {self.output_df['transit_at'][i]} for {min_price}{self.output_df['currency'][i]}
                """
        return to_send_msg
        
import pandas as pd
import os

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240813.csv')
data.head()

"""Challenge:
Create output file with 2 columns: Fur Color, count
"""
fur_color = data['Unique Squirrel ID'].groupby(data['Primary Fur Color']).count()
fur_color_df = pd.DataFrame(fur_color)
fur_color_df.to_csv('fur_color_count.csv')

#the udemy lecturer used data_dict, calculated the count of each squirrel color and thenn map to df
import pandas as pd
# import numpy as np

data = pd.read_csv("weather_data.csv")
data.head()

print(data.temp) #this is a series
temp = data['temp'].to_list() #convert to list
print(temp)

#can perform math on the pandas series
print(data['temp'].mean())

#use the longer route
print(sum(temp) / len(temp))

# get data in row of df
print(data[data.day == 'Monday'])

print(data[data.temp == max(data.temp)])
print(data[data.temp == data.temp.max()])

# convert temp to F
data['temp_f'] = data.temp * 9/5 + 32
print(data)

# create df from scratch
data_dict = {
    "students": ['Amy',"james"],
    "scores": [43,53]
}
pd.DataFrame(data_dict)
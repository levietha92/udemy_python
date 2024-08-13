import csv

with open("weather_data.csv") as file:
    data = csv.reader(file)
    print(data)
    temp = []
    for row in data:
        print(row)
        temp_row = row[1]
        temp.append(temp_row)

temp_final = []
for item in temp[1:]:
    item = int(item)
    temp_final.append(item)
print(temp_final)
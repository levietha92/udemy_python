import requests
from datetime import datetime
from config import *
import geopy.distance

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now() #this is giving me local timezone

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

# Check

coords_1 = (MY_LAT, MY_LONG)
coords_2 = (iss_latitude, iss_longitude)

distance = geopy.distance.geodesic(coords_1, coords_2).km
print(distance)

if distance <= 0.5 and (time_now.hour >= sunset or time_now.hour < sunrise):
    send_email(
        subject="Look up for the ISS!", 
        message=f"Yo, look up, wear some night goggles\n The distance of ISS from your location is {distance} km",
        to_email=to_email,
        password=my_password
        )
else:
    send_email(
        subject="International Space Station here! Just a lazy test", 
        message=f"The distance from your location is {distance} km, boo",
        to_email=to_email,
        password=my_password
        )
print(f"Distance: {distance}, LocalTime: {time_now.hour}:{time_now.min}, Sunset:{sunset}")
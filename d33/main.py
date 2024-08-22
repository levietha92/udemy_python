import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response) # returns <Response [200]>
print(response.content)
print(response.json())
print(response.status_code)

"""
https://www.webfx.com/web-development/glossary/http-status-codes/
404 = not found
1xx = hold on
2xx = ok
3xx = permission lacking
4xx = you screwed up
5xx = i screwed up (the web)
"""

response.raise_for_status()

data = response.json()
data['timestamp']
data['iss_position']['longitude']
data['iss_position']['latitude']

# https://sunrise-sunset.org/api --> SOME API NEEDS PARAMETERS

import requests

MY_LAT = 48.856613
MY_LONG = 2.352222

parameter = {
    "lat": MY_LAT,
    "lng": MY_LONG, #this comes from their documentation --> request parameters
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
# print(response)
response.raise_for_status() #need this to raise for status right away
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
sunrise.split("T")[1].split(":")[0]
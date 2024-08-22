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
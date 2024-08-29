import requests

url = "https://flight-radar1.p.rapidapi.com/flights/list-in-boundary"

querystring = {"bl_lat":"13.607884","bl_lng":"100.641975","tr_lat":"13.771029","tr_lng":"100.861566","limit":"3"}

headers = {
	"x-rapidapi-key": "2493847d36msh0772538151f9230p1b6bd6jsn91a725e70951",
	"x-rapidapi-host": "flight-radar1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
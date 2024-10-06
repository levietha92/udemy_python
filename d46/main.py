import requests
from bs4 import BeautifulSoup
import re

date_param = input("Which year do you want to travel to? Type date in format YYYY-MM-DD")

url = f"https://www.billboard.com/charts/hot-100/{date_param}"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

song_names = soup.find_all(name="h3", class_=r"a-no-trucate")
band_names = soup.find_all(name="span", class_=r"a-no-trucate")

print(len(song_names), len(band_names))

songs = [" ".join(item.getText().split()) for item in song_names]
songs
bands = [" ".join(item.getText().split()) for item in band_names]
bands

result = dict(zip(songs, bands))
print(result)



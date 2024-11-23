import requests
from bs4 import BeautifulSoup
import re
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

# getting the top 100 songs from Billboard 100
date_param = input("Which year do you want to travel to? Type date in format YYYY-MM-DD")

url = f"https://www.billboard.com/charts/hot-100/{date_param}"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

song_names = soup.find_all(name="h3", class_=r"a-no-trucate")
band_names = soup.find_all(name="span", class_=r"a-no-trucate")

print(len(song_names), len(band_names))

songs = [" ".join(item.getText().split()) for item in song_names]
bands = [" ".join(item.getText().split()) for item in band_names]

print(f"Songs are traced from Billboard top 100")
# result = dict(zip(songs, bands))
# print(result)

# connecting to Spotify account
env_path = "/Users/ha.le/Github/udemy_course/.env"
load_dotenv(dotenv_path=env_path)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id = os.getenv("SPOTIFY_CLIENT"),
    client_secret = os.getenv("SPOTIFY_SECRET"),
    scope=['playlist-modify-public','user-read-private'],
    redirect_uri='http://example.com', #this must match the Dashboard App setting,
    show_dialog=True
))
print("Connect to Spotify complete")

# getting the songs URI by using search function of spotify
song_uris = []

for i in range(0,100):
    search_json = sp.search(q=f"{songs[i]} {bands[i]}", type='track',market='US',limit=1)
    song_id = search_json['tracks']['items'][0]['id']
    song_uris.append(song_id)

print(f"The song URIs are found")

new_playlist = sp.user_playlist_create(
    public=True,
    user=os.getenv("SPOTIFY_USER_ID"),
    name=f"Top 100 on {date_param}",
    description=f"A python-generated playlist of Billboard top 100 on your date {date_param}"
)
print(f"""New playlist have been created: 
    PlaylistID: {new_playlist['id']} 
    Go to link: {new_playlist['external_urls']['spotify']}
    SnapshotID: {new_playlist['snapshot_id']}
    Adding songs in progress...
        """
    )

sp.playlist_add_items(
    playlist_id=new_playlist['id'],
    items=song_uris
)
print(f"Songs have been added for your playlist Top100 {date_param}")


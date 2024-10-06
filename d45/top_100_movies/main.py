import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

movie_list = [title.getText() for title in soup.find_all(name="h3", class_="title")]

movie_list.reverse()


with open('movie.txt', "w") as file:
    file.writelines("\n".join(movie_list))



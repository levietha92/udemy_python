import requests
from bs4 import BeautifulSoup


response = requests.get("https://news.ycombinator.com/news")
# https://appbrewery.github.io/news.ycombinator.com/ is the static page


soup = BeautifulSoup(response.text, "html.parser")
print(soup)

title_list = []
href_list = []
score_list = []

# for title in soup.find_all(name="span", class_="titleline"):
#     title_list.append(title.a.string)
#     href_list.append(title.a.get("href"))
 
# for subtitle in soup.find_all(name="span", class_="score"):
#     score_list.append(subtitle.getText().split()[0])

articles = soup.find_all(name="span", class_="titleline")

title_list = [title.a.string for title in soup.find_all(name="span", class_="titleline")]
href_list = [title.a.get("href") for title in articles]
score_list = [int(subtitle.getText().split()[0]) for subtitle in soup.find_all(name="span", class_="score") ]

# my solution
for i in range(0,len(score_list)):
    if score_list[i] == max(score_list):
        index = i

# better solution
index = score_list.index(max(score_list))

print(f"""Highest scored title is: {title_list[index]}
and its link: {href_list[index]}
and its score: {score_list[index]}
""")

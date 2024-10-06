import os
from bs4 import BeautifulSoup
import html

with open('website.html') as file:
    contents = file.read()

print(contents)

soup = BeautifulSoup(contents, "html.parser")
soup.h3.string

print(soup.prettify())

#find all things belonging to same property
for tag in soup.find_all(name="a"):
    # print(tag.getText())
    print(tag.get("href"))

#find a single particular one
heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_ = "heading")
print(section_heading)

# css selectors

company_url = soup.select_one(selector = "p a")
print(company_url)


with open('quiz.html') as file:
    quiz_html = file.read()

soup2 = BeautifulSoup(quiz_html, "html.parser")
soup2.select("li a")
soup2

soup2.find("input").get("maxlength")

# Legality of webscraping
"""
Anything behind login wall = illegal
Commercialized from scraping = sue-able
If there is API for it, use API (though monies)
Ethics
Enter robots.txt at end of .com to find details
"""
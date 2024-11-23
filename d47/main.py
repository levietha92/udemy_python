import requests
from bs4 import BeautifulSoup
import re
import os
from dotenv import load_dotenv
from pprint import pprint
import smtplib

#----------------------------------- SET UP -----------------------------------#
env_path = "/Users/ha.le/Github/udemy_python/.env"
load_dotenv(dotenv_path=env_path)
my_email = os.getenv("APP_EMAIL")
my_password = os.getenv("APP_PASSWORD")
to_email = os.getenv("TO_EMAIL")
print(my_email,my_password)
print(to_email)


TARGET_PRICE = 100
# url = f"https://appbrewery.github.io/instant_pot/"
url = f"https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

def send_email(subject, message, to_email, password):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #encrypt the mail, transport layer security
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:{subject}\n\n {message}")

#----------------------------------- SCRIPT -----------------------------------#

response = requests.get(url, headers={
    "Accept-Language":"en-US",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
})
# to show header use this https://myhttpheader.com/

soup = BeautifulSoup(response.text, "html.parser")
pprint(soup)

price_box = soup.find_all(name="span", class_="a-price aok-align-center")[0]
price = [item.getText().split() for item in price_box][0][0]
price = float(price.replace('$',''))

print(price)

if price <= TARGET_PRICE:
    send_email(
            subject=f"Woohoo price drop! Buy now!",
            message=f"Price of your favorite item in {url} has dropped to {price}",
            to_email=to_email,
            password=my_password
        )
    print("Message sent")
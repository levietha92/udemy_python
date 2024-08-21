import smtplib
from dotenv import load_dotenv
import os
import datetime as dt
import datetime as dt
import random

#----------------------------------- SET UP -----------------------------------#
env_path = "/Users/hanna/GitHub/udemy_course/.env"
load_dotenv(dotenv_path=env_path)
my_email = os.getenv("APP_EMAIL")
my_password = os.getenv("APP_PASSWORD")
print(my_email,my_password)

#----------------------------------- FUNCTIONS -----------------------------------#
def send_email(subject, message, email, password):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #encrypt the mail, transport layer security
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="vietha.le92@gmail.com", 
            msg=f"Subject:{subject}\n\n {message}")
        # connection.close()

#----------------------------------- SCRIPT -----------------------------------#
# check if Monday --> send motivational quote


with open("quotes.txt") as file:
    quotes = file.readlines()

if dt.datetime.today().weekday() == 0: #setup as today first
    quote_to_send = random.choice(quotes)
    send_email(subject="Motivational Monday!", message=quote_to_send, email=my_email, password=my_password)



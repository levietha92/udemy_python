import smtplib
import os
from dotenv import load_dotenv
import time
import math


env_path = "/Users/hanna/GitHub/udemy_course/.env"
load_dotenv(dotenv_path=env_path)
my_email = os.getenv("APP_EMAIL")
my_password = os.getenv("APP_PASSWORD")
to_email = os.getenv("TO_EMAIL")
MY_LAT = float(os.getenv("MY_LAT"))
MY_LONG = float(os.getenv("MY_LONG"))

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    #assuming that this is already local timezone coz im lazy
}

def send_email(subject, message, to_email, password):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #encrypt the mail, transport layer security
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:{subject}\n\n {message}")
        # connection.close()
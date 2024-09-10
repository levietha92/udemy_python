import smtplib
from dotenv import load_dotenv
from twilio.rest import Client
import html
import os

env_path = "/Users/hanna/GitHub/udemy_course/.env"
load_dotenv(dotenv_path=env_path)

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
my_verified_number = os.getenv("MY_VERIFIED_NUMBER")

my_email = os.getenv("APP_EMAIL")
my_password = os.getenv("APP_PASSWORD")
to_email = os.getenv("TO_EMAIL")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)
    
    def send_message(self, to_send_msg):
        message = self.client.messages.create(
            from_='+12568575370',
            to=my_verified_number,
            body=to_send_msg
        )

    def send_email(self, body:str, to_send_dict:dict, password=my_password):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() #encrypt the mail, transport layer security
            connection.login(user=my_email, password=my_password)
            for first_name, email in to_send_dict.items():
                
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject: Hey {first_name}, your FlightDeal today! \n\n {body}"
                )



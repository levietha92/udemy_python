from twilio.rest import Client
import html
import os

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
my_verified_number = os.getenv("MY_VERIFIED_NUMBER")


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


import smtplib
from dotenv import load_dotenv
import os

env_path = "/Users/hanna/GitHub/udemy_course/.env"
load_dotenv(dotenv_path=env_path)

my_email = os.getenv("APP_EMAIL")
password = os.getenv("APP_PASSWORD")
print(my_email,password)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() #encrypt the mail, transport layer security
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="vietha.le92@gmail.com", 
        msg="Subject:hola\n\n This is the body")
    # connection.close()


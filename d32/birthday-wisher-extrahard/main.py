##################### Extra Hard Starting Project ######################
from dotenv import load_dotenv
import datetime as dt
import os
import pandas as pd
import random
import smtplib

#----------------------------------- SET UP -----------------------------------#
env_path = "/Users/hanna/GitHub/udemy_course/.env"
load_dotenv(dotenv_path=env_path)
my_email = os.getenv("APP_EMAIL")
my_password = os.getenv("APP_PASSWORD")
to_email = os.getenv("TO_EMAIL")
print(my_email,my_password)

#----------------------------------- FUNCTIONS -----------------------------------#
def send_email(subject, message, to_email, password):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #encrypt the mail, transport layer security
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:{subject}\n\n {message}")
        # connection.close()

#----------------------------------- SCRIPT -----------------------------------#
# 1. Update the birthdays.csv
bdays = pd.read_csv("birthdays.csv")

# loading templates into a dictionary
template_choices = [1,2,3]
template_paths = [f"letter_templates/letter_{template_choice}.txt" for template_choice in template_choices]
template_contents = []
for path in template_paths:
    with open(path) as file:
        content = file.read()
        template_contents.append(content)
template_contents
template_dict = dict(zip(template_choices, template_contents))
template_dict

# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

dd = dt.datetime.today().date().day
mm = dt.datetime.today().date().month

for index,row in bdays.iterrows():
    random_choice = random.randrange(1,3)
    if dd == row['day'] and mm == row['month']:
        bday_msg = template_dict[random_choice].replace("[NAME]",row['name'])
        print(bday_msg)
        send_email(
            subject=f"Happy birthday {row['name']}!",
            message=bday_msg,
            to_email=row['email'],
            password=my_password
        )


# need to host in the ccloud:: https://www.pythonanywhere.com/
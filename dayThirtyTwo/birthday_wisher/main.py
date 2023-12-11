import os
import random
import smtplib
import datetime as dt
from email.mime.text import MIMEText

import pandas

my_email = "all.junk.mails.my@gmail.com"
password = "jjbw dcrj tzun uydj"
email = "all.junk.mails.my@gmail.com"

birthday = pandas.read_csv("birthdays.csv").to_dict(orient="records")
folder_path = "letter_templates"  # Replace with the actual folder path

# Get a list of all files in the folder
file_list = os.listdir(folder_path)
greeting = random.choice(file_list)
current_month = dt.datetime.now().month
current_day = dt.datetime.now().day

for el in birthday:
    if el["month"] == current_month and el["day"] == current_day:
        content = f"{folder_path}/{greeting}"
        with open(content, "r") as text:
            letter = text.read()
            old_entries = ["[NAME]", "Angela"]
            new_entries = [el["name"], "Alona"]
            new_text = letter
            for old_entry, new_entry in zip(old_entries, new_entries):
                new_text = new_text.replace(old_entry, new_entry)

            msg = MIMEText(new_text)
            msg['Subject'] = 'Birthday Greeting'
            msg['From'] = my_email
            msg['To'] = el['email']

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.send_message(msg)

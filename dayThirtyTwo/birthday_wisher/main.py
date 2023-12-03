import os
import random
import smtplib
import datetime as dt
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
print(birthday)
for el in birthday:
    if el["month"] == current_month and el["day"] == current_day:
        print(f"Its a birthday of {el['name']}")
        print()

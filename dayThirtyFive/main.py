import smtplib
from datetime import datetime, timedelta
from email.message import EmailMessage

import requests

endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "6419269eef1e3c2969a8eb8172cacbb9"
lat = 53.43333
lon = -7.95

my_email = "all.junk.mails.my@gmail.com"
password = "jjbw dcrj tzun uydj"
email = "all.junk.mails.my@gmail.com"

parameters = {
    "lat": lat,
    "lon": lon,
    "appid": API_KEY,
    "units": "metric"
}

general_data = requests.get(url=endpoint, params=parameters)
data = general_data.json()["list"]
date_today = datetime.today().date()
for item in data:
    day = item["dt_txt"].split(" ")
    weather = item["weather"][0]["description"].capitalize()
    if str(day[0]) == str(date_today):
        current_weather = f"We expect {weather} in between {day[1]}"
        if item["weather"][0]["id"] < 700:
            datetime_obj = datetime.strptime(day[1], "%H:%M:%S")

            # Add 3 hours to the datetime object
            new_datetime_obj = datetime_obj + timedelta(hours=3)

            # Extract the time component from the datetime object
            new_time_obj = new_datetime_obj.time()

            # Convert time object back to string
            new_time_str = new_time_obj.strftime("%H:%M:%S")
            rain_notice = f"We expect {weather} in between {day[1]}-{new_time_obj}"
            print(rain_notice)

            msg = EmailMessage()
            msg["Subject"] = "Rain notification"
            msg.set_content(rain_notice)

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.send_message(msg=msg, from_addr=my_email, to_addrs=email)

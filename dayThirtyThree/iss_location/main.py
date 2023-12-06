import smtplib
import time

import requests
from datetime import datetime

MY_LAT = 53.43333
MY_LONG = -7.95
password = "jjbw dcrj tzun uydj"
email = "all.junk.mails.my@gmail.com"

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_data = iss_response.json()
iss_latitude = float(iss_data["iss_position"]["latitude"])
iss_longitude = float(iss_data["iss_position"]["longitude"])


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    current_time = datetime.now().time().hour

    return sunrise <= current_time >= sunset


while True:
    time.sleep(60)
    if (iss_latitude in range(int(MY_LAT) - 5, int(MY_LAT) + 5) or
        iss_longitude in range(int(MY_LONG) - 5, int(MY_LONG) + 5)) and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=email,
                                msg="Subject:ISS is over you\n\nIss station over your head, awake!")

from datetime import datetime, timedelta

import requests

endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "6419269eef1e3c2969a8eb8172cacbb9"
lat = 53.43333
lon = -7.95

parameters = {
    "lat": lat,
    "lon": lon,
    "appid": API_KEY,
    "units": "metric"
}

general_data = requests.get(url=endpoint, params=parameters)
data = general_data.json()["list"]
date_today = datetime.today().date() + timedelta(days=1)
for item in data:
    day = item["dt_txt"].split(" ")
    weather = item["weather"][0]["description"].capitalize()
    if str(day[0]) == str(date_today):
        if "rain" in weather:
            datetime_obj = datetime.strptime(day[1], "%H:%M:%S")

            # Add 3 hours to the datetime object
            new_datetime_obj = datetime_obj + timedelta(hours=3)

            # Extract the time component from the datetime object
            new_time_obj = new_datetime_obj.time()

            # Convert time object back to string
            new_time_str = new_time_obj.strftime("%H:%M:%S")

            print(
                f"We expect {weather} in between {day[1]}-{new_time_obj}")

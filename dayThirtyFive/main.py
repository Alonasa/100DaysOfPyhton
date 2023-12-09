import requests

API_KEY = "6419269eef1e3c2969a8eb8172cacbb9"
lat = 53.43333
lon = -7.95

parameters = {
    "lat": lat,
    "lon": lon,
    "appid": API_KEY,
    "units": "metric"
}

data = requests.get(url="https://api.openweathermap.org/data/2.5/weather?", params=parameters)
print(data.json())

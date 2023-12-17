import requests
from pprint import pprint

BASE_URL = "https://api.sheety.co/1188f4ef2e5889f0a49a02ef057290e9/flightDeals/prices"

get_data = requests.get(url=BASE_URL)

data = get_data.json()

for item in data["prices"]:
    TEQUILA_LOC = f"https://api.tequila.kiwi.com/locations/query?term={item['city']}&locale=en-US&location_types=city&limit=10&active_only=true"
    par = {
        'apikey': 'qi0gKdipdlEG0zFW0Wh5KtiicSpgP_GV'
    }
    get_locations = requests.get(url=TEQUILA_LOC, headers=par)
    locations_data = get_locations.json()
    for location in locations_data["locations"]:
        if item["iataCode"] == "TESTING":
            if location["name"] == item["city"]:
                iataCode = location["code"]
                itemId = item["id"]
                body = {
                    "price": {"iataCode": iataCode}
                }
                header = {
                    "Content-Type": "application/json"
                }

                sent = requests.put(url=f"{BASE_URL}/{itemId}", json=body, headers=header)

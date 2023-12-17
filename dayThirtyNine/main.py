import requests
from pprint import pprint

BASE_URL = "https://api.sheety.co/1188f4ef2e5889f0a49a02ef057290e9/flightDeals/prices"
SEARCH_API_KEY = "bnh49sf_rc5WzYt56jZRvxXx7YOjhv7U"

get_data = requests.get(url=BASE_URL)

data = get_data.json()

datatype_type_sheet = {'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}
par = {
    'apikey': 'qi0gKdipdlEG0zFW0Wh5KtiicSpgP_GV'
}

for item in data["prices"]:
    TEQUILA_LOC = f"https://api.tequila.kiwi.com/locations/query?term={item['city']}&locale=en-US&location_types=city&limit=10&active_only=true"
    get_locations = requests.get(url=TEQUILA_LOC, headers=par)
    locations_data = get_locations.json()
    for location in locations_data["locations"]:
        if item["iataCode"] == "":
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

for item in data["prices"]:
    destination = item["iataCode"]
    url1 = f"https://api.tequila.kiwi.com/v2/search?fly_from=DUB&fly_to={destination}&date_from=18%2F12%2F2023&date_to=18%2F06%2F2024&nights_in_dst_from=7&nights_in_dst_to=28&max_fly_duration=20&ret_from_diff_city=false&ret_to_diff_city=false&one_for_city=1&one_per_date=1&adults=1&selected_cabins=M&only_working_days=false&only_weekends=false&curr=EUR&max_stopovers=0&max_sector_stopovers=0&vehicle_type=aircraft&limit=500"

    par = {
        "apikey": SEARCH_API_KEY,
        "fly_from": "DUB"
    }
    flight_finder = requests.get(url=url1, headers=par)

    response = flight_finder.json()['data']
    is_flight_exists = len(response)
    if is_flight_exists > 0:
        departure = response[0]['route'][0]['utc_departure'].split('T')
        arrival = response[0]['route'][1]['utc_departure'].split('T')
        print(f"{response[0]['cityTo']} {departure[0]}-{arrival[0]}: Є{response[0]['price']}")
    else:
        print(f"Theres no direct flights from Dublin to {destination}")

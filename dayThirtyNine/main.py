import requests
from pprint import pprint
import json
from io import StringIO

BASE_URL = "https://api.sheety.co/1188f4ef2e5889f0a49a02ef057290e9/flightDeals/prices"

get_data = requests.get(url=BASE_URL)

data = get_data.json()
for item in data['prices']:
    if item['iataCode'] == '':
        itemId = item['id']

        body = {
            "price": {"iataCode": "TESTING"}
        }

        header = {
            "Content-Type": "application/json"
        }

        sent = requests.put(url=f"{BASE_URL}/{itemId}", json=body, headers=header)

import requests
from pprint import pprint

fetch = requests.get(url="https://api.sheety.co/1188f4ef2e5889f0a49a02ef057290e9/flightDeals/prices")

data = fetch.json()['prices']
for item in data:
    if item['iataCode'] == '':
        item['iataCode'] = 'TESTING'
pprint(data)

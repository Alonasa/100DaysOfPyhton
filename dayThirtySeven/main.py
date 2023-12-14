from datetime import datetime

import requests

USERNAME = "alona"
TOKEN = "alonecoder25"
GRAPH_ID = "graph"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Tasks",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime(year=2023, month=12, day=13)
today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5",
}

create_response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

pixel_update = {
    "quantity": "5"
}

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_response = requests.put(url=update_endpoint, json=pixel_update, headers=headers)
print(update_response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
delete_response = requests.delete(url=update_endpoint, headers=headers)
print(delete_response.text)

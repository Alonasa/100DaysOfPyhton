import requests

pixela_endpoint = "https://pixe.la/v1/users"
params = {
    "token": "alonecoder25",
    "username": "alona",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=params)

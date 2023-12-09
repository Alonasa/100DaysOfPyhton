import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
data = response.json()
if data["response_code"] == 0:
    question_data = data["results"]

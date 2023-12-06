import requests

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
data = response.json()
if data["response_code"] == 0:
    question_data = data["results"]

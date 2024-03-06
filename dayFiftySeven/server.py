from datetime import datetime

import requests
from flask import Flask, render_template

app = Flask(__name__)
year = datetime.now().year


@app.route("/")
def main():
    return render_template("index.html", year=year)


@app.route("/<username>")
def show_data(username):
    get_data = requests.get(f"https://api.agify.io?name={username}").json()
    gender_data = requests.get(f"https://api.genderize.io?name={username}").json()
    age = get_data["age"]
    gender = gender_data["gender"]
    return render_template("index.html", name=username, age=age, gender=gender, year=year)


if __name__ == "__main__":
    app.run(debug=True, port=3000)

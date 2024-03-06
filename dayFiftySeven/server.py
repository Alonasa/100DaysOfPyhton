from datetime import datetime

import requests
from flask import Flask, render_template

app = Flask(__name__)
year = datetime.now().year
posts = requests.get("https://api.npoint.io/08afc6f266b78ea0dd46").json()


@app.route("/")
def main():
    return render_template("index.html", year=year, posts=posts)


@app.route("/users/<username>")
def show_data(username):
    get_data = requests.get(f"https://api.agify.io?name={username}").json()
    gender_data = requests.get(f"https://api.genderize.io?name={username}").json()
    age = get_data["age"]
    gender = gender_data["gender"]
    return render_template("user.html", name=username, age=age, gender=gender, year=year)


@app.route("/blog/<int:post_id>")
def show_post(post_id):
    post = None
    for p in posts:
        if p["id"] == post_id:
            post = p
            break
    if post is None:
        return "Post not found"
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True, port=3000)

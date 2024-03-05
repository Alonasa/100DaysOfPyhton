from datetime import datetime

from flask import Flask, render_template, request

app = Flask(__name__)
year = datetime.now().year


def get_name():
    if request.method == "POST":
        name = request.form.get('name')
        return name


def get_click():
    return 'Get click on button'


@app.route("/")
def main():
    return render_template("index.html", year=year)


@app.route("/<username>")
def show_data(username):
    return render_template("index.html", name=username, year=year)


if __name__ == "__main__":
    app.run(debug=True, port=3000)

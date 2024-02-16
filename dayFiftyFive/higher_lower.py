import random

from flask import Flask

app = Flask(__name__)

random_number = random.randint(0, 9)


@app.route("/")
def title():
    return "<div style='text-align: center; width: 50%; display: flex; flex-direction: column; align-items: center'>" \
           "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>" \
           "</div>"


@app.route("/<int:val>")
def user_input(val):
    if val < random_number:
        return "<h1 style='color: red'>Number is too low</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif val > random_number:
        return "<h1 style='color: red'>Number is too high</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1 style='color: green'>YOU ARE RIGHT</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)

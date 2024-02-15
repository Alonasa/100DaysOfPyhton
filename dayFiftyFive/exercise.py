from flask import Flask

app = Flask(__name__)


def returner(func, tag):
    def wrapper(*args, **kwargs):
        return f"<{tag}>{func(*args, **kwargs)}</{tag}>"

    return wrapper


def bold(func):
    return returner(func, 'b')


def italic(func):
    return returner(func, 'i')


def underlined(func):
    return returner(func, 'u')


@app.route("/")
@bold
@italic
@underlined
def main():
    text = "<h1 style='text-align: center'>Welcome to the main page</h1>"
    return text


@app.route("/user/<name>")
def greet_user(name):
    return f"Hello, {name.capitalize()}!!!"


if __name__ == "__main__":
    app.run(debug=True)

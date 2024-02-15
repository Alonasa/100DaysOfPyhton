from flask import Flask

app = Flask(__name__)


@app.route("/")
def title():
    return "<div style='text-align: center; width: 50%; display: flex; flex-direction: column; align-items: center'>" \
           "<h1>Guess a number between 0 and 9</h1>" \
           "<input style='margin-bottom: 25px' value='' type='number'>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>" \
           "</div>"


if __name__ == "__main__":
    app.run(debug=True)

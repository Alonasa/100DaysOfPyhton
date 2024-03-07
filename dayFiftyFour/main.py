import time
from functools import wraps

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>My first server</h1>'


def person_function(func):
    @wraps(func)
    def person_decorator(*args, **kwargs):
        print('I am a robot')
        time.sleep(2)
        return func(*args, **kwargs)

    return person_decorator


@app.route('/bot')
@person_function
def bot():
    message = 'I am a bot'
    return message


@app.route('/yo')
@person_function
def person_skills():
    message = 'I know Python, JS, HTML, CSS'
    print(message)
    return message


if __name__ == "__main__":
    app.run()

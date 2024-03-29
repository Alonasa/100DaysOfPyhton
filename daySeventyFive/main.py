from flask import Flask

app = Flask()


@app.route('/')
def main():
    pass


if __name__ == "main":
    app.run(port=3000, debug=True)

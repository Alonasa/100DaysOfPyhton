import smtplib

from flask import Flask, render_template, request

app = Flask(__name__)

my_email = "all.junk.mails.my@gmail.com"
password = "jjbw dcrj tzun uydj"
email = "all.junk.mails.my@gmail.com"


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/send-request")
def open_form():
    return render_template("send-request.html")


@app.route("/send-form", methods=["POST", "GET"])
def send_form():
    if request.method == "POST":
        name = request.form["contact-form__name"].strip()
        mail = request.form["contact-form__email"].strip()
        message = request.form["contact-form__message"].strip()

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg=f"Subject: You received new message from {mail}, "
                                    f"Content: Name - {name} message - {message}")

        return '<h1>Successfully sent your message</h1>'


if __name__ == "__main__":
    app.run(debug=True, port=3010)

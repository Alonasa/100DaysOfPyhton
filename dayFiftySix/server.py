import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import Flask, render_template, request

app = Flask(__name__)

my_email = "all.junk.mails.my@gmail.com"
password = "jjbw dcrj tzun uydj"
email = "all.junk.mails.my@gmail.com"
year = datetime.now().year


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
        message_content = f"You just received new request from {mail}\n\n Message: {message}"

        msg = MIMEMultipart()
        msg["From"] = mail
        msg["To"] = my_email
        msg["Subject"] = f"You received new request from {name}"

        # Create the message content part
        text_part = MIMEText(message_content, "plain")

        # Attach the message content part to the email
        msg.attach(text_part)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.send_message(msg)

        return render_template('thank-you.html',
                               title="Successfully sent your message",
                               link="/",
                               link_text="Go to main page",
                               year=year,
                               domain="https://github.com/Alonasa/aportfolio")


if __name__ == "__main__":
    app.run(debug=True, port=3010)

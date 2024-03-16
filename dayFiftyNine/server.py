import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Text, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask import Markup

app = Flask(__name__)
posts_api = "https://api.npoint.io/2241ceff81d5eee97ca6"
all_posts = requests.get(posts_api).json()

my_email = "all.junk.mails.my@gmail.com"
password = "jjbw dcrj tzun uydj"
email = "all.junk.mails.my@gmail.com"


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


def posts_list():
    get_posts = db.session.execute(db.select(BlogPost))
    posts = get_posts.scalars().all()
    return posts


@app.route("/")
def build_main():
    posts = posts_list()
    return render_template("index.html", posts=posts)


@app.route("/about")
def build_about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def build_contact():
    if request.method == "POST":
        try:
            name = request.form["name"].strip()
            e_mail = request.form["email"].strip()
            phone = request.form["phone"].strip()
            message = request.form["message"].strip()
            message_content = f"Name: {name}\nEmail: {e_mail}\nPhone: {phone}\nMessage: {message}"

            msg = MIMEMultipart()
            msg["From"] = e_mail
            msg["To"] = my_email
            msg["Subject"] = e_mail

            text = MIMEText(message_content, "plain")
            msg.attach(text)

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.send_message(msg)

            return render_template("thank-you.html", title="Form submission successful!",
                                   description="We received your form and will answer soon")
        except smtplib.SMTPException as e:
            # Handle SMTP-related exceptions
            return render_template("contact.html", title="Error sending email: " + str(e),
                                   description="Failed to send your email, Please try again later", error=True)
        except Exception as e:
            # Handle other exceptions
            return render_template("contact.html", title="An error occurred: " + str(e),
                                   description="We have a technical issues. Please try again later", error=True)

    return render_template("contact.html")


@app.route("/posts/post/<int:post_id>")
def build_post(post_id):
    posts = posts_list()
    translator = Markup
    return render_template("post.html", posts=posts, id=post_id, translator=translator)


if __name__ == "__main__":
    app.run(port=3000, debug=True)

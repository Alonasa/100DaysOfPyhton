import os
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_ckeditor import CKEditor, CKEditorField
from markupsafe import Markup
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, Text, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import StringField, URLField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
posts_api = "https://api.npoint.io/2241ceff81d5eee97ca6"
all_posts = requests.get(posts_api).json()
app.config['SECRET_KEY'] = os.urandom(32)
Bootstrap(app)
ckeditor = CKEditor(app)

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

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


def posts_list():
    get_posts = db.session.execute(db.select(BlogPost))
    posts = get_posts.scalars().all()
    return posts


class AddPostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = URLField("Blog Image URL", validators=[DataRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired()], _translations='en')
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    name = StringField("Your Name", validators=[DataRequired(), Length(min=2)])
    email = EmailField("Your Email", validators=[DataRequired()])
    password = PasswordField("Your Passwords", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Register", render_kw={"class": "btn-primary btn-sm mt-3"})


class LoginForm(FlaskForm):
    email = EmailField("Your Email", validators=[DataRequired()])
    password = PasswordField("Your Passwords", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Register")


@app.context_processor
def inject_year():
    current_year = datetime.now().year
    return {'current_year': current_year}


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


@app.route("/new-post", methods=["GET", "POST"])
def create_post():
    form = AddPostForm()
    validation = form.validate_on_submit()
    if validation:
        new_post = BlogPost(
            title=form.title.data.capitalize(),
            subtitle=form.subtitle.data.capitalize(),
            date=datetime.now().strftime("%B %d, %Y"),
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data
        )
        db.session.add(new_post)
        db.session.commit()
        flash("New Post Added")
        return redirect(url_for('build_main'))

    return render_template("add.html", form=form, is_edit=False)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    db_post = db.get_or_404(BlogPost, post_id)
    form = AddPostForm(obj=db_post)

    if form.validate_on_submit():
        if form.data != form.data.get("_obj"):  # Check if the form data has changed
            form.populate_obj(db_post)  # Update fields of db_post with form data
            db.session.commit()  # Save changes to the database
            flash("Fields have been changed!", "success")
        else:
            flash("No changes were made.", "info")
        return redirect(url_for("view_post", post_id=post_id))

    return render_template("add.html", form=form, is_edit=True)


@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)

    if post:
        db.session.delete(post)
        db.session.commit()
        flash("Post Deleted Successfully")
        return redirect(url_for('build_main'))
    else:
        flash("Post not found")
        return redirect(url_for('build_main'))


@app.route("/login")
def login():
    pass


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(
            username=request.form.get("name"),
            email=request.form.get("email"),
            password=request.form.get("password")
        )
        db.session.add(new_user)
        db.session.commit()
        flash("New User Has Added")
        redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/logout")
def logout():
    pass


if __name__ == "__main__":
    app.run(port=3000, debug=True)

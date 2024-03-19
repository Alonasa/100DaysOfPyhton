import os

from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(36)
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form_email = request.form.get("email")
    user = db.session.execute(db.select(User).where(User.email == form_email))

    if request.method == "POST":
        new_user = User(
            email=request.form.get("email"),
            password=generate_password_hash(password=request.form.get("password"), method="pbkdf2", salt_length=8),
            name=request.form.get("name")
        )

        if user:
            return render_template("login.html", message="You've already signed with this email. Please sign-in "
                                                         "instead")
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)

        flash("New User Is Added")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form_password = request.form.get("password")
    form_email = request.form.get("email")
    data = db.session.execute(db.select(User))
    data_list = data.scalars().all()

    if len(data_list) == 0:
        return render_template("register.html")

    user = db.session.execute(db.select(User).where(User.email == form_email))
    data = user.scalar()

    if form_email is None and form_password is None:
        return render_template("login.html")

    if check_password_hash(data.password, form_password):
        login_user(data, remember=True)
        return redirect(url_for("secrets"))
    else:
        flash("Wrong fields. Please check your email and password")

    return render_template("login.html", message="Wrong fields. Please check your email and password")


@app.route("/secrets")
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/download")
@login_required
def download():
    return send_from_directory(directory="static", path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)

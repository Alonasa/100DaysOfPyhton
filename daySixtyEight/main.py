from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE IN DB
class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        new_user = User(
            email=request.form.get("email"),
            password=generate_password_hash(password=request.form.get("password"), method='scrypt', salt_length=16),
            name=request.form.get("name")
        )
        db.session.add(new_user)
        db.session.commit()
        flash("New User Is Added")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    data = db.session.execute(db.select(User))
    data_list = data.scalars().all()

    form_password = request.form.get("password")
    form_email = request.form.get("email")

    if len(data_list) == 0:
        return render_template("register.html")

    if form_email is None and form_password is None:
        return render_template("login.html")

    for item in data_list:
        password = item.password
        email = item.email

        if email == form_email and password == form_password:
            return render_template("secrets.html", name=item.name.capitalize())
        else:
            flash("Wrong fields. Please check your email and password")

    flash("Wrong credentials. Please check your email and password")
    return render_template("login.html")


# @app.route('/login', methods=["GET", "POST"])
# def login():
#     data = db.session.execute(db.select(User))
#     data_list = data.scalars().all()
#
#     form_password = request.form.get("password")
#     form_email = request.form.get("email")
#
#     if not data_list:
#         return redirect(url_for("register"))
#     else:
#         for item in data_list:
#             password = item.password
#             email = item.email
#
#             if email == form_email and password == form_password:
#                 flash("We find you in our system")
#                 return render_template("secrets.html", name=item.name.capitalize())
#             else:
#                 flash("Wrong fields, Please check your email and password")
#                 return redirect(url_for("login"))
#
#     return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory(directory='static', path='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)

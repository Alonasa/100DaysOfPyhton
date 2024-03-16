import os
import random

from flask import Flask, jsonify, render_template, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from werkzeug.exceptions import NotFound
from wtforms import StringField, BooleanField, URLField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


def get_cafes_from_db():
    get_cafes = db.session.execute(db.select(Cafe))
    cafes = get_cafes.scalars().all()
    return cafes


class AddCafeForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=250)],
                       render_kw={"placeholder": "Caffe name"})
    map_url = URLField("Map Url", validators=[DataRequired(), Length(min=2, max=500)],
                       render_kw={"placeholder": "Google maps URL"})
    img_url = URLField("Img Url", validators=[DataRequired(), Length(min=2, max=500)],
                       render_kw={"placeholder": "Photo Url"})
    location = StringField("Location", validators=[DataRequired(), Length(min=2, max=250)],
                           render_kw={"placeholder": "Location"})
    seats = StringField("Seats", validators=[DataRequired(), Length(min=1, max=250)],
                        render_kw={"placeholder": "Seats available"})
    has_toilet = BooleanField("Has Toilet", false_values=(False, "false", ""))
    has_wifi = BooleanField("Has Wi-Fi", false_values=(False, "false", ""))
    has_sockets = BooleanField("Has Sockets", false_values=(False, "false", ""))
    can_take_calls = BooleanField("Accept Calls", false_values=(False, "false", ""))
    coffee_price = StringField("Coffe Price", validators=[DataRequired(), Length(min=2, max=250)],
                               render_kw={"placeholder": "Coffe Price from"})
    submit = SubmitField("Add Cafe")


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    cafes = get_cafes_from_db()
    cafe = random.choice(cafes)
    cafe = cafe.to_dict()
    jsonified_cafe = jsonify(cafe=cafe)
    return jsonified_cafe


@app.route("/all")
def all_cafes():
    cafes = get_cafes_from_db()
    cafes_obj = {"cafes": []}
    for cafe in cafes:
        nested = cafe.to_dict()
        cafes_obj["cafes"].append(nested)
    return jsonify(cafes_obj)


@app.route("/search/")
def find_cafe():
    query_loc = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_loc))
    get_cafes = result.scalars().all()

    if get_cafes:
        cafes_json = [cafe.to_dict() for cafe in get_cafes]
        return jsonify(cafes_json)
    else:
        return jsonify(error={"Not found": "Sorry, we don't have a cafe at that location."}), 404

        # HTTP POST - Create Record


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddCafeForm()
    validation = form.validate_on_submit()
    if validation:
        cafe = Cafe(
            name=request.form["name"],
            map_url=request.form["map_url"],
            img_url=request.form["img_url"],
            location=request.form["location"],
            seats=request.form["seats"],
            has_toilet=bool(request.form.get("has_toilet", False)),
            has_wifi=bool(request.form.get("has_wifi", False)),
            has_sockets=bool(request.form.get("has_sockets", False)),
            can_take_calls=bool(request.form.get("can_take_calls", False)),
            coffee_price=request.form["coffee_price"])
        db.session.add(cafe)
        db.session.commit()

        success_response = jsonify(response={"success": "Successfully added the new cafe."})
        return success_response

    return render_template("add.html", form=form)


# HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    new_price = request.args.get("price")

    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})


# HTTP DELETE - Delete Record


@app.route("/report-closed/<int:cafe_id>")
def close(cafe_id):
    top_secret_api = "my_secret_key"
    secret_key = request.args.get("api-key")

    try:
        cafe = db.get_or_404(Cafe, cafe_id)
        if top_secret_api == secret_key:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify({"success": "Cafe closed successfully."})
        else:
            return jsonify({"error": "Sorry, that's not allowed. Make sure that you have the correct API-Key!"})
    except NotFound:
        return jsonify({"error": f"Cafe with ID not found in the database."})


if __name__ == "__main__":
    app.run(debug=True)

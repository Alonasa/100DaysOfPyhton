import random
from flask import Flask, jsonify, render_template, request, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
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


with app.app_context():
    db.create_all()


def get_cafes_from_db():
    get_cafes = db.session.execute(db.select(Cafe))
    cafes = get_cafes.scalars().all()
    return cafes


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    cafes = get_cafes_from_db()
    cafe = random.choice(cafes)
    jsonified_cafe = jsonify(cafe={"id":             cafe.id,
                                   "name":           cafe.name,
                                   "map_url":        cafe.map_url,
                                   "img_url":        cafe.img_url,
                                   "location":       cafe.location,
                                   "seats":          cafe.seats,
                                   "has_toilet":     cafe.has_toilet,
                                   "has_wifi":       cafe.has_wifi,
                                   "has_sockets":    cafe.has_sockets,
                                   "can_take_calls": cafe.can_take_calls,
                                   "coffee_price":   cafe.coffee_price})
    return jsonified_cafe


@app.route("/all")
def all_cafes():
    cafes = get_cafes_from_db()
    cafes_obj = {"cafes": []}
    for cafe in cafes:
        nested = {"id":             cafe.id,
                  "name":           cafe.name,
                  "map_url":        cafe.map_url,
                  "img_url":        cafe.img_url,
                  "location":       cafe.location,
                  "seats":          cafe.seats,
                  "has_toilet":     cafe.has_toilet,
                  "has_wifi":       cafe.has_wifi,
                  "has_sockets":    cafe.has_sockets,
                  "can_take_calls": cafe.can_take_calls,
                  "coffee_price":   cafe.coffee_price}

        cafes_obj["cafes"].append(nested)
    return jsonify(cafes_obj)

    # HTTP POST - Create Record

    # HTTP PUT/PATCH - Update Record

    # HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)

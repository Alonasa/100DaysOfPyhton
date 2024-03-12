from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, URLField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy()
db.init_app(app)


class Movie(db.Model):
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(250), unique=True, nullable=False)
    year = db.Column(Integer, nullable=False)
    description = db.Column(String(250), nullable=False)
    rating = db.Column(Float, nullable=False)
    ranking = db.Column(Integer, nullable=False)
    review = db.Column(String(250), nullable=False)
    img_url = db.Column(String(250), nullable=False)


with app.app_context():
    db.create_all()

# CREATE TABLE

new_movie = Movie(
    title='Phone Booth',
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review='My favourite character was the caller.',
    img_url='https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg'
)


class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()], render_kw={'placeholder': 'Movie title'})
    year = IntegerField('Year', validators=[DataRequired()], render_kw={'placeholder': 'Year of production'})
    description = StringField('Movie Description', validators=[DataRequired()], render_kw={'placeholder': 'Movie '
                                                                                                          'description'})
    rating = IntegerField('Movie Rating', validators=[DataRequired()],
                          render_kw={'placeholder': 'Movie rating', 'value': 1.0, 'min': 1.0, 'max': 10.0, 'step': 0.1})
    ranking = IntegerField('Rank Of The Movie', validators=[DataRequired()], render_kw={'placeholder': 'Rank of '
                                                                                                       'movie'})
    review = StringField('Your Review', validators=[DataRequired()], render_kw={'placeholder': 'Your review'})
    img_url = URLField('Img URL', validators=[DataRequired()], render_kw={'placeholder': 'Add valid url for image'})
    submit = SubmitField('Add Movie')


@app.route('/')
def home():
    result = db.session.execute(db.select(Movie))
    all_movies = result.scalars().all()
    return render_template('index.html', movies=all_movies)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    validation = form.validate_on_submit()
    if request.method == 'POST' and validation:
        movie = Movie(title=request.form['title'].strip().capitalize(),
                      year=request.form['year'].strip(),
                      description=request.form['description'].strip(),
                      rating=request.form['rating'].strip(),
                      ranking=request.form['ranking'].strip(),
                      review=request.form['review'].strip(),
                      img_url=request.form['img_url'].strip())
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html', form=form)


@app.route('/update')
def update():
    pass


@app.route('/delete')
def delete():
    pass


if __name__ == '__main__':
    app.run(debug=True, port=3000)

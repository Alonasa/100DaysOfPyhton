from datetime import datetime

import requests
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, FloatField, IntegerField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
base_url = 'https://api.themoviedb.org/3/'
api_key = '352ac6a4ded4ca0c8fc24094e857dd60'
headers = {
    "accept":        "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9."
                     "eyJhdWQiOiIzNTJhYzZhNGRlZDRjYTBjOGZjMjQwOTRlODU3ZGQ2MCIsInN1YiI6Ij"
                     "Y1ZjIwNjQ0ZDY0YWMyMDE0YjVkOWJlNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2Z"
                     "XJzaW9uIjoxfQ.M-ZTqF8IPDstAChrGIfXJZDseUFCCDMCZNgj5Wd1p-k"
}

Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy()
db.init_app(app)


class Movie(db.Model):
    id = db.Column(Integer, primary_key=True)
    source_id = db.Column(Integer, unique=True)
    title = db.Column(String(250), nullable=False)
    year = db.Column(Integer, nullable=False)
    description = db.Column(String(2000), nullable=False)
    rating = db.Column(Float, nullable=False)
    ranking = db.Column(Integer, nullable=False)
    review = db.Column(String(500), nullable=False)
    img_url = db.Column(String(250), nullable=False)


with app.app_context():
    db.create_all()


class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()], render_kw={'placeholder': 'Movie title'})
    year = IntegerField('Year', validators=[DataRequired(), NumberRange(min=1900, max=datetime.now().year)], render_kw={
        'placeholder': 'Year of production'})
    description = StringField('Movie Description', validators=[DataRequired()],
                              render_kw={'placeholder': 'Movie description'})
    rating = FloatField('Movie Rating', validators=[DataRequired(), NumberRange(min=1.0, max=10.0)],
                        render_kw={'placeholder': 'Movie rating', 'value': 1.0})
    ranking = IntegerField('Rank Of The Movie', validators=[DataRequired()], render_kw={'placeholder': 'Rank of '
                                                                                                       'movie'})
    review = StringField('Your Review', validators=[DataRequired()], render_kw={'placeholder': 'Your review'})
    img_url = URLField('Img URL', validators=[DataRequired()], render_kw={'placeholder': 'Add valid url for image'})
    submit = SubmitField('Add Movie')


class EditMovieForm(FlaskForm):
    rating = FloatField('Your Rating out of 10 e.g. 5.2', validators=[NumberRange(min=1.0, max=10.0)],
                        render_kw={'placeholder': 'New rating', 'value': 1.0, 'min': 1.0, 'max': 10.0, 'step': 0.1})
    review = StringField('Your Review', validators=[DataRequired()], render_kw={'placeholder': 'Your review'})
    submit = SubmitField('Change')


class FindMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()], render_kw={'placeholder': 'Movie title'})
    submit = SubmitField('Add Movie')


@app.route('/')
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
    all_movies = result.scalars().all()

    length = len(all_movies)
    for i in range(length):
        all_movies[i].ranking = i + 1
    db.session.commit()

    return render_template('index.html', movies=all_movies)


def get_movies(title):
    url = f'{base_url}search/movie?query={title}&include_adult=true&language=en-US&page=1'

    movies = requests.get(url, headers=headers)
    return movies


@app.route('/find')
def find():
    movie_id = request.args.get('id')
    movie_url = f'{base_url}movie/{movie_id}'
    pic_url = 'https://image.tmdb.org/t/p/w500'

    movie = requests.get(movie_url, headers=headers).json()
    release_year = int(movie["release_date"].split('-')[0])

    try:
        movie = Movie(title=movie['original_title'],
                      source_id=movie_id,
                      year=release_year,
                      description=movie['overview'],
                      rating=1.0,
                      review='review',
                      ranking=1,
                      img_url=f"{pic_url}{movie['poster_path']}")
        db.session.add(movie)
        db.session.commit()
    except IntegrityError:
        return redirect(url_for('add', title="You can't add the same movie twice"))

    return redirect(url_for('update', id=movie.id))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = FindMovieForm()
    validation = form.validate_on_submit()
    title = request.args.get('title')
    if validation:
        movies_raw = get_movies(form.title.data).json()
        movies = movies_raw['results']
        return render_template('select.html', movies=movies)
    if title:
        return render_template('select.html', title=title)

    return render_template('add.html', form=form)


@app.route('/update', methods=['GET', 'POST'])
def update():
    form = EditMovieForm()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    validation = form.validate_on_submit()

    if request.method == 'POST' and validation:
        movie.rating = form.rating.data
        movie.review = request.form['review'].strip()
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", movie=movie, form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=3000)

from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, URLField, FloatField
from wtforms.validators import DataRequired, NumberRange

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
    img_url = URLField('Img URL', validators=[DataRequired()], render_kw={'placeholder': 'Add valid url for image'})
    submit = SubmitField('Change')


@app.route('/')
def home():
    result = db.session.execute(db.select(Movie))
    all_movies = result.scalars().all()
    return render_template('index.html', movies=all_movies)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    validation = form.validate_on_submit()
    if validation:
        movie = Movie(title=request.form['title'].strip().capitalize(),
                      year=request.form['year'].strip(),
                      description=request.form['description'].strip(),
                      rating=request.form['rating'],
                      ranking=request.form['ranking'].strip(),
                      review=request.form['review'].strip(),
                      img_url=request.form['img_url'].strip())
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('home'))

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
        movie.img_url = request.form['img_url'].strip()
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

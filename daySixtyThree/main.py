import os
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, String, Float, func
from sqlalchemy.orm import DeclarativeBase
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(64)
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-book-collection.db"
db = SQLAlchemy()
db.init_app(app)


class Book(db.Model):
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(250), unique=True, nullable=False)
    author = db.Column(String(250), nullable=False)
    rating = db.Column(Float, nullable=False)


with app.app_context():
    db.create_all()


class AddBookForm(FlaskForm):
    title = StringField('Book Name', validators=[DataRequired()], render_kw={
        "placeholder": "Book name e.g. Harry Potter"})
    author = StringField('Book Author', validators=[DataRequired()], render_kw={
        "placeholder": "Author name e.g. J. K. Rowling"})
    rating = IntegerField('Rating', render_kw={"value": 1.0, "min": 1.0, "max": 10.0, "step": 0.1})
    submit = SubmitField('Add book')


@app.route('/')
def home():
    result = db.session.query(Book).order_by(Book.title).all()
    record_count = db.session.query(func.count()).select_from(Book).scalar()
    if record_count > 0:
        return render_template('index.html', books=result)

    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddBookForm()
    validation = form.validate_on_submit()
    if request.method == 'POST' and validation:
        new_book = Book(title=request.form['title'].strip().capitalize(),
                        author=request.form['author'].strip().capitalize(), rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(port=5000, debug=True)

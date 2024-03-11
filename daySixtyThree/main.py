import os
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, String, Float, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(64)
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()

all_books = []


class AddBookForm(FlaskForm):
    book = StringField('Book Name', validators=[DataRequired()], render_kw={
        "placeholder": "Book name e.g. Harry Potter"})
    author = StringField('Book Author', validators=[DataRequired()], render_kw={
        "placeholder": "Author name e.g. J. K. Rowling"})
    rating = FloatField('Rating', validators=[DataRequired(), NumberRange(min=1, max=10)], render_kw={
        "placeholder": "Add your rating from 1 to 10"})
    submit = SubmitField('Add book')


def get_last_db_id():
    engine = create_engine('sqlite:///books-collection.db')  # Replace with your SQLite database file path
    session = sessionmaker(bind=engine)
    session = session()
    last_id = session.query(Book.id).order_by(Book.id.desc()).first()

    last_inserted_id = last_id[0] if last_id else None
    return last_inserted_id


@app.route('/')
def home():
    if len(all_books) > 0:
        for book in all_books:
            return render_template('index.html', book=book)
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddBookForm()
    validation = form.validate_on_submit()
    if request.method == 'POST':
        if validation:
            book = {
                'title':  f"{request.form['book'].strip().capitalize()}",
                'author': f"{request.form['author'].strip().capitalize()}",
                'rating': f"{request.form['rating']}"
            }
            all_books.append(book)
            last_id = get_last_db_id()

            with app.app_context():
                new_book = Book(id=int(last_id) + 1, title=book['title'], author=book['author'], rating=book[
                    'rating'])
                db.session.add(new_book)
                db.session.commit()

            return redirect(url_for('home'))
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(port=5000, debug=True)

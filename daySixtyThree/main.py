import os
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(64)
Bootstrap5(app)

all_books = []


class AddBookForm(FlaskForm):
    book = StringField('Book Name', validators=[DataRequired()], render_kw={
        "placeholder": "Book name e.g. Harry Potter"})
    author = StringField('Book Author', validators=[DataRequired()], render_kw={
        "placeholder": "Author name e.g. J. K. Rowling"})
    rating = IntegerField('Rating', validators=[DataRequired(), NumberRange(min=1, max=10)], render_kw={
        "placeholder": "Add your rating from 1 to 10"})
    submit = SubmitField('Add book')


# min=0, max=10, step=1,
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

            return redirect(url_for('home'))
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(port=5000, debug=True)

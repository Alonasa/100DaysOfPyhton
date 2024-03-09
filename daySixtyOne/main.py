import os

from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def home():
    return render_template('index.html')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    if form.errors:
        return redirect('/denied')
    return render_template('login.html', form=form)


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/denied')
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)

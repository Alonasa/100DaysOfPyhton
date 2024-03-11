from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField, TimeField
from wtforms.validators import DataRequired
import csv

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
CSV_FILE = 'cafe-data.csv'
CUP = '☕'
BICEPS = '💪'
SOCKET = '🔌'


def generate_smiles(smile):
    smiles = []
    for item in range(5):
        smiles.append(smile * (item + 1))
    smiles.append('✘')
    return smiles


cups = generate_smiles(CUP)
biceps = generate_smiles(BICEPS)
power = generate_smiles(SOCKET)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Cafe location on Google Maps URL', validators=[DataRequired(message="That field is required")])
    opening = TimeField('Opening Time e.g 7AM', validators=[DataRequired(message="That field is required")],
                        format='%H:%M')
    closing = TimeField('Closing Time e.g 7PM', validators=[DataRequired()], format='%H:%M')
    rating = SelectField('Coffee Rating', choices=cups, validators=[DataRequired()], validate_choice=True)
    wifi = SelectField('WiFi Strength Rating', choices=biceps, validators=[DataRequired()], validate_choice=True)
    power = SelectField('Power Socket Availability', choices=power, validators=[DataRequired()], validate_choice=True)
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = CafeForm()
    validation = form.validate_on_submit()
    if request.method == 'POST':
        if validation:
            with open(CSV_FILE, 'a', newline='', encoding='utf-8') as csv_file:
                name = request.form['cafe'].strip()
                location = request.form['location'].strip()
                opening = request.form['opening']
                closing = request.form['closing']
                rating = request.form['rating']
                wifi = request.form['wifi']
                power = request.form['power']
                data_row = [name, location, opening, closing, rating, wifi, power]

                writer = csv.writer(csv_file)
                writer.writerow(data_row)

                flash('Cafe added successfully!', 'success')
                return redirect(url_for('cafes'))

                # Exercise:
        if not validation:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'Error in field "{field}": {error}', 'danger')

    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open(CSV_FILE, newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

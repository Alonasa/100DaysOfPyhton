import os

import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = os.environ.get("SEC_KEY")
Bootstrap(app)

colors_data = pd.read_csv('data/colors.csv')
sets_data = pd.read_csv('data/sets.csv')
unique_colors = colors_data['name'].nunique()
transparent_colors = colors_data['is_trans']
amt_transparent = 0
for item in transparent_colors:
    if item == 't':
        amt_transparent += 1
print(unique_colors)
print(amt_transparent)
print(sets_data.head())
get_first_lego_release = sets_data.sort_values('year').head()
years = sets_data.sort_values('year')['year'].drop_duplicates()
print(get_first_lego_release)
print(years)


@app.route('/')
def main_page():
    return render_template('index.html', years=years)


@app.route('/select', methods=['POST'])
def show_data_by_year():
    data = request.form['years']
    return data


if __name__ == "__main__":
    app.run(port=3000, debug=True)

import os

import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, jsonify
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
# print(unique_colors)
# print(amt_transparent)
# print(sets_data.head())
get_first_lego_release = sets_data.sort_values('year').head()
years = sets_data.sort_values('year')['year'].drop_duplicates()
print(get_first_lego_release)
data_by_year = sets_data[sets_data['year'] == 1965]


@app.route('/')
def main_page():
    return render_template('index.html', years=years)


@app.route('/select', methods=['POST'])
def show_data_by_year():
    data = request.form['years']
    data_by_year = sets_data[sets_data['year'] == int(data)]
    unify_data = data_by_year.to_dict()
    ready_data = []
    for key in unify_data['theme_id']:
        item = {
            "set_num":   unify_data['set_num'][key],
            "name":      unify_data['name'][key],
            "year":      unify_data['year'][key],
            "theme_id":  unify_data['theme_id'][key],
            "num_parts": unify_data['num_parts'][key]
        }
        ready_data.append(item)
    return render_template('index.html', data=ready_data, years=years)


if __name__ == "__main__":
    app.run(port=3000, debug=True)

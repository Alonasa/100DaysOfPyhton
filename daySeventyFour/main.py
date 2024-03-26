import os

import pandas as pd
import plotly.graph_objects as go
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from plotly.offline import offline

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
    data_filtered = sets_data[sets_data['year'] == int(data)]
    unify_data = data_filtered.to_dict()
    ready_data = []
    for key in unify_data['theme_id']:
        element = {
            "set_num":   unify_data['set_num'][key],
            "name":      unify_data['name'][key],
            "year":      unify_data['year'][key],
            "theme_id":  unify_data['theme_id'][key],
            "num_parts": unify_data['num_parts'][key]
        }
        ready_data.append(element)
    return render_template('index.html', data=ready_data, years=years)


@app.route('/visualize-sets')
def visualize_sets():
    filtered_data = sets_data[sets_data['year'].isin([int(year) for year in years])]
    sets = filtered_data.groupby('year')['year'].value_counts()
    fig = go.Figure(data=go.Scatter(x=sets.index[:-2], y=sets.values[:-2], mode='lines'))

    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Amt Of Parts in Sets Per Year'
    )

    offline.plot(fig, filename='templates/plot.html', auto_open=False)
    return render_template('plot.html')


if __name__ == "__main__":
    app.run(port=3000, debug=True)

import os
import pandas as pd
import plotly.graph_objects as go
import plotly.subplots as sp
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from plotly.offline import offline

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = os.environ.get("SEC_KEY")
Bootstrap(app)

colors_data = pd.read_csv('data/colors.csv')
sets_data = pd.read_csv('data/sets.csv')
themes_data = pd.read_csv('data/themes.csv')
unique_colors = colors_data['name'].nunique()
transparent_colors = colors_data['is_trans']
amt_transparent = 0
for item in transparent_colors:
    if item == 't':
        amt_transparent += 1
get_first_lego_release = sets_data.sort_values('year').head()
years = sets_data.sort_values('year')['year'].drop_duplicates()
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


@app.route('/show-sets')
def visualize_sets():
    filtered_data = sets_data[sets_data['year'].isin([int(year) for year in years])]
    themes = filtered_data.groupby('year').agg({'theme_id': pd.Series.nunique})
    themes.rename(columns={'theme_id': 'nr_themes'}, inplace=True)

    sets = filtered_data.groupby('year')['year'].value_counts()
    indexes = themes.index[:-2]
    themes_by = themes.nr_themes[:-2]

    fig = sp.make_subplots(specs=[[{"secondary_y": True}]])

    trace_1 = go.Scatter(x=indexes, y=themes_by, mode='lines', name='Amt of themes')
    trace_2 = go.Scatter(x=sets.index[:-2], y=sets.values[:-2], mode='lines', name='Amt of sets')

    fig.add_trace(trace_1, secondary_y=False)
    fig.add_trace(trace_2, secondary_y=True)

    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Amt Of Themes',
        yaxis2_title='Amt Of Sets',
        legend=dict(x=0, y=1, xanchor='left', yanchor='top')
    )

    fig.update_yaxes(title_text='Amt Of Themes', secondary_y=False)
    fig.update_yaxes(title_text='Amt Of Sets', secondary_y=True)

    offline.plot(fig, filename='templates/plot.html', auto_open=False)
    return render_template('plot.html')


@app.route('/show-complexity')
def visualize_complexity():
    data = sets_data
    parts_per_set = data.groupby('year').agg({'num_parts': pd.Series.mean})

    scatter = go.Scatter(x=parts_per_set.index[:-2], y=parts_per_set.num_parts[:-2], mode='markers', name='Pieces Per '
                                                                                                          'Set')
    layout = go.Layout(
        title='Pieces per Set',
        xaxis=go.layout.XAxis(title='Year'),
        yaxis=go.layout.YAxis(title='Pieces per set')
    )
    figure = go.Figure(data=[scatter], layout=layout)
    offline.plot(figure, filename='templates/scatter-plot.html', auto_open=False)

    return render_template('scatter-plot.html')


@app.route('/show-themes')
def visualize_themes():
    themes = themes_data
    sets = sets_data
    count_set = sets["theme_id"].value_counts()
    count_set = pd.DataFrame({'id': count_set.index, 'set_count': count_set.values})
    merged_df = pd.merge(count_set, themes, on='id')
    scatter = go.Bar(x=merged_df.name[:10], y=merged_df.set_count[:10], name='Pieces Per '
                                                                             'Set')
    layout = go.Layout(
        title='Pieces per Set',
        xaxis=go.layout.XAxis(title='Name'),
        yaxis=go.layout.YAxis(title='Sets')
    )
    figure = go.Figure(data=[scatter], layout=layout)
    offline.plot(figure, filename='templates/barchart.html', auto_open=False)

    return render_template('barchart.html')


if __name__ == "__main__":
    app.run(port=3000, debug=True)

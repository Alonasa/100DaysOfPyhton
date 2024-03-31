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

# Lego analysis
colors_data = pd.read_csv('data/lego/colors.csv')
sets_data = pd.read_csv('data/lego/sets.csv')
themes_data = pd.read_csv('data/lego/themes.csv')
get_first_lego_release = sets_data.sort_values('year').head()
years = sets_data.sort_values('year')['year'].drop_duplicates()

# Google Trends Bitcoin, Tesla, Unemployment
bitcoin_price = pd.read_csv('data/trends/Daily Bitcoin Price.csv')
bitcoin_search = pd.read_csv('data/trends/Bitcoin Search Trend.csv')

ben_vs_ue = pd.read_csv('data/trends/UE Benefits Search vs UE Rate 2004-20.csv')
tesla_se_vs_pr = pd.read_csv('data/trends/TESLA Search Trend vs Price.csv')
bitcoin_price.dropna(inplace=True)

df_bc_search = pd.DataFrame(bitcoin_search)
df_bc_price = pd.DataFrame(bitcoin_price)
df_tesla = pd.DataFrame(tesla_se_vs_pr)
df_unemployment = pd.DataFrame(ben_vs_ue)

df_bc_search.MONTH = pd.to_datetime(bitcoin_search.MONTH)
df_bc_price.DATE = pd.to_datetime(bitcoin_price.DATE)
df_tesla.MONTH = pd.to_datetime(tesla_se_vs_pr.MONTH)
df_unemployment.MONTH = pd.to_datetime(ben_vs_ue.MONTH)

df_bc_price['DATE'] = pd.to_datetime(df_bc_price['DATE'])
df_bc_monthly = df_bc_price.resample('M', on='DATE').mean()
df_bc_price.set_index('DATE', inplace=True)
resampled_dates = df_bc_monthly.index


# apps = pd.read_csv('data/appStore/apps.csv')
# df_apps = pd.DataFrame(apps)
# print(df_apps)


@app.route('/')
def main_page():
    return render_template('index.html')


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
    return render_template('lego-template.html', data=ready_data, years=years)


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
    scatter = go.Bar(x=merged_df.name[:18], y=merged_df.set_count[:18], name='Show amount of sets')
    layout = go.Layout(
        title='Number of Sets',
        xaxis=go.layout.XAxis(title='Name', tickangle=-20),
        yaxis=go.layout.YAxis(title='Sets')
    )
    figure = go.Figure(data=[scatter], layout=layout)
    offline.plot(figure, filename='templates/barchart.html', auto_open=False)

    return render_template('barchart.html')


@app.route('/lego')
def show_lego():
    return render_template('lego-template.html', years=years)


@app.route('/searches')
def show_searches():
    return render_template('searches-template.html')


@app.route('/tesla')
def visualize_tesla():
    searches = df_tesla['TSLA_WEB_SEARCH']
    prices = df_tesla['TSLA_USD_CLOSE']
    indexes = df_tesla['MONTH']

    fig = sp.make_subplots(specs=[[{"secondary_y": True}]])

    trace_1 = go.Scatter(x=indexes, y=prices, mode='lines', line=dict(width=3), name='Closing Price')
    trace_2 = go.Scatter(x=indexes, y=searches, mode='lines', line=dict(width=3), name='Web Searches')

    fig.add_trace(trace_1, secondary_y=False)
    fig.add_trace(trace_2, secondary_y=True)

    fig.update_layout(
        title={'text': 'Tesla Web Search vs Price', 'x': 0.5, 'font': {'size': 14}},
        xaxis_title='Years',
        yaxis_title='TSLA Stock Price',
        yaxis2_title='Searches Trend',
        legend=dict(x=0, y=0, xanchor='left', yanchor='top')
    )

    fig.update_yaxes(title_text='Closing Prices', secondary_y=False)
    fig.update_yaxes(title_text='Web Searches', secondary_y=True)

    offline.plot(fig, filename='templates/tsla.html', auto_open=False)
    return render_template('tsla.html')


@app.route('/unemployment')
def visualize_unemployment():
    searches = df_unemployment['UE_BENEFITS_WEB_SEARCH']
    rate = df_unemployment['UNRATE']
    indexes = df_unemployment['MONTH']
    date_series = pd.to_datetime(pd.Series(indexes))

    fig = sp.make_subplots(specs=[[{"secondary_y": True}]])

    trace_1 = go.Scatter(x=indexes, y=rate, mode='lines', line=dict(width=3, color='cyan', dash='dash'),
                         name='Unemployment Rate')
    trace_2 = go.Scatter(x=indexes, y=searches, mode='lines', line=dict(width=3, color='purple'), name='Web Searches')

    fig.add_trace(trace_1, secondary_y=False)
    fig.add_trace(trace_2, secondary_y=True)

    fig.update_layout(
        title={'text': 'Monthly Search of "Unemployment Benefits" in the U.S. vs U/E Rate',
               'x':    0.5, 'font': {'size': 14}},
        xaxis_title='Years',
        xaxis=dict(
            tickmode='array',
            tickvals=date_series.dt.year,
            dtick='M1',
            tickformat='%Y',
            ticklabelmode='period'
        ),
        yaxis_title='Unemployment Rate',
        yaxis_color='blue',
        yaxis2_color='purple',
        yaxis2_title='Searches Trend',
        legend=dict(x=1, y=0, xanchor='center', yanchor='top')
    )

    fig.update_yaxes(title_text='Unemployment Rate', secondary_y=False)
    fig.update_yaxes(title_text='Web Searches', secondary_y=True)

    offline.plot(fig, filename='templates/unemployment.html', auto_open=False)
    return render_template('unemployment.html')


@app.route('/bitcoin')
def visualize_bitcoin():
    rate = df_bc_monthly['CLOSE']
    indexes_price = resampled_dates
    indexes_search = df_bc_search['MONTH']
    searches = df_bc_search['BTC_NEWS_SEARCH']

    fig = sp.make_subplots(specs=[[{"secondary_y": True}]])
    trace_1 = go.Scatter(x=indexes_price, y=rate, mode='lines', line=dict(width=3, color='orange', dash='dash'),
                         name='BTC Price')
    trace_2 = go.Scatter(x=indexes_search, y=searches, mode='lines+markers', line=dict(width=3, color='cyan'),
                         name='Search Trends')

    fig.add_trace(trace_1, secondary_y=False)
    fig.add_trace(trace_2, secondary_y=True)

    fig.update_layout(
        title={'text': 'Bitcoin News Search vs Resampled Price',
               'x':    0.5, 'font': {'size': 14}},
        xaxis_title='Years',
        yaxis_title='BTC Price',
        yaxis_color='orange',
        yaxis2_color='cyan',
        yaxis2_title='Search Trend',
        legend=dict(x=1, y=0, xanchor='center', yanchor='top')
    )

    fig.update_yaxes(title_text='Bitcoin Price', secondary_y=False)
    fig.update_yaxes(title_text='Web Searches', secondary_y=True)

    offline.plot(fig, filename='templates/bitcoin.html', auto_open=False)
    return render_template('bitcoin.html')


# @app.route('/apps')
# def visualize_apps():
#     data = df_apps
#     print(data)


if __name__ == "__main__":
    app.run(port=3000, debug=True)

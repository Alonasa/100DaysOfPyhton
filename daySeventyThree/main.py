import pandas as pd

data = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
pd.options.display.float_format = '{:,.2f}'.format

languages = {}


def count_posts():
    counter = data.groupby('TAG').mean(True)
    return counter


popularity = count_posts()

print(popularity)


def create_unique():
    d = data
    unique = d['TAG'].unique()

    for value in unique:
        languages[value] = {}

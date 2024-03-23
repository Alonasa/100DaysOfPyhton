import pandas as pd

pd.options.display.float_format = '{:,.2f}'.format
data = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
data.DATE = pd.to_datetime(data.DATE)
pivoted = data.pivot(index='DATE', columns='TAG', values='POSTS')
pivoted.fillna(0, inplace=True)

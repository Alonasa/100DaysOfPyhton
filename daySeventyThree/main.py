import matplotlib.pyplot as plt
import mplcursors
import pandas as pd

pd.options.display.float_format = '{:,.2f}'.format
data = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
data.DATE = pd.to_datetime(data.DATE)
pivoted = data.pivot(index='DATE', columns='TAG', values='POSTS')
pivoted.fillna(0, inplace=True)

plt.figure(figsize=(13, 13))
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Posts', fontsize=12)
plt.ylim(0, 35000)

for column in pivoted.columns:
    plt.plot(pivoted.index, pivoted[column], label=column)

cursor = mplcursors.cursor(hover=True)


@cursor.connect("add")
def on_add(legend):
    legend.annotation.set_text(legend.artist.get_label())


plt.legend(fontsize=12)
plt.grid(True)
plt.show()

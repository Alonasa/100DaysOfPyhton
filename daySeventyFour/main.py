import pandas as pd

colors_data = pd.read_csv('data/colors.csv')
# pivoted_colors = colors_data.pivot(index='id', columns='rgb', values='name')
print(colors_data)
print(colors_data['name'])
unique_colors = colors_data['rgb'].nunique()
print(unique_colors)

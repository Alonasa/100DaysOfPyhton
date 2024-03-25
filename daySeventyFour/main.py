import pandas as pd

colors_data = pd.read_csv('data/colors.csv')
unique_colors = colors_data['name'].nunique()
transparent_colors = colors_data['is_trans']
amt_transparent = 0
for item in transparent_colors:
    if item == 't':
        amt_transparent += 1
print(unique_colors)
print(amt_transparent)

import pandas

data = pandas.read_csv("squirrel_count.csv")
colors = data["Primary Fur Color"].dropna().tolist()

crazy_squirrels = {}

for color in colors:
    if color != "nan":
        if color in crazy_squirrels:
            crazy_squirrels[color] += 1
        else:
            crazy_squirrels[color] = 0

df = pandas.DataFrame.from_dict(crazy_squirrels, orient='index', columns=['Count'])

# Write the DataFrame to a CSV file
df.to_csv('squirrels_count.csv', index_label='Color')

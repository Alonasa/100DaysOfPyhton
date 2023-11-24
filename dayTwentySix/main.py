import pandas

# TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
decoder = {code.letter: code.code for (idx, code) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

get_name = input("Input your name: ").upper()
encoder = [decoder[le] for le in get_name]
print(encoder)

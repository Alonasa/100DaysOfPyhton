import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
decoder = {code.letter: code.code for (idx, code) in data.iterrows()}

encoder = []
while True:
    try:
        get_name = input("Input your name: ").upper()
        encoder = [decoder[le] for le in get_name]
    except KeyError:
        print("Sorry, name can contain only letters!")

    else:
        print(encoder)
        break

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def crypt(text, shift, action):
    encrypted = ''
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if action == 'e':
                new_idx = index + shift
            else:
                new_idx = index - shift

            extra = new_idx % len(alphabet)
            encrypted += alphabet[extra]

        else:
            encrypted += letter

    print(encrypted)
    return encrypted


def user_direction(direction, text, shift):
    if direction[0].lower() == 'e':
        crypt(text, shift, 'e')
    elif direction[0].lower() == 'd':
        crypt(text, shift, 'd')
    else:
        return print("Sorry, but your request isn't recognised!\nType 'encode' or 'decode'\n")


def to_continue():
    again = True
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    user_direction(direction, text, shift)

    while again:
        question = input(
            "Do you like to make another operation? Type Yes or No ")
        if question[0].lower() == 'y':
            to_continue()
        else:
            print('Goodbye')
            again = False


to_continue()

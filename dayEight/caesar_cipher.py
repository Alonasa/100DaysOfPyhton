alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def encrypt(text, shift):
    encrypted = ''
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            newIdx = index + shift
            if newIdx < len(alphabet):
                encrypted += alphabet[newIdx]
            else:
                extra = newIdx % len(alphabet)
                encrypted += alphabet[extra]

        else:
            encrypted += letter

    print(encrypted)
    return encrypted


def decrypt(text, shift):
    decrypted = ''
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            newIdx = index - shift
            if 0 <= newIdx < len(alphabet):
                decrypted += alphabet[newIdx]
            else:
                extra = newIdx % len(alphabet)
                decrypted += alphabet[extra]
        else:
            decrypted += letter

    print(decrypted)
    return decrypted


def user_direction(direction, text, shift):
    if direction[0].lower() == 'e':
        encrypt(text, shift)
    elif direction[0].lower() == 'd':
        decrypt(text, shift)
    else:
        print("Sorry, but your request isn't recorgnised!")


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
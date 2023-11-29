"""
make simple password generator
"""

# Password Generator Project
import random
from tkinter import messagebox, simpledialog

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    # print("Welcome to the PyPassword Generator!")
    nr_letters = simpledialog.askinteger(title="Letters", prompt="How many letters would you like in your password?\n")
    nr_symbols = simpledialog.askinteger(title="Symbols", prompt="How many symbols would you like?\n")
    nr_numbers = simpledialog.askinteger(title="Numbers", prompt="How many numbers would you like?\n")

    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    password = ''

    for letter in range(int(nr_letters)):
        idx = random.randint(0, len(letters) - 1)
        password += letters[idx]

    for sym in range(nr_symbols):
        idx = random.randint(0, len(symbols) - 1)
        password += symbols[idx]

    for num in range(nr_numbers):
        idx = random.randint(0, len(numbers) - 1)
        password += numbers[idx]

    strong = ''.join(random.sample(password, len(password)))
    messagebox.showinfo(message=f"Your secure password is: {strong}")

    return strong

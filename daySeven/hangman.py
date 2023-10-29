import random
import os
from graphics import graphic
from words import word_list


def pick_word(words):
    """
    (list of strings) -> string
    """
    idx = random.randint(0, len(words) - 1)
    return words[idx]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def title():
    print("\nWelcome to Hangman!!!")
    print("Start guessing letters in the word")


def guess_letter():
    word = pick_word(word_list)
    print(word)
    continue_game = True
    underscores = ['_'] * len(word)
    looses = 0
    while continue_game:
        title()
        print(graphic[looses])
        print(' '.join(underscores))
        found = False
        guess = input('\nGuess a letter ').lower()
        for position in range(len(word)):
            letter = word[position]
            if letter == guess:
                underscores[position] = letter
                found = True

        compare = ''.join([str(item) for item in underscores])

        if compare == word:
            continue_game = False
            print('YOU HAVE WIN')
        if not found:
            if looses < len(graphic) - 2:
                looses += 1
                clear_screen()
            else:
                clear_screen()
                print(graphic[-1])
                print("YOU LOOSE")
                continue_game = False


def play():
    play_again = True
    while play_again:
        guess_letter()
        again = input("Do you like to play again? ")
        if again[0].lower() != 'y':
            play_again = False


play()

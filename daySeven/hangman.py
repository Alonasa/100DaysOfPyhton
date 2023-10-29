import random
import os
import time

words = ['pig', 'dog', 'mouse', 'cat', 'wolf', 'butterfly', 'horse', 'bird', 'cow', 'goat', 'bool', 'ship']

pic1 = """
.____________
|            
|           
|
|
|
|
|
"""

pic2 = """
.____________
|        |    
|           
|
|
|
|
|
"""

pic3 = """
.____________
|        |    
|       (O)  
|
|
|
|
|
"""

pic4 = """
.____________
|        |    
|       (O)  
|        | 
|
|
|
|
"""

pic5 = """
.____________
|        |    
|       (O)  
|        |\ 
|
|
|
|
"""

pic6 = """
.____________
|        |    
|       (O)  
|       /|\ 
|
|
|
|
"""

pic7 = """
.____________
|        |    
|       (O)  
|       /|\ 
|       /
|
|
|
"""

pic8 = """
.____________
|        |    
|       (O)  
|       /|\ 
|       / \ 
|
|
|
"""

grapnic = [pic1, pic2, pic3, pic4, pic5, pic6, pic7, pic8]


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


def guess_letter(words):
    word = pick_word(words)
    continue_game = True
    underscores = ['_'] * len(word)
    looses = 0
    while continue_game:
        title()
        print(grapnic[looses])
        print(' '.join(underscores))
        found = False
        guess = input('\nGuess a letter ').lower()
        for position in range(len(word)):
            letter = word[position]
            if letter == guess:
                underscores[position] = letter
                found = True

        if not found:
            if looses < len(grapnic) - 2:
                looses += 1
                clear_screen()
            else:
                clear_screen()
                print(grapnic[-1])
                print("YOU LOOSE")
                continue_game = False

def play():
    play_again = True
    while play_again:
        guess_letter(words)
        again = input("Do you like to play again? ")
        if again[0].lower() != 'y':
            play_again = False

play()
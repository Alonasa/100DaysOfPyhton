import random

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


def guess_letter(words):
    print('Welcome to Hangman!!!')
    print('Start guessing letters in the word\n')
    word = pick_word(words)
    print(word)
    continue_game = True
    underscores = ['_'] * len(word)
    print(' '.join(underscores))
    looses = 0
    print(grapnic[looses])
    while continue_game:
        letter = input('\nGuess a letter ')
        if letter in word:
            amount_letters = word.count(letter)

            idx = word.index(letter)
            underscores[idx] = letter
            for item in underscores:
                print(item, end='')
        else:
            if looses < len(grapnic)-2:
                looses += 1
                print(grapnic[looses])

            else:
                print(grapnic[-1])
                print("YOU LOOSE")
                continue_game = False


guess_letter(words)

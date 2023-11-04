import os
import random
from graphics import art

MIN_VALUE = 1
MAX_VALUE = 100

wins = 0
loses = 0


def guess_number():
    """
    (int, int) -> None
    """
    global wins
    global loses
    print(f'\033[95m{art}\033[0m')
    number = random.randint(MIN_VALUE, MAX_VALUE)
    attempts = 5

    check_level = True
    while check_level:
        level = input('Choose level, Hard or Easy \n')
        if level.lower() not in ('hard', 'easy'):
            print('Please choose correct level')
        else:
            check_level = False

        if level.lower() == 'easy':
            attempts = 10
        elif level.lower() == 'hard':
            attempts = 5

    while attempts > 0:
        print(f'Guess the number in range {MIN_VALUE} - {MAX_VALUE}')
        guess = int(input('Make a guess:  '))
        try:
            int(guess)
        except ValueError:
            print('Incorrect input, please add valid integer!!!')

        if number == guess:
            print('🎡Congratulations you are Right🎡')
            wins += 1
            return wins
        elif number > guess:
            attempts -= 1
            print('Number is too Low!')
        else:
            attempts -= 1
            print('Number is too High!')

        if attempts == 0:
            loses += 1
            print('Sorry, you are loose😭😭😭')
            return loses
        print(f'Attempts left: {attempts}')


def game_play():
    play_again = True

    while play_again:
        os.system('clear')
        guess_number()
        message = 'You rather Win! ' if wins > loses else 'You rather loose, Sorry!'
        print(f'You WIN: {wins} times {"":>15} You LOOSE: {loses} times\n')
        if wins > loses:
            print(message)
        elif wins == loses:
            print(f'{"You are on the middle":^47}')
        else:
            print(f'{message:>57}')
        again = input('Do you like to play again? N - no or any other key for yes ')
        print('\n')

        if again[0].lower().strip() == 'n':
            play_again = False
            print('Thank you for playing with US!!!')


game_play()

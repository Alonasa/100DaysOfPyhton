from game_data import data
from art import logo, vs
import random

top_score = [0]


def set_topscore(score):
    if top_score[0] < score:
        top_score[0] = score
    return top_score


def get_random(items):
    item = random.randint(0, len(items) - 1)
    return items[item]


def higher_lower():
    counter = 0
    winner = {}
    loose = False
    while not loose:
        print(logo)

        a = get_random(data)
        b = get_random(data)
        if len(winner) > 0:
            a = winner
            
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']} ")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']} ")

        a_or_b = True
        while a_or_b:
            question = input("Who has more followers? Type 'A' or 'B': ")
            if question.lower() not in ('a', 'b'):
                print("Incorrect input. Please decide between 'A' and 'B' ")
            else:
                a_or_b = False

            if a['follower_count'] > b['follower_count']:
                if question.lower() == 'a':
                    counter += 1
                    winner = a
                    print(f"You're right! Current score: {counter}")
                else:
                    set_topscore(counter)
                    print(f"Sorry, that's wrong. Final score: {counter}. Your Top Score {top_score[0]}")
                    loose = True
            elif b['follower_count'] > a['follower_count']:
                if question.lower() == 'b':
                    counter += 1
                    winner = b
                    print(f"You're right! Current score: {counter}")
                else:
                    set_topscore(counter)
                    print(f"Sorry, that's wrong. Final score: {counter}. Your Top Score {top_score[0]}")
                    loose = True


def game_play():
    game_over = False
    higher_lower()
    again = input('Do you like to play again? Press N for no or any other key for continue ')

    if again[0].lower() == 'n':
        game_over = True

    while not game_over:
        game_play()


game_play()

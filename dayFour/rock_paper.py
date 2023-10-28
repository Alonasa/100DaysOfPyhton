'''
Simple rock paper game 
according to knowledges on current lesson
'''
import random

ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

elements = [ROCK, PAPPER, SCISSORS]

computer_choice = random.randint(0, 2)
choice = int(
    input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scisors "))
print(elements[computer_choice])
print(f'\nComputer choose: {computer_choice}')
print(elements[choice])

message = ''
if computer_choice == 0 and choice == 0 or computer_choice == 1 and choice == 1 or computer_choice == 2 and choice == 2:
    message = 'Its a draw'
elif computer_choice == 0 and choice == 2 or computer_choice == 2 and choice == 1:
    message = 'You loose'
else:
    message = 'You win'

print(f'\n{message}')

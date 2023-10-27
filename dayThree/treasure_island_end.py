'''
Treasure Island game
'''

print(
    '''
******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.\nYour mission is to find the tressure.")
answer = input(
    "You're at cross road. Where do you want to go? Type 'Left' or 'Right' ")

if answer.lower() == 'left':
    print("You\'ve come to a lake. There is an island in the middle of the lake")
    lake_ch = input(
        'Type "wait" to wait for a boat. Type "swim" to swim across. ')
    if lake_ch.lower() == "swim":
        print("You get attacked by an angry trout. Game Over.")
    elif lake_ch.lower() == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. ")
        color_ch = input(
            "One red, one yellow and one blue. Which colour do you choose? ")
        if color_ch.lower() == "red":
            print("It's a room full of fire. Game Over.")
        elif color_ch.lower() == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")
else:
    print("You fell into a hole. Game Over.")

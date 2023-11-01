import random
import os
from art import logo

HEARTS = chr(9829)
# Character 9829 is '♥'.
DIAMONDS = chr(9830)
# Character 9830 is '♦'.
SPADES = chr(9824)
# Character 9824 is '♠'.
CLUBS = chr(9827)
# Character 9827 is '♣'.

cards = []

for suit in HEARTS, DIAMONDS, SPADES, CLUBS:
    for rank in range(2, 11):
        cards.append(f"{str(rank)}{suit}")
    for rank in 'K', 'Q', 'A', 'J':
        cards.append(f"{rank}{suit}")
    random.shuffle(cards)


def draw_card(cards_list, is_dealer):
    rows = ['', '', '', '', '', '', '', '', '', '', '']
    if is_dealer:
        print("Dealer:")
    elif not is_dealer:
        print("Player:")
    for card in cards_list:
        leng = len(card)
        if len(card[0]) < 2:
            length = 5 - len(card[0])
        else:
            length = 6 - len(card[0])

        for i in range(11):
            if i == 0 or i == 10:  # Rows 0 and 10 are for top and bottom borders
                rows[i] += ".-----------. "
            elif i == 5:  # Row 5 is for suit
                if leng > 2:
                    rows[i] += f"|{card[2]:^11}| "
                else:
                    rows[i] += f"|{card[1]:^11}| "
            elif i % 4 == 1:  # Odd rows are for card value
                if leng > 2:
                    rows[
                        i] += f"|{card[0:2]:^{length}}{card[0:2]:>{length + 2}} | "
                else:
                    rows[i] += f"|{card[0]:^{length}}{card[0]:>{length + 2}} | "
            else:  # Rest of the rows are blank spaces
                rows[i] += "|           | "

    for row in rows:
        print(row)


player_list = []
dealer_list = []


def get_card(li, amount, dealer):
    for item in range(amount):
        rand = random.choice(cards)
        card = cards.pop(cards.index(rand))
        if dealer:
            dealer_list.append(card)
        else:
            player_list.append(card)
    draw_card(li, dealer)


def deal(amount):
    another = True
    os.system("clear")
    print(logo)
    get_card(player_list, amount, False)
    get_card(dealer_list, amount, True)

    while another:
        deal_more = input("Type 'y' to get another card, type 'n' to pass ")
        if deal_more[0].lower().strip() == 'y':
            get_card(player_list, 1, False)


deal(2)

import os
from art import logo


def make_bids():
    bids = {}
    os.system("clear")
    print(logo)
    make_bid = True
    while make_bid:
        name = input("What's your name? ")
        bid = int(input("What's your bid?: $ "))
        bids[name] = bid
        print(bids)
        bid_request = input("Do you like to make another bid? Yes or No ")
        if bid_request[0].lower() == 'n':
            max_value = max(bids.values())
            max_keys = [key for key, value in bids.items() if value == max_value]
            if len(max_keys) > 1:
                print("The winners: ")
                for i in max_keys:
                    print(f"The winner is {i} with bid {max_value}")
            else:
                print(f"The winner is {max_keys[0]} with bid {max_value}")
            make_bid = False


def start_auction():
    start = True
    while start:
        make_bids()
        another_auction = input("Do you like to start another auction? Y/N ")
        if another_auction[0].lower() == 'n':
            start = False


start_auction()

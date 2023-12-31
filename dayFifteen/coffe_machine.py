import os
import time

from resources import MENU, resources


def get_coins():
    coin_list = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}
    inserted = {}
    while True:
        try:
            for item in coin_list:
                while True:
                    insert = input(f"How many {item}? ")
                    if insert.strip() == "":
                        print("Please enter a valid integer value")
                    elif int(insert) < 0:
                        print("Value cannot be less than zero.")
                    else:
                        inserted[str(coin_list[item])] = int(insert)
                        break
            break
        except ValueError:
            print("Amount must be a full number!!!")

    return inserted


def counter(money):
    """
    (dict of items) -> float
    """
    summ = 0
    for key, value in money.items():
        summ += float(key) * value

    return summ


def check_resources(drink):
    is_enough = []
    print("Checking resources....")
    time.sleep(0.5)
    for key, value in MENU[drink]["ingredients"].items():
        for resource, amount in resources.items():
            if key == resource:
                if amount >= value:
                    resources[resource] -= value
                    is_enough.append(True)
                else:
                    print(f"Sorry, there isn't enough {key} left")
                    is_enough = []
    if len(is_enough) == 3:
        return True


def make_report():
    for key, value in resources.items():
        end = ""
        begin = ""
        if key in ("water", "milk"):
            end = "ml"
        elif key == "coffee":
            end = "g"
        elif key == "money":
            begin = "$"

        print(f"{key.upper()}: {begin}{value}{end}")


def make_coffe(info):
    if info.lower() in MENU:
        price = MENU[info]["cost"]
        if check_resources(info):
            print(f"Price: {price}$")
            while True:
                money = get_coins()
                summ = counter(money)

                if summ == price:
                    resources["money"] += price
                    print(f"Here is your {info.capitalize()}. Enjoy!")
                    break
                elif summ < price:
                    difference = price - summ
                    print(f"You need to insert {round(difference, 2)}")
                    check_continue = input("Press 1 to add more coins or other key to Quit ")
                    if check_continue == '1':
                        while True:
                            extra_coins = get_coins()
                            summ += counter(extra_coins)
                            if summ >= price:
                                resources["money"] += price
                                print(
                                    f"Here is your {info.capitalize()}. Enjoy!"
                                    f"Please take your change {round(abs(summ - price), 2)}")
                                break
                            difference = price - summ
                            print(f"Money insert left {round(difference, 2)}")
                    else:
                        print(f"Please don't forget your change {summ}")
                else:
                    resources["money"] += price
                    print(f"Please take your change {round(abs(summ - price), 2)}!!!")
                    break
    elif info.lower() == "report":
        make_report()
    elif info == "maintenance":
        print(resources)
        for resource in resources:
            amt = int(input(f"Add amount for {'withdraw ' if resource == 'money' else ''}{resource} "))
            if resource == "money":
                resources[resource] -= amt
            else:
                resources[resource] += amt
        print(resources)
        print("Maintenance completed.")
    else:
        print(f"Sorry, wrong input")


def coffe_machine():
    os.system("clear")
    while True:
        info = input("What would you like? (espresso/latte/cappuccino) ").lower()
        if info == "off":
            print("Machine on maintenance")
            break
        else:
            make_coffe(info)


coffe_machine()

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()

coffee = CoffeeMaker()
till = MoneyMachine()


def caffe(drink):
    if my_menu.find_drink(drink):
        for el in my_menu.menu:
            if el.name == drink:
                if coffee.is_resource_sufficient(el):
                    print(f"Price of your drink is ${el.cost}")
                    if till.make_payment(el.cost):
                        coffee.make_coffee(el)
    elif drink == 'report':
        coffee.report()
        till.report()


def barista():
    while True:
        drink = input(f"Please choose your drink from menu {my_menu.get_items()} ").lower().strip()
        if drink == 'off':
            print("Thank you for using our coffee machine!!!")
            return False
        else:
            caffe(drink)


barista()

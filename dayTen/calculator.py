from art import logo
import os


def calculator(first_int, second):
    print(logo)
    if second == False:
        first_int = float(input("\nWhat's the first number?: "))
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ").strip()
    second_int = float(input("What's the next number?: "))
    if operation == '+':
        result = first_int + second_int
    elif operation == '-':
        result = first_int - second_int
    elif operation == '/':
        result = first_int / second_int
    elif operation == '*':
        result = first_int * second_int

    return result


def repeat_calculation():
    calculate_more = True
    while calculate_more:
        result = calculator(0, False)
        repeat = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation: ")
        if repeat[0].lower().strip() == 'y':
            os.system("clear")
            result = calculator(result, True)
        elif repeat[0].lower().strip() == 'n':
            calculator(0)
        else:
            calculate_more = False
        print(result)


repeat_calculation()





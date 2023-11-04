from art import logo
import os


def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b


operations = {
    "*": multiply,
    "+": add,
    "-": subtract,
    "/": divide,
}


print(logo)


def calculator(first_int, second):
    if not second:
        first_int = float(input("\nWhat's the first number?: "))
    for item in operations:
        print(item)
    operation = input("Pick an operation: ").strip()
    second_int = float(input("What's the next number?: "))
    get_operation = operations[operation]
    result = get_operation(first_int, second_int)
    print(f"{first_int} {operation} {second_int} = {result}")

    return result


def repeat_calculation():
    calculate_more = True
    result = calculator(0, False)
    while calculate_more:
        repeat = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation: ")
        if repeat[0].lower().strip() == 'y':
            os.system("clear")
            result = calculator(result, True)
        elif repeat[0].lower().strip() == 'n':
            repeat_calculation()
        else:
            print("Thank you fo using our Calculator! Good bye!!!")
            calculate_more = False


repeat_calculation()

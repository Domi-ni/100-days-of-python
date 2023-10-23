from os import system
from art import logo


def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    print("Welcome to the Calculator App")

    first_number = float(input("Enter first number: "))
    for key in operations:
        print(key)

    calculating = True
    while calculating == True:
        operator = input("\nPick an operator: ")
        second_number = float(input("\nEnter next number: "))
        result = operations[operator](first_number, second_number)

        print(f"{first_number} {operator} {second_number} = {result}\n")

        if (
            input(
                f'Type "y" to continue calculating with {result}, or type "n" to start a new calculation: '
            ).lower()
            == "y"
        ):
            first_number = result

        else:
            calculating = False
            calculator()
            system("cls")


calculator()

from art import logo
import os

def calculator(number1, operation, number2):
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    else:
        result = number1 / number2
    return result



stored_value = 0
still_calculating = True

while still_calculating:
    if stored_value == 0:
        first_number = int(input("What's the first number?: "))
        print("+\n-\n*\n/")
    else:
        first_number = stored_value
    operator = input("Pick an operation: ")
    second_number = int(input("What's the second number?: "))
    calc_result = calculator(number1=first_number, operation=operator, number2=second_number)
    print(f"{first_number} {operator} {second_number} = {calc_result}")
    continue_with_calc_result = input(f"Type 'y' to continue calculating with {calc_result}, or type 'n' to start a new calculation: ")
    if continue_with_calc_result == "y":
        stored_value = calc_result
    else:
        os.system("cls")
        print(logo)
        stored_value = 0

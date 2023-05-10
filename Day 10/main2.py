from art import logo

#Add
def add(n1, n2):
    return n1 + n2
#Subtract
def subtract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    continue_calculation = True

    num1 = float(input("What's the first number?: "))
    for operator in operations:
        print(operator)

    while continue_calculation:
        operator_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))

        result = operations[operator_symbol](num1, num2)

        print(f"{num1} {operator_symbol} {num2} = {result}")
        continue_with_calc_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if continue_with_calc_result == "y":
            num1 = result
        else:
            continue_calculation = False
            calculator()

calculator()
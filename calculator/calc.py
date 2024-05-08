from art import logo
print(logo)
# Add
def add(a, b):
    return a + b


# Subtract
def subtract(a, b):
    return a - b


# Multiply
def multiply(a, b):
    return a * b


# Divide
def divide(a, b):
    return a / b


# Dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What's the second number?: "))
        # Calculation
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
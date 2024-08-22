from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    should_continue = True

    num1 = float(input("Enter the first number: "))
    while should_continue:

        for key in operations:
            print(key)
        operation_key = input("Pick an operation: ")
        num2 = float(input("Enter the second number: "))
        result = operations[operation_key](num1, num2)
        print(f"{num1} {operation_key} {num2} = {result} ")

        choice = input(f"If you want to continue with {result}? Type 'y'"
                       "If you want to start with new calculation? Type 'n'")
        if choice == "y":
            num1 = result
        else:
            should_continue = False
            print("\n" * 20)
            calculator()
calculator()

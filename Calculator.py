def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print("CALCULATOR USING PYTHON")
def Calculator(): 
    should_accumulate = True

    num1 = float(input("What's your first number?:  "))

    while should_accumulate:
   
        for symbol in operation:
            print(symbol)
        operation_symbol = input("Pick your operation:  ")
        num2 = float(input("What's your second number?:  "))

        answer = operation[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")


        choice =  input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start new caluclation: ")

        if choice == 'y':
            num1 = answer 
        else:
            should_accumulate = False
            print("\n" * 20)
            Calculator()

Calculator()



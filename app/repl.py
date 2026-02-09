from app.operations import add, subtract, multiply, divide


def get_number(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Invalid number. Please try again.")


def start():
    print("Welcome to Calculator")
    print("Operations: +  -  *  /  exit")

    while True:
        op = input("Enter operation: ")

        if op == "exit":
            print("Goodbye!")
            break

        if op not in ["+", "-", "*", "/"]:
            print("Invalid operation")
            continue

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        try:
            if op == "+":
                print("Result:", add(a, b))
            elif op == "-":
                print("Result:", subtract(a, b))
            elif op == "*":
                print("Result:", multiply(a, b))
            elif op == "/":
                print("Result:", divide(a, b))

        except ValueError as e:
            print("Error:", e)

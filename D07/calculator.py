def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Error: Division by zero"

print("Simple Calculator")
print("Operations: +, -, *, /")

while True:
    choice = input("\nEnter operation (+, -, *, /) or 'exit' to quit: ")
    if choice.lower() == 'exit':
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '+':
        print("Result:", add(num1, num2))
    elif choice == '-':
        print("Result:", subtract(num1, num2))
    elif choice == '*':
        print("Result:", multiply(num1, num2))
    elif choice == '/':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation. Try again.")

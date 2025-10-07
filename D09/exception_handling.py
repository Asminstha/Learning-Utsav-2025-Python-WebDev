# --- Basic Exception Handling ---
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter a valid number.")
else:
    print("Operation completed successfully.")
finally:
    print("Execution finished.\n")

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("You must be 18 or older.")
    print("Access granted.")
except ValueError as e:
    print("Exception caught:", e)
finally:
    print("Program ended.")

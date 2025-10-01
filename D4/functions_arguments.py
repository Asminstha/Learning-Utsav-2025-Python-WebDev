# Function with arguments
def add_numbers(a, b):
    return a + b

# Function with default argument
def greet_user(name="Guest"):
    return f"Hello, {name}!"

print("Sum:", add_numbers(5, 7))
print(greet_user("Asmin"))
print(greet_user())

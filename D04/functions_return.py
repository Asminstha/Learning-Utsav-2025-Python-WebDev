# Function with return value
def square(num):
    return num * num

# Function returning multiple values
def calculate(a, b):
    return a + b, a - b, a * b, a / b

print("Square of 4:", square(4))
add, sub, mul, div = calculate(10, 2)
print("Add:", add, "Sub:", sub, "Mul:", mul, "Div:", div)

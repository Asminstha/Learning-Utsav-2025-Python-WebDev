# Problem 1: Sum of first n natural numbers
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum of first", n, "numbers is:", total)

# Problem 2: Factorial of a number
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial of", n, "is:", fact)

# Problem 3: Multiplication table
num = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

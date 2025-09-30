# While loop example
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# Example: keep asking until correct input
password = ""
while password != "python123":
    password = input("Enter password: ")
print("Access granted!")

# Working with Lists in Python

# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding and updating
fruits.append("orange")
fruits[1] = "blueberry"
print("Updated fruits:", fruits)

# Iterating through a list
for fruit in fruits:
    print("Fruit:", fruit)

# List slicing
print("First two fruits:", fruits[:2])

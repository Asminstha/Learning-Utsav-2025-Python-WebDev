# Working with Tuples in Python

# Creating a tuple
colors = ("red", "green", "blue")

# Accessing elements
print("First color:", colors[0])
print("Last color:", colors[-1])

# Iterating through a tuple
for color in colors:
    print("Color:", color)

# Tuple unpacking
(r, g, b) = colors
print("Unpacked values:", r, g, b)

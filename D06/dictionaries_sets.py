# --- Dictionaries ---
student = {
    "name": "Asmin",
    "age": 22,
    "course": "Python Web Dev"
}

# Access values
print("Name:", student["name"])
print("Course:", student.get("course"))

# Add/update
student["email"] = "asmin@example.com"
student["age"] = 23
print("Updated dict:", student)

# Delete
del student["course"]
print("After deletion:", student)

# Loop
for key, value in student.items():
    print(key, ":", value)


# --- Sets ---
fruits = {"apple", "banana", "cherry", "apple"}  # removes duplicate
print("Unique fruits:", fruits)

# Add element
fruits.add("orange")

# Remove element
fruits.remove("banana")

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

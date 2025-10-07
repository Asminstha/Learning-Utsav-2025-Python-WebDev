# --- Writing to a File ---
with open("notes.txt", "w") as file:
    file.write("Welcome to Learning Utsav 2025!\n")
    file.write("Today I learned about file handling in Python.\n")

print("Data written to notes.txt")

# --- Reading from a File ---
with open("notes.txt", "r") as file:
    content = file.read()
    print("\nFile Content:")
    print(content)

# --- Appending Data ---
with open("notes.txt", "a") as file:
    file.write("Appending new lines is easy with 'a' mode.\n")

print("\nData appended successfully.")

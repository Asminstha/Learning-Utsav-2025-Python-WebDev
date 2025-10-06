def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\nFile Content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print("Unexpected error occurred:", e)
    else:
        print("\nFile read successfully.")
    finally:
        print("Operation completed.")

# --- Main Program ---
file_name = input("Enter filename to read: ")
read_file(file_name)

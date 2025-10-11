import os
import json
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, "contacts.json")
TXT_FILE = os.path.join(BASE_DIR, "contacts.txt")

#  FILE OPERATIONS 
def load_contacts():
    """Load contacts from JSON if exists, else recover from TXT."""
    contacts = {}
    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, "r") as file:
                contacts = json.load(file)
        except json.JSONDecodeError:
            print("⚠️ JSON file corrupted. Attempting recovery from TXT...")
            contacts = recover_from_txt()
    else:
        if os.path.exists(TXT_FILE):
            print("⚠️ JSON file missing. Attempting recovery from TXT...")
            contacts = recover_from_txt()
    return contacts

def save_contacts(contacts):
    """Save contacts to both JSON and TXT files."""
    # Save JSON
    with open(JSON_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

    # Save TXT backup
    with open(TXT_FILE, "w") as file:
        for name, info in contacts.items():
            file.write(f"{name}, {info['number']}, {info['email']}, {info['address']}\n")

def recover_from_txt():
    """Recover contacts from TXT file if JSON is missing or corrupted."""
    recovered = {}
    if os.path.exists(TXT_FILE):
        with open(TXT_FILE, "r") as file:
            for line in file:
                parts = [p.strip() for p in line.strip().split(",")]
                if len(parts) == 4:
                    name, number, email, address = parts
                    recovered[name] = {
                        "number": number,
                        "email": email,
                        "address": address
                    }
        print(f"✅ Recovery successful. {len(recovered)} contacts restored.")
        save_contacts(recovered)  # Save back to JSON
    else:
        print("❌ No TXT backup found. Starting with empty contacts.")
    return recovered

#  VALIDATIONS 
def validate_number(number):
    if not number.isdigit():
        print("❌ Number must contain only digits.")
        return False
    if len(number) != 10:
        print("❌ Number must be exactly 10 digits long.")
        return False
    if not (number.startswith("97") or number.startswith("98")):
        print("❌ Number must start with 97 or 98 (valid Nepali mobile numbers).")
        return False
    return True

def validate_email(email):
    if email == "" or email.lower() == "n/a":
        return True  # optional field
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email):
        return True
    else:
        print("❌ Invalid email format. Example: name@example.com")
        return False

#  CORE FEATURES 
def add_contact(contacts):
    name = input("Enter name: ").title()

    while True:
        number = input("Enter 10-digit phone number: ")
        if validate_number(number):
            break

    while True:
        email = input("Enter email (optional): ") or "N/A"
        if validate_email(email):
            break

    address = input("Enter address (optional): ") or "N/A"

    if name in contacts:
        print("⚠️ Contact already exists.")
    else:
        contacts[name] = {"number": number, "email": email, "address": address}
        save_contacts(contacts)
        print("✅ Contact added successfully!")

def view_contacts(contacts):
    if contacts:
        print("\n--- Contact List ---")
        for name, info in contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {info['number']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
    else:
        print("No contacts found.")

def search_contact(contacts):
    name = input("Enter name to search: ").title()
    if name in contacts:
        info = contacts[name]
        print(f"\nName: {name}")
        print(f"Phone: {info['number']}")
        print(f"Email: {info['email']}")
        print(f"Address: {info['address']}")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter name to delete: ").title()
    if name in contacts:
        confirm = input(f"Are you sure you want to delete {name}? (y/n): ")
        if confirm.lower() == "y":
            del contacts[name]
            save_contacts(contacts)
            print("✅ Contact deleted successfully.")
    else:
        print("Contact not found.")

#  MAIN 
def main():
    contacts = load_contacts()
    print("📒 Contact Book Loaded Successfully.")
    print(f"Existing contacts: {len(contacts)}\n")

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

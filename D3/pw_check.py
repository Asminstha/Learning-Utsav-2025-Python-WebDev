# Password check with limited attempts

correct_pw = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    
    if password == correct_pw:
        print("Access granted!")
        break
    else:
        print("Incorrect password, try again.")
        attempts += 1

if attempts == max_attempts:
    print("Too many failed attempts. Access denied.")

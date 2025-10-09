class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Current balance: ${self.__balance}")

# Example Usage
acc = Account("Asmin", 1000)
acc.deposit(200)
acc.withdraw(500)
acc.check_balance()


# Encapsulation ensures data protection by hiding sensitive variables (like __balance) inside the class, accessible only through defined methods.



# Base Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

# Derived Classes
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Example Usage
dog = Dog("Buddy")
cat = Cat("Misty")

print(f"{dog.name} says {dog.speak()}")
print(f"{cat.name} says {cat.speak()}")


# The Dog and Cat classes inherit properties and methods from the Animal class and override the speak() method — showcasing inheritance and polymorphism in action.

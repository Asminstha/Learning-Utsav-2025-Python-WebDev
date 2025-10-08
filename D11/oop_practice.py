# --- Class and Object Example ---

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.brand} {self.model} engine has started.")

    def car_info(self):
        return f"{self.year} {self.brand} {self.model}"

# Creating Objects
car1 = Car("Tesla", "Model 3", 2024)
car2 = Car("Toyota", "Corolla", 2020)

# Accessing Methods
print(car1.car_info())
car1.start_engine()

print(car2.car_info())
car2.start_engine()

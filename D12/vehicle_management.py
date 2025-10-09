class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"Car - Brand: {self.brand}, Model: {self.model}, Fuel: {self.fuel_type}")

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def display_info(self):
        print(f"Bike - Brand: {self.brand}, Model: {self.model}, Engine: {self.engine_cc}cc")

# Polymorphism in Action
vehicles = [
    Car("Tesla", "Model S", "Electric"),
    Bike("Yamaha", "R15", 155)
]

for v in vehicles:
    v.display_info()

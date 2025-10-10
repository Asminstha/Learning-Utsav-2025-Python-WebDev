class Father:
    def skills(self):
        return ["Driving", "Gardening"]

class Mother:
    def skills(self):
        return ["Cooking", "Painting"]

class Child(Father, Mother):
    def skills(self):
        return super().skills() + ["Programming", "Music"]

child = Child()
print("Child skills:", child.skills())

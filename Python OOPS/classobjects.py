class Bike:
    name = ""
    gear = 0
    #Constructor
    def __init__(self, name, gear):
        self.name = name
        self.gear = gear
    def details(self):
        print(f"This is a bike whose name is {self.name} and it has {self.gear}")


bike1 = Bike("HayaBusa",4)
bike2 = Bike("GT 600",6)
print(f"Name: {bike1.name}, Gears: {bike1.gear}")
print(f"Name: {bike2.name}, Gears: {bike2.gear}")

bike1.details()
bike2.details()
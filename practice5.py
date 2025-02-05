from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def fuel_type(self):
        pass

class Car(Vehicle):
    wheel = 4
    @classmethod
    def set_wheel(cls,num_wheels):
        Car.wheel = num_wheels
    @staticmethod
    def general_info():
        print("Cars are a common mode of transportation")
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def fuel_type(self):
        print("Uses petrol or diesel")

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Wheel: {Car.wheel}")

car1 = Car("Hyundai","I20")

car2 = Car("Tata","Nexa")

car1.display_info()
car1.general_info()
print()
Car.set_wheel(5)
car2.display_info()
car2.general_info()
car1.fuel_type()
car2.fuel_type()
class ElectricCar(Car):
    def __init__(self,brand,model,battery_capacity):
        super().__init__(brand,model)
        self.battery_capacity = battery_capacity
    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity}")
    def fuel_type(self):
        print("Uses Uses Electricity")

print()
elect1 = ElectricCar("Tesla","M5","5300Mah")
elect1.display_info()
elect1.fuel_type()







#Inheritance


class Vehicle:
    def __init__(self,vehicle_type):
        self.vehicle_type = vehicle_type
    def show_info(self):
        print(f"Vehicle Type: {self.vehicle_type}")

class Car(Vehicle):
    def __init__(self,vehicle_type,brand):
        super().__init__(vehicle_type)
        self.brand = brand
    def show_details(self):
        self.show_info()
        print(f"Car Brand: {self.brand}")


vehicle_type = input()
brand = input()
car1 = Car(vehicle_type,brand)
car1.show_details()
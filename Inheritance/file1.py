# # class Animal:
# #     def __init__(self,name):
# #         self.name = name
# #     def make_sound(self):
# #         print("Animal makes a sound")
# #
# # class Dog(Animal):
# #     def __init__(self,name,breed):
# #         Animal.__init__(self,name)
# #         self.breed = breed
# #     def bark(self):
# #         self.make_sound()
# #         print("Dog barks")
# #         print(f"Dod Breed: {self.breed}")
# #
# # dog1 = Dog("Simba","Labradog")
# # dog1.bark()
# from OOPs.file1 import brand
#
#
# # class Person:
# #     def __init__(self,name):
# #         self.name = name
# #     def show_person_info(self):
# #         print(f"Person Name: {self.name}")
# #
# # class Employee:
# #     def __init__(self,name,salary):
# #         Person.__init__(self,name)
# #         self.salary = salary
# #     def show_salary(self):
# #         self.show_person_info()
# #         print(f"Person Salary: {self.salary}")
# #
# # class Manager(Person,Employee):
# #     def __init__(self,name,salary):
# #         Person.__init__(self,name)
# #         Employee.__init__(self,name,salary)
# #     def show_manager_info(self):
# #         self.show_person_info()
# #         self.show_salary()
# #
# # manager1 = Manager("Rashid",25000)
# # manager1.show_manager_info()
#
# # class Device:
# #     def __init__(self,device_name):
# #         self.device_name = device_name
# #     def show_device_info(self):
# #         print(f"Device Name: {self.device_name}")
# # class Connectivity:
# #     def __init__(self,connectivity_type):
# #         self.connectivity_type = connectivity_type
# #     def show_connectivity_info(self):
# #         print(f"Connectivity Type: {self.connectivity_type}")
# # class Smartphone(Device,Connectivity):
# #     def __init__(self,device_name,connectivity_type,brand,price):
# #         Device.__init__(self,device_name)
# #         Connectivity.__init__(self,connectivity_type)
# #         self.brand = brand
# #         self.price = price
# #     def show_smartphone_info(self):
# #         self.show_device_info()
# #         self.show_connectivity_info()
# #         print(f"Brand: {self.brand}")
# #         print(f"Price: {self.price}")
# #
# # phone1 = Smartphone("Samsung Galaxy","5G","Samsung",25000)
# # phone1.show_device_info()
# # phone1.show_connectivity_info()
# # phone1.show_smartphone_info()
#
# # class Item:
# #     def __init__(self,title,author):
# #         self.title = title
# #         self.author = author
# #     def display_item_info(self):
# #         print(f"Title: {self.title}")
# #         print(f"Author: {self.author}")
# # class Book(Item):
# #     def __init__(self,title,author,genre):
# #         super().__init__(title,author)
# #         self.genre = genre
# #     def display_book_info(self):
# #         self.display_item_info()
# #         print(f"Genre: {self.genre}")
# # class Ebook(Book):
# #     def __init__(self,title,author,genre,file_size):
# #         super().__init__(title,author,genre)
# #         self.file_size = file_size
# #     def display_ebook_info(self):
# #         super().display_book_info()
# #         print(f"File Size: {self.file_size}")
# #
# # ebook1 = Ebook("Python Mastery","John Doe","Programming","5MB")
# # ebook1.display_ebook_info()

# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def display_vehicle_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
# class Car(Vehicle):
#     def __init__(self,brand,model,fuel_type):
#         super().__init__(brand,model)
#         self.fuel_type = fuel_type
#     def display_car_info(self):
#         super().display_vehicle_info()
#         print(f"Fuel Type: {self.fuel_type}")
# class Bike(Vehicle):
#     def __init__(self,brand,model,engine_capacity):
#         super().__init__(brand,model)
#         self.engine_capacity = engine_capacity
#     def display_bike_info(self):
#         super().display_vehicle_info()
#         print(f"Engine Capacity: {self.engine_capacity}")
#
# car1 = Car("Honda","Civic","Petrol")
# bike1 = Bike("Yamaha","R15","155cc")
# car1.display_car_info()
# print()
# bike1.display_bike_info()

class Person:
    def __init__(self,name):
        self.name = name
    def display_name(self):
        print(f"Name: {self.name}")
class Employee(Person):
    def __init__(self,name,salary):
        super()






        



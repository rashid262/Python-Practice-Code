# class Animal:
#     name = ""
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         print("Animal Speaks")
# class Dog(Animal):      #inhering the properties and behaviours of Animal class in Dog class
#     def __init__(self,name):
#         super().__init__(name)
#     def speak(self):
#         print(f"{self.name} says Woof!")

# class Shape:
#     def area(self):
#         print("Area of shape")
#
# class Circle(Shape):
#     radius = 0
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         area1 = 3.14 * self.radius * self.radius
#         print("Area of circle is", area1)
#
# class Rectangle(Shape):
#     length = 0
#     breadth = 0
#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
#     def area(self):
#         area1 = self.length * self.breadth
#         print("Area of Rectangle is: ",area1)
# cir = Circle(49)
# rect = Rectangle(15,15)
# cir.area()
# rect.area()
#Single Inheritance
# class Animal:
#     def eat(self):
#         print("Animal eats")
# class Dog(Animal):
#     def eat(self):
#         print("Dog Barks")
#
# anim = Animal()
# anim.eat()
# dog = Dog()
# dog.eat()

#Multilevel Inheritance
# class Person:
#     name = ""
#     def __init__(self,name):
#         self.name = name
#     def introduce(self):
#         print(f"Hello I am {self.name}")
# class Employee(Person):
#     salary = 0
#     def __init__(self,name,salary):
#         super().__init__(name)
#         self.salary = salary
#     def work(self):
#         print(f"I am working with a salary of {self.salary}")
# class Manager(Employee):
#     def __init__(self,name,salary):
#         super().__init__(name,salary)
#     def manage(self):
#         print("I am managing team")
#
# manager = Manager("Mohammad Rashid Ansari",65000)
# manager.introduce()
# manager.work()
# manager.manage()

#Hirarchical Inheritance
# class Vehicle:
#     brand = ""
#     def __init__(self,brand):
#         self.brand = brand
#     def display_brand(self):
#         print(f"This is a {self.brand} vehicle")
# class Car(Vehicle):
#     def __init__(self,brand):
#         super().__init__(brand)
#     def drive(self):
#         print("Car is driving")
# class Bike(Vehicle):
#     def __init__(self,brand):
#         super().__init__(brand)
#     def ride(self):
#         print("Bike is riding")
# car = Car("Baleno")
# bike = Bike("GT 700")
# print(car.brand)
# car.drive()
# print(bike.brand)
# bike.ride()


# Multiple Inheritance (Method Resolution Technique)
# Search Sequence -> child_class --> first_written_in_inheritance --> _next_written_class_in_child_parameter_inheritance
# (as soon as we got out member in any class search will be stopped)
"""
class Person:
    def work(self):
        print("Hello, i am a person")

class Employee:
    def work(self):
        print("I am working")

class Manager(Person,Employee):
    def manage(self):
        pass
myManager  = Manager()
myManager.work()
"""

# class Demo1:
#     def __init__(self):
#         self.x = 100
# class Demo2:
#     def __init__(self):
#         self.x = 200
# class Demo3(Demo2, Demo1):
#     def __init__(self):
#         self.x = 300
#
#
# obj1 = Demo3()
# print(obj1.x)

# class ElectricDevice:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def display_device_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#
# class Warranty:
#     def __init__(self,warranty_provider,warranty_expiry):
#         self.warranty_provider = warranty_provider
#         self.warranty_expiry = warranty_expiry
#     def display_warranty_info(self):
#         print(f"Warranty Provider: {self.warranty_provider}")
#         print(f"Warranty Expiry: {self.warranty_expiry}")
#
# class Laptop(ElectricDevice,Warranty):
#     def __init__(self,brand,model,serial_number,warranty_provider,warranty_expiry):
#        ElectricDevice.__init__(self,brand,model)
#        Warranty.__init__(self,warranty_provider,warranty_expiry)
#        self.serial_number = serial_number
#     def display_laptop_info(self):
#         self.display_device_info()
#         print(f"Serial Number: {self.serial_number}")
#         self.display_warranty_info()
#
#
# brand = input()
# model = input()
# serial_number = input()
# warranty_provider = input()
# warranty_expiry = input()
#
# laptop1 = Laptop(brand,model,serial_number,warranty_provider, warranty_expiry)
# laptop1.display_laptop_info()


# class Media:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
#     def display_media_info(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
# class DigitalMedia(Media):
#     def __init__(self,title,author,file_format):
#         super().__init__(title,author)
#         self.file_format = file_format
#     def display_digital_media_info(self):
#         super().display_media_info()
#         print(f"File Format: {self.file_format}")
# class Ebook(DigitalMedia):
#     def __init__(self,title,author,file_format,file_size):
#         super().__init__(title,author,file_format)
#         self.file_size = file_size
#     def display_ebook_info(self):
#         self.display_digital_media_info()
#         print(f"File Size: {self.file_size}")
#
# title = input()
# author = input()
# file_format = input()
# file_size = input()
#
# ebook1 = Ebook(title,author,file_format,file_size)
# ebook1.display_ebook_info()

# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def display_vehicle_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
# class Engine:
#     def __init__(self,engine_type):
#         self.engine_type = engine_type
#     def display_engine_info(self):
#         print(f"Engine Type: {self.engine_type}")
# class Car(Vehicle,Engine):
#     def __init__(self,brand,model,engine_type,battery_capacity):
#         Vehicle.__init__(self,brand,model)
#         Engine.__init__(self,engine_type)
#         self.battery_capacity = battery_capacity
#     def display_electric_car_info(self):
#         self.display_vehicle_info()
#         self.display_engine_info()
#         print(f"Battery Capacity: {self.battery_capacity}")
#
# brand = input()
# model = input()
# engine_type = input()
# battery_capacity = input()
# ev1 = Car(brand,model,engine_type,battery_capacity)
# ev1.display_electric_car_info()




























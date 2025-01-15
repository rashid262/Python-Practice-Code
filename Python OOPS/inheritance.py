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

#Multiple Inheritance
# class Person:
#     def introduce(self):
#         print("Hello, i am a person")
#
# class Employee:
#     def work(self):
#         print("I am working")
#
# class Manager(Person,Employee):
#     def manage(self):
#         print("i am managing team")
# myManager  = Manager()
# myManager.introduce()
# myManager.work()
# myManager.manage()

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
class Vehicle:
    brand = ""
    def __init__(self,brand):
        self.brand = brand
    def display_brand(self):
        print(f"This is a {self.brand} vehicle")
class Car(Vehicle):
    def __init__(self,brand):
        super().__init__(brand)
    def drive(self):
        print("Car is driving")
class Bike(Vehicle):
    def __init__(self,brand):
        super().__init__(brand)
    def ride(self):
        print("Bike is riding")
car = Car("Baleno")
bike = Bike("GT 700")
print(car.brand)
car.drive()
print(bike.brand)
bike.ride()







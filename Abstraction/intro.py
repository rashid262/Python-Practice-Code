"""
    1. If abstract class doesn't have any method
    then object for that abstract class can be created.

    2. If abstract class have only concrete method
    then object of that abstract class can be created,
    we can invoke that concrete method also.
"""

# from abc import ABC, abstractmethod
# #Abstract method
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
# class Car(Vehicle):
#     def start(self):
#         print("Car is starting")
#     def stop(self):
#         print("Car is stopping")
#
# my_car = Car()
# my_car.start()
# my_car.stop()

# from abc import ABC, abstractmethod
# #mimicing Interface
# class PaymentProcess(ABC):
#     @abstractmethod
#     def process_payment(self,amount):
#         pass
# class CreditCardPayment(PaymentProcess):
#     def __init__(self, amount):
#         self.amount = amount
#     def process_payment(self):
#         print(f"Processing credit card payment of amount {self.amount} dollars")
# class PayPalPayment(PaymentProcess):
#     def __init__(self, amount):
#         self.amount = amount
#     def process_payment(self):
#         print(f"Processing Paypal payment of amount {self.amount} dollars")
#
# credit_payment = CreditCardPayment(2500)
# credit_payment.process_payment()
# paypal_payment = PayPalPayment(27000)
# paypal_payment.process_payment()

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self,):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        print(f"Rectangle Area: {self.length * self*width}")
    def perimeter(self):
        print(f"Rectangle Perimeter: {2 * (self.length + self.width)}")
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(f"Circle Area: {3.14 * self.radius * self.radius}")
    def perimeter(self):
        print(f"Circle Perimeter: {2 * self.radius * 3.14}")

length = float(input())
width = float(input())
radius = float(input())

rect = Rectangle(length,width)
circle = Circle(radius)




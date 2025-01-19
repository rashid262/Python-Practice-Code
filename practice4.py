# def greet(name):
#     return f'Hello, {name}'
#
# print(greet("Rashid"))
from traceback import print_tb


# def add(num1 = 100, num2 = 200):
#     return num1 + num2
#
# print(add())

#Function with arbitrary numbers of arguments

# def find_sum(*numbers):
#     result = 0
#     for num in numbers:
#         result = result + num
#     return result
#
# print(find_sum(52))
# print(find_sum(65,98))
# print(find_sum(45,89,35))

#in python we can only access global variable and can;t be changes

"""
When we create a variable inside a function, it is local by default.
When we define a variable outside of a function, it is global by default. You don't have to use the global keyword.
We use the global keyword to modify (write to) a global variable inside a function.
Use of the global keyword outside a function has no effect.
"""

# import  math as mt
# print(dir(mt))  #this will show are the functions name in this module

# try:
#     numerator = 10
#     denominator = 0
#     result = numerator / denominator
#     print(result)
# except ZeroDivisionError:
#     print(ZeroDivisionError)


# str1 = "i am not coming"
# print(str1.count(" "))

# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def calculate_are(self):
#         return 3.14 * self.radius * self.radius
#
# c1 = Circle(25)
# print(c1.calculate_are())

# def safe_division(x):
#     return x / 2 if x%2 == 0 else " "
# num = [safe_division(x) for x in range(1,11)]
# print(num)

# list with only off num

# num = [x for x in range(1,11) if x%2 != 0]
# print(num)

num = []

# for x in range(1,11):
#     num.append(x)

# for x in range(1,11):
#     num.append(x**2)
#
# print(num)
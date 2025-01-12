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

try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(result)
except ZeroDivisionError:
    print(ZeroDivisionError)


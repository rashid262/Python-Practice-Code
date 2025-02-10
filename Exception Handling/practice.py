# def divide(a,b):
#     try:
#         print(a / b)
#     except ZeroDivisionError:
#         print("Divided by Zero error")
#
# divide(10,0)
import math


# def division(a):
#     print("Result:", a / 5)
#
# try:
#     num = int(input("Enter a number: "))  # Moved inside try block
#     division(num)
# except ValueError:
#     print("Error: Please enter a valid number.")
# finally:
#     print("Calculation Completed.")

# def division(num):
#     try:
#         print("Program started")
#         print(100/int(num))
#     except ZeroDivisionError:
#         print("You are trying to divide by zero")
#     except ValueError:
#         print("You have not entered integer")
#     else:
#         print(f"Output: {100/int(num)}")
#     finally:
#         print("Program Ended")
#
# num = input()
# division(num)

# def division(num):
#     try:
#         result = 100/int(num)
#     except ValueError:
#         print("You have entered non-integer value")
#     except ZeroDivisionError:
#         print("You are trying to divide by zero")
#     except Exception as e:
#         print(e)
#     else:
#         print(f"Output after calculation: {result}")
#     finally:
#         print("Execution Completed")

# class NegativeValueError(Exception):
#     pass
#
# def value(num):
#     if num < 0:
#         raise NegativeValueError("Negative value Entered")
#     else:
#         print("Correct Value Entered")
#
# num = int(input())
#
# try:
#     value(num)
# except NegativeValueError:
#     print("Negative value Entered")

# class OnlyPositive(Exception):
#     pass
#
# def onlyPositive(num):
#     if int(num) < 0:
#         raise OnlyPositive("You have to enter only positive number")
#     else:
#         print("Correct Input")
#
# num = input()
# try:
#     onlyPositive(num)
# except OnlyPositive as e:
#     print(e)

# def divideByZero(a,b):
#     try:
#         result = a/b
#     except:
#         print("You can't divide a number by zero")
#     else:
#         print(f"Result of division: {a/b}")
#     finally:
#         print("Program Execution Completed")
#
#
# num1 = int(input())
# num2 = int(input())
# divideByZero(num1,num2)


# def sqrt(num):
#     try:
#         result = math.sqrt(int(num));
#     except ValueError:
#         print("Enter a positive number")
#     except:
#         print("Cannot calculate square root of a negative number")
#     else:
#         print("Result: ",result)
#     finally:
#         print("Program Executed")
#
# num = input()
# sqrt(num)

# class Order:
#     def __init__(self):
#         self.total = 0
#     def place_order(self,amount):
#         if amount < 0:
#             raise ValueError("Order failed. Order amount must be positive.")
#         else:
#             self.total += amount
#             print(f"Order of {amount} placed successfully. Current total: {self.total}")
#     def apply_discount(self,discount):
#         if discount < 0 or discount > self.total:
#                 raise ValueError("Discount failed. Discount cannot be greater than total order value.")
#         else:
#             self.total -= discount
#             print(f"Discount of {discount} applied successfully. Current total: {self.total}")
#
# amount = int(input())
# discount = int(input())
#
# order1 = Order()
#
# try:
#     order1.place_order(amount)
# except ValueError as e:
#     print(e)
#
# try:
#     order1.apply_discount(discount)
# except ValueError as e:
#     print(e)

class Inventory:
    def __init__(self):
        self.products = {}
    def add_product(self,name,quantity):
        if quantity < 0:
            raise ValueError("Addition failed. Quantity must be positive")
        else:
            self.products[name] = quantity
            print(f"{quantity} {name} added in inventory. Current quantity: {self.products[name]}" )
    def remove_product(self,name,quantity):
        if name not in self.products or quantity < 0 or quantity > self.products[name]:
            raise ValueError(f"Removal failed. Product {name} not found in inventory.")
        else:
            self.products[name] -= quantity
            print(f"{quantity} {name} removed from inventory. Current quantity: {self.products[name]}")

inv1 = Inventory()
name1, quantity1 = input().split(" ")
name2, quantity2 = input().split(" ")
try:
    inv1.add_product(name1, int(quantity1))
except ValueError as e:
    print(e)
try:
    inv1.remove_product(name2,int(quantity2))
except ValueError as e:
    print(e)





























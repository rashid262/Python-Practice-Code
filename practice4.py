# # def greet(name):
# #     return f'Hello, {name}'
# #
# # print(greet("Rashid"))
# from traceback import print_tb
#
# from pygments.styles.dracula import yellow
#
# from practice import second
#
# # def add(num1 = 100, num2 = 200):
# #     return num1 + num2
# #
# # print(add())
#
# #Function with arbitrary numbers of arguments
#
# # def find_sum(*numbers):
# #     result = 0
# #     for num in numbers:
# #         result = result + num
# #     return result
# #
# # print(find_sum(52))
# # print(find_sum(65,98))
# # print(find_sum(45,89,35))
#
# #in python we can only access global variable and can;t be changes
#
# """
# When we create a variable inside a function, it is local by default.
# When we define a variable outside of a function, it is global by default. You don't have to use the global keyword.
# We use the global keyword to modify (write to) a global variable inside a function.
# Use of the global keyword outside a function has no effect.
# """
#
# # import  math as mt
# # print(dir(mt))  #this will show are the functions name in this module
#
# # try:
# #     numerator = 10
# #     denominator = 0
# #     result = numerator / denominator
# #     print(result)
# # except ZeroDivisionError:
# #     print(ZeroDivisionError)
#
#
# # str1 = "i am not coming"
# # print(str1.count(" "))
#
# # class Circle:
# #     def __init__(self,radius):
# #         self.radius = radius
# #     def calculate_are(self):
# #         return 3.14 * self.radius * self.radius
# #
# # c1 = Circle(25)
# # print(c1.calculate_are())
#
# # def safe_division(x):
# #     return x / 2 if x%2 == 0 else " "
# # num = [safe_division(x) for x in range(1,11)]
# # print(num)
#
# # list with only off num
#
# # num = [x for x in range(1,11) if x%2 != 0]
# # print(num)
#
# # num = []
#
# # for x in range(1,11):
# #     num.append(x)
#
# # for x in range(1,11):
# #     num.append(x**2)
# #
# # print(num)
#
# # nums = [1, 2, 3, 4, 5]
# # squares_gen = (x**2 for x in nums)  # Creates a generator object
# # print(squares_gen)  # Output: <generator object <genexpr> at 0x...>
# #
# # # To get the values, iterate through the generator
# # for square in squares_gen:
# #     print(square)
# #
# # # Output:
# # # 1
# # # 4
# # # 9
# # # 16
# # # 25
#
# """
# Generator Comprehension
# """
#
# # num = range(1,51)
# # sum_of_num = list(x for x in num)
# # print(sum_of_num)
#
# """file input output"""
#
# # with open("file1.txt","r") as file:
# #     content = file.read()
# #     print(content)
#
# # words = input("Enter your words: ").split(" ")
# # print(words)
#
# # words = input().split(" ")
# #
# # dict = {}
# #
# # for x in words:
# #     if x in dict:
# #         dict[x] += 1
# #     else:
# #         dict[x] = 1
# #
# # for key,value in dict.values():
# #     print(f"{key} : {value}")
#
#
# """
# #Sample Input
# 'Milk, 2.50'
# 'Egg, 2.5'
# """
# # products = {}
# # while True:
# #     user_input = input().strip()
# #     if user_input.lower() == "done":
# #         break
# #     else:
# #         key, value = user_input.split(",")
# #         value = value.strip()
# #         products[key] = value
# #
# # print(products)
#
# # coordinates = (10, 20)
# # x, y = coordinates
# # print(f"X : {x}")
# # print(f"Y : {y}")
#
# # numbers = [x for x in range(1,6)]
# # a , *middle, b = numbers
# # print(f"First: {a}")
# # print(f"Middle: {middle}")
# # print(f"Last: {b}")
#
# # numbers = [x for x in range(7,11)]
# #
# # x, y, *z = numbers
# #
# # print(f"X: {x}")
# # print(f"Y: {y}")
# # print(f"Z: {z}")
#
# # text = "hello"
# #
# # first, *middle, last = text
# #
# # print(f"First : {first}")
# # print(f"Middle : {middle}")
# # print(f"Last : {last}")
#
# # nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# #
# # first_row, second_row, *remaining_row = nested_list
# #
# # print(f"First Row: {first_row}")
# # print(f"Second Row: {second_row}")
# # print(f"First Row: {remaining_row}")

# s = "apple,banana,cherry"
# list1 = s.split(",")
# print(list1)
# new_list = ";".join(list1)
# print(new_list)
#
# s = "   Hello, Python!   "
# print(s.strip())

s_list = ["\t\n   Hello, World!   \n\t", "  Python is great!  ", "   Practice makes perfect!   "]
print(s_list)



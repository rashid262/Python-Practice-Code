# from Threading.DifferentMethods import print_task
# from operators import result
#
# # numbers = [1,2,3,4,5,6,7,8,9]
# #
# # def double(num):
# #     return num * 2
# #
# # double_list = list(map(double,numbers))
# # print(double_list)
# #map returns map object we have to convert it into list
#
# #
# # numbers = [1,2,3,4,5,6,7,8,9]
# # def checkEven(num):
# #     return num % 2 == 0
# #
# # even_list = list(filter(checkEven,numbers))
# # print(even_list)
# #
# # from functools import reduce
# # def mul(a,b):
# #     return a * b
# #
# # numbers = [1,2,3,4,5,6,7,8,9]
# # res = reduce(mul,numbers)
# # print("Multiplication is: ", res)
from numpy.core.defchararray import capitalize

# def double(num):
#     return num*2
#
# result_list = list(map(double,num))
# print(result_list)

# num = [3,6,9]
# doubled_list = list(map(lambda x:x*2,num))
# print(doubled_list)

# num = ['1','2','3','4']
#
# num_list = list(map(int,num))
# print(num_list)
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# sum_list = list(map(lambda x, y: x + y, list1, list2))
# print(sum_list)
# list_input = ["hello", "world", "python"]
# list_output = list(map(lambda x: x.upper(),list_input))
# print(list_output)

# input_list = ["apple", "banana", "cherry"]
# output_list = list(map(lambda x :len(x),input_list))
# print(output_list)

input_list = ["john", "alice", "bob"]
output_list = list(map(lambda x:x.capitalize(),input_list))
print(output_list)
















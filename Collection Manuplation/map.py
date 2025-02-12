from Threading.DifferentMethods import print_task

# numbers = [1,2,3,4,5,6,7,8,9]
#
# def double(num):
#     return num * 2
#
# double_list = list(map(double,numbers))
# print(double_list)
#map returns map object we have to convert it into list

#
# numbers = [1,2,3,4,5,6,7,8,9]
# def checkEven(num):
#     return num % 2 == 0
#
# even_list = list(filter(checkEven,numbers))
# print(even_list)
#
from functools import reduce
def mul(a,b):
    return a * b

numbers = [1,2,3,4,5,6,7,8,9]
res = reduce(mul,numbers)
print("Multiplication is: ", res)




# numbers = [1,2,3,4,5,6,7,8,9]
#
# doubled = []
# print(numbers)
# for num in numbers:
#     doubled.append(num*2)
# print(doubled)

"""
List Comprehension
"""
from numpy.core.defchararray import upper

# numbers = [1,2,3,4,5,7,8,9,10]
# doubled = [num * 2 for num in numbers]
# print(numbers)
# print(doubled)

# [expression for item in iterable if condition]


# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_numbers = [num for num in numbers if num%2==0]
# print(numbers)
# print(even_numbers)

#List comprehension to print number from 1 to 10

# list1 = [i for i in range(1,11)]
# print(list1)

# squared_list = [i*i for i in range(1,6)]
# print(squared_list)
#
# even_numbers = [num for num in range(1,11) if num%2==0]
# print(even_numbers)

# divisible_by_three = [num for num in range(1,21) if num%3==0]
# print(divisible_by_three)
#
# list1 = ["apple", "banana", "cherry"]
# new_list = [item.upper() for item in list1]
# print((new_list))


tuples = [(num, num**2) for num in range(1, 6)]
print(tuples)



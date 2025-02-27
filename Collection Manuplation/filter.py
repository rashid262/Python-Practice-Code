# num = [1, 2, 3, 4, 5, 6]
# def is_even(num):
#     return num%2==0
# output_list = list(filter(is_even,num))
# print(output_list)

# input_list = [10, 15, 20, 25, 30]
# output_list = list(filter(lambda x: x%2==0,input_list))
# print(output_list)

# input_list = ["apple", "banana", "cat", "elephant", "dog"]
# output_list = list(filter(lambda x : len(x) > 5,input_list))
# print(output_list)

import math


# def check_prime(num):
#     if num < 2:
#         return False  # Prime numbers start from 2
#
#     for i in range(2, int(math.sqrt(num)) + 1):  # Check divisibility up to sqrt(num)
#         if num % i == 0:
#             return False  # Not a prime number
#
#     return True  # If no divisor is found, it's prime
#
#
# input_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# output_list = list(filter(check_prime, input_list))
# print(output_list)

input_list = ["123", "hello", "456", "world", "789"]
output_list = list(filter(lambda x: x.isdigit(),input_list))
print(output_list)











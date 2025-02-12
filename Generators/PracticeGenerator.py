# def count(num):
#     count = 1
#     while num > count:
#         yield count
#         count += 1
#
#
# for num in count(5):
#     print(num)

# def factorial_generator(max_value):
#     factorial = 1
#     i = 1
#     while i <= max_value:
#         factorial *= i  # Update factorial first
#         yield factorial  # Then yield
#         i += 1  # Increment i
#
# num = int(input("Enter a number: "))
# ref = factorial_generator(num)
#
# for i in ref:
#     print(i)


#prime generator
import math

def prime_generator(max_value):
    current = 2
    while current <= max_value:
        is_prime = True
        for i in range(2, math.isqrt(current) + 1):
            if current % i == 0:
                is_prime = False
                break
        if is_prime:
            yield current
        current += 1

num = int(input())
ref = prime_generator(num)

for i in ref:
    print(i)




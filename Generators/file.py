#Normal Function
# def disp():
#     return 10
#     return 10
#     return 10
#
# print(disp())
# print(disp())
# print(disp())

# #Generator Function
# def generator_Function():
#     yield 25
#     yield 20
#     yield 30
#
# print(generator_Function())
# # Output: <generator object generator_Function at 0x000001CE02124A90>
# # generator object is simply created with the above statement
# print(next(generator_Function()))
# print(next(generator_Function()))
# print(next(generator_Function()))

# A generator function to count numbers from 1 to 3
def count_to_three():
    print("Hello")
    yield 1
    yield 2
    yield 3

# Using the generator
gen = count_to_three()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3


# message = 'Learning Python'
# print("First Character:",message[0])
# print("Last Character:",message[-1])
# print("Length of message is:",len(message))

# print(message[:5])
#
# print(message[::-1])


# message = "python is great"
# print(message.upper())
# print(message.replace("fun","awsome"))
# print(message.strip())

# print("great" in message)
# print(message.find("great"))

# first = "hello"
# second = "World"
#
# print(first + " " + second)
#
# name = "Alice"
# age = 25
#
# print(f"My name is {name} and i am {age} years")

# message = "Python is amazing"
# print(message.count('a'))
# print(message.find("is"))
# splitted_message = message.split(" ")
# joined_message = "-".join(splitted_message)
# print(splitted_message)
# print(joined_message)

# num1 = 25;
# print(num1,type(num1))
#
# num2 = 5.5
# print(num2,type(num2))
#
# addition = num1 + num2
# print(addition,type(addition))
#
# subtraction = num1  - num2
# print(subtraction,type(subtraction))
#
# division = num1 / num2
# print(division,type(division))
#
# num1 = '25'
# print(num1,type(num1))
# numint = int(num1)
# print(numint,type(numint))

# a = "25.6"
# b = float(a)
# c = 10.4
# print(b + c)
#
# list1 = [10,20,30]
# tuple1 = tuple(list1)
# print(list1,type(list1))
# print(tuple1,type(tuple1))
#
# num = 15
# str1 = str(num)
# print(f'{str1} is a number')


# num = float(input())
# print(2*num)

# print("*")

# num = int(input("Enter number if start to be printed"))
# for i in range(num):
#     print("*",end="")

# num = int(input("Enter number of rows to be printed in pyramid: "))
# for i in range(1,num+1):
#     for j in range(i):
#         print("*",end="")
#     print()


# num = int(input("Enter number of rows: "))
# for i in range(1,num+1):
#     for j in range(num-i+1):
#         print("*",end="")
#     print()

# num = int(input("Enter the number of rows: "))
# for i in range(1,num+1):
#     for j in range(num-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()

# num = int(input("Enter the number of rows: "))
# for i in range(1,num+1):
#     for j in range(num - i):
#         print(" ",end="")
#     for k in range(2*i - 1):
#         print("*",end="")
#     print()

# num = int(input("Enter the number of terms you want in fibonacci: "))
# first = 0
# second = 1
# next_term = 0
# if num == 0:
#     print("Enter a valid number")
# elif num == 1:
#     print(first)
# elif num == 2:
#     print(first)
#     print(second)
# else:
#     print(first)
#     print(second)
#     for i in range(3,num+1):
#         next_term = first + second
#         print(next_term)
#         first = second
#         second = next_term


num = int(input("Enter number of terms you want"))
first = 0
second = 1
next_term = 0
if num < 1:
    print("Enter a valid number")
elif num == 1:
    print(first)
elif num == 2:
    print(first)
    print(second)
else:
    print(first)
    print(second)
    for i in range(3,num+1):
        next_term = first + second
        print(next_term)
        first = second
        second = next_term








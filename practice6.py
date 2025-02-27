# num1 = float(input("Enter First Number: "))
# num2 = float(input("Enter second Number: "))
# print(f"The sum of two number is: {num1+num2}")

# str1 = "       I am not coming you know       "
# print(str1)
# print(str1.strip())

# list = str1.split(" ")
# print(list)
# print("-".join(list))

# str1 = "Python is an amazing programming language"
# print(f"The word 'amazing' starts at {str1.find('amazing')}")

# str1 = "This is String1"
# str2 = str1.replace('String1','String2')
# print(str1)
# print(str2)

# str1 = "Python is a versatile language"
# list1 = str1.split(" ")
# print(list1)
# print("-".join(list1))

# str1 = "Hello"
# str2 = "Hello"
# print(id(str1))
# print(id(str2))

# def function1():
#     print("Function without argument without return type")
#
# def function2(num):
#     for i in range(num):
#         print("Function with argument and without return type")
#
# def function3():
#     return "Function without argument and with return type"
#
# def function4(name):
#     return name
#
# function1()
# function2(4)
# print(function3())
# print(function4("Function with argument and with return type"))

# num = int(input())
# for i in range(num):
#     if i == 5:
#         continue
#     print(f"{i}Printing from 0 to {num-1} skipping 5")

# num = int(input("What table you want to print?"))
#
# for i in range(1,11):
#     print(f"{num} * {i} = {num*i}")

# num = int(input())
# for i in range(1,num+1):
#     if i %2 == 0:
#         print(i)

# num = int(input())
#
# factorial = 1;
# while num > 0:
#     factorial *= num
#     num = num - 1
#
# print(factorial)

# def fibo(num):
#     first = 0
#     second = 1
#     while num > 0:
#         next = first + second
#         print(next)
#         first, second = second, next
#         num = num - 1
# fibo(5)


# def fibo(num):
#     first = 0
#     second = 1
#     if num == 1:
#         print(first)
#     elif num == 2:
#         print(first)
#         print(second)
#     else:
#         print(first)
#         print(second)
#         for i in range(3,num+1):
#             next = first + second
#             print(next)
#             first, second = second, next
# fibo(6)

# num = int(input())
# sum = 0
# while num > 0:
#     rem = num % 10
#     sum = sum + rem
#     num = num // 10
#
# print(sum)

# def reverseNum(num):
#     rev = 0
#     while num > 0:
#         rem = num % 10
#         rev = rev*10 + rem
#         num = num // 10
#     return rev
#
# print(reverseNum(123456))

# def largestInDigit(num):
#     largest = 0
#     while num > 0:
#         rem = num % 10
#         if rem > largest:
#             largest = rem
#         num = num // 10
#     return largest
#
# print(largestInDigit(245869))

# names = ["Rashid","Wajid","Ariz","Maryam"]
# print(names)
# capitalizedName = [name.upper() for name in names]
# print(capitalizedName)

# nums = [[1,2,3],[4,5,6],[7,8,9]]
# print(nums)
#
# flattenedList = [j for num in nums for j in num]
# print(flattenedList)

# nums = [[[1,2], [3,4]], [[5,6], [7,8]]]
# print(nums)
# flattenedList = [k for num in nums for j in num for k in j]
# sum = 0
# for i in flattenedList:
#     sum = sum + i
#
# print(sum/len(flattenedList))

# nums = [1,2,3,4,5,6,7,8,9]
# print(nums)
# squared = [i**2 for i in nums]
# print(squared)

# nums = list(map(int,input().split(" ")))
# numCount = {}
# for num in nums:
#     if num not in numCount:
#         numCount[num] = 1
#     else:
#         numCount[num] += 1
#
# print(numCount)

# numlist = list(map(int,input().strip().split(" ")))
# max = float('-inf')
# min = float('inf')
# for i in numlist:
#     if i > max:
#         max = i
#     if i < min:
#         min = i
# print(f"Minimun is: {min}")
# print(f"Maximum is: {max}")

# numlist = list(map(int,input().strip().split(" ")))
# print(numlist[::-1])

# numlist = tuple(map(int,input().strip().split(" ")))
# oddNum = 0
# evenNum = 0
# for i in numlist:
#     if i%2==0:
#         evenNum = evenNum + 1
#     if i%2!=0:
#         oddNum = oddNum + 1
#
# print(f"There are {evenNum} Even Numbers and {oddNum} Odd Numbers")

# numList = tuple(map(int,input().strip().split(" ")))
# index = int(input())
# for index,num in enumerate(numList):
#     print(f"Index of {num} is {index}")

# tuple1 = tuple(map(int, input().strip().split(" ")))
# print(tuple1[::2])

# words = list(input().split(" "))
# wordCount = {}
# for word in words:
#     word = word.strip("., /")
#     if word not in wordCount:
#         wordCount[word] = 1
#     else:
#         wordCount[word] += 1
#
# print(wordCount)

dict = {}

while True:
    items = input()
    if items.lower() == "done":
        break
    else:
        product, price = items.split(", ")
        dict[product] = price

for key, value in dict.items():
    print(f"{key}: {value}")




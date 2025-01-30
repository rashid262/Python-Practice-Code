#Average Number in The list
#taking user-input and changing it in list
# list1 = list(map(int,input().split(" ")))
# print(list1)
#
# sum = 0
# for i in list1:
#     sum += i
# print(f"Average of numbers is: {sum/len(list1)}")
from operator import indexOf

from peewee import ensure_entity

from Programming.stringValidator import string


# sub-listing using slicing
# list1 = list(map(int,input().split(" ")))
# start = int(input("Start of slicing"))
# end = int(input("End of slicing"))
# print(f"Extracted sublist: {list1[start:end]}")

#list comprehension square

# list1 = list(map(int,input().split(" ")))
# print(f"List of squares: {[x**2 for x in list1]}")

# occurence of each numbers

# list1 = list(map(int,input().split(" ")))
# count_of_occurence = {}
#
# for x in list1:
#     if x in count_of_occurence:
#         count_of_occurence[x] += 1
#     else:
#         count_of_occurence[x] = 1
#
# for key,value in count_of_occurence.items():
#     print(f"{key} occurs {value} times(s)")

#max and min

# def max_min(list1):
#     maxNum = float('-inf')
#     minNum = float('inf')
#     for x in list1:
#         if x > maxNum:
#             maxNum = x
#         if x < minNum:
#             minNum = x
#     print(f"The maximum value is: {maxNum}")
#     print(f"The minimum value is: {minNum}")
# list1 = list(map(int,input().split(" ")))
# max_min(list1)

# # Reversing the list
# list1  = list(map(int,input().split()))
# print(f"List: {list1}")
# print(f"Reversed List: {list1[::-1]}")

#squring numbers
# list1 = list(map(int,input().split(" ")))
# print(f"List of squares: {[x**2 for x in list1]}")
# #count even and odd in tuple
# tuple1 = tuple(map(int,input().split(" ")))
#
# even = 0
# odd = 0
# for x in tuple1:
#     if x%2==0:
#         even += 1
#     else:
#         odd += 1
# print(f"Number of even elements: {even}")
# print(f"Number of odd elements: {odd}")

# sum of all elemenst in tuple

# tuple1 = tuple(map(int,input().split(" ")))
# sum = 0
# for x in tuple1:
#     sum += x
# print(f"The sum of the elements in the tuple is: {sum}")
#index of elements in tuple

# tuple1 = tuple(map(int,input().split(" ")))
# target = int(input())
# flag = False
# for index,y in enumerate():
#     if y == target:
#         print(f"The index of {target} in the tuple is: {index}")
#         flag = True
# 
# if flag == False:
#     print(f"{target}  is not present in the tuple")




# def find_index(tuple1,target):
#     flag = False
#     for index,num in enumerate(tuple1):
#         if num == target:
#             flag = True
#             return index
#         return 0

# tuple1 = tuple(map(int,input().split(" ")))
# target = int(input())
#
# flag = False
#
# for index,num in enumerate(tuple1):
#     if num == target:
#         flag = True
#         print(f"The index of {target} in the tuple is: {index}")
#
# if flag == False:
#     print(f"{target} is not found in the tuple")
#

# tuple1 = tuple(map(int,input().split(" ")))
#
# print(f"Elements at even indices: {tuple1[::2]}")

# #Symmetric difference
# li1 = set(map(int,input().split(" ")))
# li2 = set(map(int,input().split(" ")))
# res = list(li1.symmetric_difference(li2))
# res.sort()
# print(f"Symmetric Difference of elements: {res}")

#check subset

# set1 = set(map(int,input().split(" ")))
# set2 = set(map(int,input().split(" ")))
#
# result = set1.issubset(set2)
# if result == True:
#     print("Set 1 is a subset of Set 2")
# else:
#     print("Set 1 is not a subset of set 2")

# set1 = set(map(int,input().split(" ")))
# set2 = set(map(int,input().split(" ")))
#
# result = list(set1.intersection(set2))
# result.sort()
# print(f"Common elements: {result}")

# set1 = set(map(int,input().split(" ")))
# set2 = set(map(int,input().split(" ")))
#
# result = (set1.difference(set2))
#
# print(f"Elements in Set 1 but not in Set 2: {result}")

#Disjoint

# set1 = set(map(int,input().split(" ")))
# set2 = set(map(int,input().split(" ")))
#
# is_disjoint = set1.isdisjoint(set2)
#
# if is_disjoint:
#     print("The sets are disjoint")
# else:
#     print("The sets are not disjoint")

#occurence of each word in sentence

# words = list(input().split(" "))
# word_count = {}
# for word in words:
#     word = (word.strip(",.!?$")).upper()
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
#
# for key,value in word_count.items():
#     print(f"{key} : {value}")
#
#
# print(word_count)

# contacts = {}
# cont = list(input().split(" "))
# name = cont[0]
# name = name.strip(",")
# number = cont[1]
# print(f"Name: {name} Number: {number}")
# print(cont)


# contacts = {}
# while True:
#     entry = input()
#     if entry.lower() == "done":
#         break
#     else:
#         name, number = entry.split(", ")
#         contacts[name] = number
#
# for key,value in contacts.items():
#     print(f"{key}: {value}")

# sauda = {}
# while True:
#     entry = input()
#     if entry.lower() == "done":
#         break
#     else:
#         name,quantity = entry.split(", ")
#         sauda[name] = quantity
#
# for key,value in sauda.items():
#     print(f"{key}: {value}")


# def cat_hat(str):
#     countcat = 0
#     counthat = 0
#     for i in range(len(str)):
#         temp = str[i:i+3]
#         if temp == "cat":
#             countcat += 1
#         if temp == "hat":
#             counthat += 1
#     return countcat == counthat
#
# str = "hatcatatcathatyatcat"
# print(cat_hat(str))

#
# def count_pattern(str):
#     count = 0
#     for i in range(len(str) - 3):
#         # count "co(any character)d"
#         if str[i:i+2]  == "co" and str[i+3:i+4] == "e":
#             count += 1
#     return count
#
# print(count_pattern("coee"))

# def count_abc_aba(str):
#     count = 0
#     # count abc and aba
#     for i in range(len(str) - 2):
#         if str[i:i+3] == "abc" or str[i:i+3] == "aba":
#             count += 1
#     return count
#
# print(count_abc_aba("abcabacabc"))


# def multiplicationTable(N):## in is a membership operator that is true if something is a member of sequence
#     for i in range(1,11): ## i in range(x,y,z) means i goes from x to y-1 and increments z steps in each iteration
#         print(i * N, end=" ")
#
# print(multiplicationTable(5))

# def fizz_buzz(n):
#     for i in range(1,n+1):
#         if i%3==0:
#             print("Fizz")
#         elif i%5==0:
#             print("Buzz")
#         elif i%5==0 and i%3==0:
#             print("FizzBuzz")
#         else:
#             print(i)
# fizz_buzz(10)

# def reverse_string(str):
#     listr = list(str)
#     start = 0
#     end = len(str) - 1
#     while start <= end:
#         temp = listr[start]
#         listr[str] = listr[end]
#         listr[end] = temp
#     return string(listr)
#
# print(reverse_string("hello"))










































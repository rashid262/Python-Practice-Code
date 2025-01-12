# val1 = 25
# print(val1,type(val1))
# val2 = 3.5
# print(val2,type(val2))
# val3 = True;
# print(val3,type(val3))
# val4 = 'R'
# print(val4,type(val4))
# val5 = 5 + 9j
# print(val5,type(val5))
# val6 = "Rashid"
# print(val6,type(val6))

# # list literals
# fruits = ["apple", "mango", "orange"]
# print(fruits,type(fruits))
#
# #tuple literals
# numbers = (25,45,78,96)
# print(numbers,type(numbers))
#
# #dictionary literals
# alphabets = {'a':'apple', 'b':'ball', 'c':'cat'}
# print(alphabets,type(alphabets))
#
# #set literals
# vowels = {'a','e','i','o','u'}
# print(vowels, type(vowels))

# #python seperator
# print('New Year', 2023, 'See you soon!')

# number = 25
# result = 'pass' if number > 25 else 'fail'


# languages = ['Java', 'Python', 'C++', 'C', 'GoLang', 'SQL']
# n = len(languages)
# for i in range(n):
#     if languages[i] == 'C':
#         continue
#     print(languages[i],end=' ')

# i = 25
# while i > 0:
#     print(i,end=" ")
#     i = i-1

# import random as ran
# lst = [1,2,5,8,9,6,3,4,8,225,95]
# print(ran.choice(lst))

# import math as mt
# print(mt.e)
# print(mt.pi)
# print(mt.cos(mt.pi))
# print(mt.factorial(6))

#python List

# ages = [48,56,25,78,95,14]
# student = ["jack",56,False,["They will not come"],3.6]
# print(student)
#
# # List are ordered
# # List are mutable
# # Lisr allows duplicate
#
# #adding element to list
# ages.append(65)
# print(ages)
#
# #add element at specific index
# ages.insert(25,69)
# print(ages)
#
# # adding two lists
#
# lst1 = [1,2,3,4,5,6,7,8,9]
# lst2 = [10,11,12,13,14,15,16,17,18,19,20]
# lst1.extend(lst2)
# print(lst1)
# print(lst2)

#remove element from list

# lst5 = ["Rashid","Wajid","Ariz"]
# print(lst5)
#
# lst5.remove("Wajid")
# print(lst5)

#delete using indexing

# lst1 = ["Hello","I am","Not","Coming"]
# print(lst1)
# del lst1[-3:2]
# print(lst1)

# fruits = ['apple', 'banana', 'orange']
# # for i in fruits:
# #     print(i)
#
# # print('apple' in fruits)
#
# #Python Tuple
#
# numbers = (1,2,5,8,9,6,3,4,78,5)
# print(type(numbers))

# Tuple are ordered
# Tuple are immutable
# Tuple allows duplicate

# Python Set
"""
Set don't allow duplicate
Set are mutable
Set don't maintain order
"""

# # create a set of integer type
# student_id = {112, 114, 116, 118, 115}
# print('Student ID:', student_id)
#
# # create a set of string type
# vowel_letters = {'a', 'e', 'i', 'o', 'o', 'u'}
# print('Vowel Letters:', vowel_letters)
#
# # create a set of mixed data types
# mixed_set = {'Hello', 101, -2, 'Bye'}
# print('Set of mixed data types:', mixed_set)

#Create empty set in python

# set1 = set()
# dict1 = {}
# print(type(set1))
# print(type(dict1))

#remove element from set
#
# languages = {'Swift', 'Java', 'Python'}
# print(languages)
# languages.discard("Swift")
# print(languages)

# #Python set operations
# #UNION
# A = {1,3,5}
# B = {0,2,4}
# #union using |
# print("Union using | : ", A | B)
# #union using union()
# print("Union using union(): ",A.union(B))

#INTERSECTION
# A = {1,3,5}
# B = {1,2,3}
# #intersection using &
# print(A & B)
# #Intersection using intersection()
# print(A.intersection(B))

#DIFFERENCE
# first set
# A = {2, 3, 5}
#
# # second set
# B = {1, 2, 6}
#
# # perform difference operation using &
# print('Difference using &:', A - B)
#
# # perform difference operation using difference()
# print('Difference using difference():', A.difference(B))

#SYMMETRIC DIFFERENCE

# # first set
# A = {2, 3, 5}
#
# # second set
# B = {1, 2, 6}
#
# # perform difference operation using &
# print('using ^:', A ^ B)
#
# # using symmetric_difference()
# print('using symmetric_difference():', A.symmetric_difference(B))

#Python dictionary

#Dictionary keys must be immutable, such as tuples,
# strings, integers, etc. We cannot use mutable (changeable)
# objects such as lists as keys.

# creating a dictionary
# country_capitals = {
#   "Germany": "Berlin",
#   "Canada": "Ottawa",
#   "England": "London"
# }
# for i in country_capitals:
#     capital = country_capitals[i]
#     print(i," :- ",capital)




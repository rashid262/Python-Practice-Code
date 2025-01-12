# #if string is holding int it can be converted into int
# a = '30'
# b = int(a)
# print(a,type(a))
# print(b,type(b))
#
# #if string is holding string it can't be converted into int
# x = 'Kod'
# print(x,type(x))
# y = int(x)
# print(y,type(y)) #wrong way
from traceback import print_tb

#string holding float is allowed to be converted to float
# p = '3.5'
# print(p,type(p))
# q = float(p)
# print(q,type(q))
#
# q = ''
# q = bool(q)
# print(q,type(q))

'''1. While converting int to bool for all non zero values we will get true
 2. While converting int to bool for 0 and empty strings we will get false'''

# print(bool('Kodnest')) #True
# print(int('Kod')) #Error
# print(int('11')) #True
# print(float('Kodnest')) #Error
# print(float('2.2')) #True
# print(bool('')) #False
# print(bool(0)) #False
# print(bool(12)) # True
# print(int('22.22')) # Error

value = int(float(input("Enter price in float: ")))
print(value,type(value))



# # map(function, iterable_object) --> it will return iterator object
#
# def double(x):
#     return int(x)
#
# li = [1,2,3,4,5]
#
# double_li = map(double, li)
#
# print(list(double_li))
#
# tup = ('10','20','30')
#
# print(list(map(double,tup)))

li2 = [1,5,66]

print(list(map(float,li2)))

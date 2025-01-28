# li = [10,20,30]
#
# for idx, ele in enumerate(li):
#     print(idx,ele)

"""
Write a python program to print all Even index elements
"""

li = [10,20,30,40,50,60]
for idx,ele in enumerate(li,start=1):
    if idx%2==0:
        print(idx,ele)


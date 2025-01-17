# li = [10,20,30,40,50,60,70,80,90,100]
# print("Before Reverse:" ,li)
# li.reverse()
# print("After reverse:", li)

"""
Reverse method will reverse the original object 
"""

li2 = [11,22,33,44,55]
revli2 = reversed(li2)  #it will always return iteratable object
print(list(revli2))
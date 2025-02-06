import time

li1 = [1,2,3,4,5,6,7,8,9]
li2 = ['a','b','c','d','e']

def displayDigit(li1):
    for i in li1:
        print(i,end=" ")
    time.sleep(3)
def displayAlpha(li2):
    for i in li2:
        print(i,end=" ")


displayDigit(li1)
print()
displayAlpha(li2)
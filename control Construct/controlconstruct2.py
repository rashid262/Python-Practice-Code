"""
for control_variable in range() <-- (iterable object will go here)
"""
"""
range(5) ---> 5 is end
range(5,10) --> 5 is start 10 is end # 5,6,7,8,9
range(1,11,2) -->1 is start 11 is end and 2 is step 1,3,5,7,9
"""
# for i in 'Kodnest':
#     print(i,end="*")

# for j in [10,20,30,40,50,60,70,80,90]:
#     print(j)

# for i in range(1,11):
#     print(i,end=" ")

# for i in range(1,20,2):
#     print(i,end=" ")
# print("Even Numbers: ")
# for i in range(1,11):
#     if i%2==0 :
#         print(i,end=" ")


# i = 0
# while i < 10:
#     print(i+100)
#     i = i+1

def jumpstatement(num):
    for i in range(1,num+1):
        if i == 6:
            continue
        print(i)
jumpstatement(10)

def jumpstatement(num):
    for i in range(1,num+1):
        if i == 5:
            break
        print(i)
jumpstatement(10)
# simple row and col patter

# row = 4
# col = 5
# for i in range(1,row+1):
#     for j in range(col):
#         print("*",end=" ")
#     print()

num = int(input())

for i in range(1,num+1):
    for j in range(i):
        print("*",end=" ")
    print()

for k in range(1,num + 1):
    for l in range(num - k):
        print("*", end=" ")
    print()
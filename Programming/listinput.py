# li = []
# num = int(input("Enter count: "))
#
# for i in range(num):
#     li.append(int(input(f"Enter {i+1} Element: ")))
#
# print(li)

# #space separated element input
# li = input("Enter space separated elements: ")
# print(li)
#
# li = li.split(" ")
#
# print(list(map(int, li)))

# tup = tuple(map(int, input("Enter SPace seperated element").split()))
#
# print(tup,type(tup))

# li = list(map(int,input("Enter space separated input: ").split(" ")))
# print([i for i in li if i%2==0])

# [[10,20,],[30,40],[50,60]]
# li = []
# num = int(input("How many sublist you want?: "))
# for i in range(num):

num = input("Enter space separated element: ").split(" ")
print(list(map(int,num)))




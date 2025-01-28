# if __name__ == '__main__':
#     N = int(input())
#     list1 = []
#     for x in range(N):
#         command = input("").strip().split()
#         action = command[0]
#         if action == "insert":
#             index, value = int(command[1]), int(command[2])
#             list1.insert(index, value)
#         elif action == "print":
#             print(list1)
#         elif action == "remove":
#             value = int(command[1])
#             list1.remove(value)
#         elif action == "append":
#             value = int(command[1])
#             list1.append(value)
#         elif action == "sort":
#             list1.sort()
#         elif action == "pop":
#             list1.pop()
#         else:
#             list1.reverse()
#

li = []
n = int(input("How many operation you want to perform? "))
for i in range(n):
    command = input(f"Insert {i+1} command: ").split(" ")
    task = command[0]
    if task == "insert":
        value = int(command[1])
        index = int(command[2])
        li.insert(index,value)
    elif task == "print":
        print(li)
    elif task == "remove":
        li.reverse()
    elif task == "append":
        value = int(command[1])
        li.append(value)
    elif task == "sort":
        li.sort()
    elif task == "pop":
        li.pop()
    else:
        li.reverse()
    

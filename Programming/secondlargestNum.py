# scores = list(map(int,input("Enter scores in coma separated format: ").split(" ")))
#
# set1 = set(scores)
# new_list = list(set1)
# new_list.sort()
#
# print(new_list)
# print(new_list[-2])

# second smallest element

num = list(map(int,input("Enter comma separated elements: ").split(",")))

set1 = set(num)
new_list = list(set1)
new_list.sort()
print(new_list)
print(new_list[1])



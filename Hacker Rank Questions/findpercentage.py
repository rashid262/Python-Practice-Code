dict1 = {}
n = int(input("How many Data will You Enter? "))
for i in range(n):
    name, *score = input("Insert name and marks separated by space: ").split(" ")
    score = list(map(float,score))
    dict1[name] = score
    
target_name = input("Insert the target name you want average of: ")
for name, score in dict1.items():
    if name == target_name:
        print(sum(dict1[target_name])/len(dict1[target_name]))
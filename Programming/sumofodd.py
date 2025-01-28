num = int(input("Upto wat number you want sum odd numbers: "))
sum = 0
for i in range(1,num+1):
    if i%2!=0:
        sum += i
print(f"The sum of all odd numbers between 1 and {num} is {sum}")

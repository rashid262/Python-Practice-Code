num = int(input("Enter upto which you want sum of natural numbers: "))
temp = num
sum = 0
while num >= 1:
    sum += num
    num -= 1
print(f"The sum of first {temp} numbers is {sum}")
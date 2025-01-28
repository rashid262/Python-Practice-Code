num = int(input("Upto which digit you want sum of square: "))

sum = 0
while num >= 1:
    sum += num ** 2
    num  = num - 1
print(f"Sum of the square of first {num} numbers is: {sum} ")
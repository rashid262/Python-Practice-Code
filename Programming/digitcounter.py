num = int(input("Enter the number from which you want to count digit: "))

temp = num
count = 0

while temp > 0:
    count += 1
    temp //=10
print(f"The number {num} has {count} digits.")
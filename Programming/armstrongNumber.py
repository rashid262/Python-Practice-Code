def digitCount(num):
    count = 0
    while num > 0:
        count = count + 1
        num = num // 10
    return count

def arsmtrongCheck(num):
    temp = num
    sum = 0
    rem = 0
    while num > 0:
        rem = num % 10
        sum = sum + rem**digitCount(temp)
        num = num // 10
    return temp == sum

num  = int(input("Enter a number to check for Armstrong: "))





print(arsmtrongCheck(num))






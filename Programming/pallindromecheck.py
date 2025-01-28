def pallindromeCcheck(num):
    temp = num
    rev = 0
    while num > 0:
        rem = num % 10
        rev = rev*10 + rem
        num = num // 10
    return temp == rev

num = int(input("Enter number to check for palindrome: "))
if num <= 0:
    print("Enter a positive number.")
else:
    print(pallindromeCcheck(num))
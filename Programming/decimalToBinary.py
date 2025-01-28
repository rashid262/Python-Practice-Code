def binaryDecimal(decimal):
    binary = ""
    rem = 0
    if decimal == 0:
        return 0
    else:
        while decimal > 0:
            rem = decimal % 2
            binary =  str(rem) + binary
            decimal = decimal // 2
    return binary

num = int(input("Enter a number in Decimal: "))

print(binaryDecimal(num))
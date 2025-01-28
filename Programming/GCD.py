def findgcd(a, b):
    while b > 0:
        rem = a % b
        a = b
        b = rem
    return a

print(findgcd(8,12))
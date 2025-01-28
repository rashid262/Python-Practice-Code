def isPerfectSquare(num):
    for i in range(1,num+1):
        if i*i == num:
            return True
    return False

print(isPerfectSquare(9))
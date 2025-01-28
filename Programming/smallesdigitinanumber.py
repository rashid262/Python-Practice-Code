def smallest(num):
    min = float("inf")
    while num > 0:
        rem = num % 10
        if rem < min:
            min = rem
        num = num // 10
    return min

print(smallest(981273))
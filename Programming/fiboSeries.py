def fiboseries(num):
    first, second = 0, 1
    if num >= 1:
        print(first)
    if num >= 2:
        print(second)
    for i in range(2, num):
        next_num = first + second
        print(next_num)
        first, second = second, next_num

num = int(input("How many number you want to print in series? "))
if num <= 0:
    print("Please enter a positive number greater than zero.........")
else:
    fiboseries(num)
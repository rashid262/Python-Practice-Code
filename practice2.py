#sum of digits

# num = int(input("Enter a number to find sum of it's digit "))
# n = num
# sum = 0
# rem = 0
#
# while n > 0:
#     rem = n % 10
#     sum = sum + rem
#     n = int(n / 10)
# print(f"The sum of the digits is {sum}")

#reverse the number
# num = int(input("Enter a number to reverse: "))
# n = num
# reverse = 0
# rem = 0
# while n > 0:
#     rem = n % 10
#     reverse = reverse * 10 + rem
#     n = int(n / 10)
# print(f"Reverse of {num} is {reverse}")

#largest digit in a number
#
# num = int(input())
# rem = 0
# largest = float('-inf')
# smallest = float('inf')
# while num > 0:
#     rem = num % 10
#     if rem > largest:
#         largest = rem
#     num = int(num / 10)
# print(f'The largest digit is {largest}.')

#last even digit

# num = int(input())
# n = num
# rem = 0
# while n > 0:
#     rem = n % 10
#     if rem % 2 == 0:
#         print(f"The last even digit in {num} is {rem}.")
#         break
#     else:
#         print("No even digit found.")

# printing even digit from a number in order
# num = int(input())
# n = num
# even_digits = []
# while n > 0:
#     digit = n % 10
#     if digit % 2 == 0:
#         even_digits.append(str(digit))
#     n = n // 10
#
# if even_digits:
#     even_digits.reverse()
#     print(f"The even digits in {num} are: {' '.join(even_digits)}")
# else:
#     print(f"No even digits found in {num}.")


# num = int(input())
#
# for i in range(1,num+1):
#     for j in range(num - i):
#             print(" ",end="")
#     print("*",end="")
#     for
#     print()








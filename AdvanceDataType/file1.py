numbers = [10,20,30,40,50,60,70,60,60]
print(numbers)
numbers.append(80)
print(numbers)
numbers.remove(50)
print(numbers)
def count_occurence(num,numbers):
    count = 0
    for x in numbers:
        if x == num:
            count += 1
    return count
print(60,count_occurence(60,[10,20,30,40,50,60,70,60,60]))

def reverse_num(numbers):
    start = 0
    end = len(numbers) - 1
    while start <= end:
        temp = numbers[start]
        numbers[start] = numbers[end]
        numbers[end] = temp
    return numbers

print(f"Reversed Numbers {reverse_num([10,20,30,40,50,60,70,60,60])}")

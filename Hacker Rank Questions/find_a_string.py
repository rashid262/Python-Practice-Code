string = input("Enter your string: ")
substring = input("Enter your substr: ")

def count_substr(string, substring):
    count = 0
    n = len(string) - len(substring) + 1
    for i in range(n):
        if substring == string[i:len(substring)+i]:
            count += 1
    return count

print(count_substr(string, substring))




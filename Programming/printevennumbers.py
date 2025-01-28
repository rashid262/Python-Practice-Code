num = int(input("How many even number you want to print?: "))

print(f"The first {num} even Numbers are: ")
for i in range(2,num*2+1,2):
    print(i)


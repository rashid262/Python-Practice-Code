string = input("Enter string: ")


print(any([i.isalnum() for i in string]))
print(any([i.isalpha() for i in string]))
print(any([i.isnumeric() for i in string]))
print(any([i.islower() for i in string]))
print(any([i.isupper() for i in string]))

#ant(iterator) this will return true if any og the inner value will be true
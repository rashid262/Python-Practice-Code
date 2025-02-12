li = [10,20,30,40]
print(type(li),li)
iteratorobj = iter(li)
# we can convert iterable object (list,set,range() etc) as iterator
print(type(iteratorobj),iteratorobj)

print(next(iteratorobj))
print(next(iteratorobj))
print(next(iteratorobj))
print(next(iteratorobj))
print(next(iteratorobj)) #StopIteration

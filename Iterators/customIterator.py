class Counter:
    def __init__(self,limit):
        self.limit = limit
        self.count = 0

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            return self.count
    
count1 = Counter(5)
# print(next(count1))
# print(next(count1))
# print(next(count1))
# print(next(count1))
# print(next(count1))
print(count1.__next__())
print(count1.__next__())
print(count1.__next__())
print(count1.__next__())
print(count1.__next__())
#both will call same method

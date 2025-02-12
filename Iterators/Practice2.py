# class CountUpTo:
#     def __init__(self,limit):
#         self.limit = limit
#         self.current = 0
#
#     def __iter__(self):
#         return  self
#
#     def __next__(self):
#         if self.current < self.limit:
#             self.current += 1
#             return self.current
#         else:
#             raise StopIteration
#
# counter = CountUpTo(10)
#
# for num in counter:
#     print(num)
class EvenNumber:
    def __init__(self,limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit < self.current:
            raise StopIteration
        even_num = self.current
        self.current += 2
        return even_num

num = int(input())
even_number = EvenNumber(num)

for num in even_number:
    print(num)



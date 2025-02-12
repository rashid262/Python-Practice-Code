class Fibonacci:
    def __init__(self, max_value):
        self.max_value = max_value
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max_value:
            raise StopIteration
        fib_number = self.a
        self.a, self.b = self.b, self.a + self.b
        return fib_number


num = int(input())

fib1 = Fibonacci(num)

for num in fib1:
    print(num)
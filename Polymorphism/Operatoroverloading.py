"""
in python if we print reference variable
then internally python will invoke __str__() which will display string representation
of an address of an object

so in the above example we have overridden 
__str__ method in their respective classes
"""

# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     # overloading the + operator
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
# p1 = Point(2,3)
# p2 = Point(4,5)
# p3 = p1+p2
# print(p3)

class ComplexNumber:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def __add__(self,other):
        return f"({self.real + other.real}, {self.imag + self.imag})"
    def __mul__(self,other):
        return f"({self.real * other.real}, {self.imag * self.imag})"

real1 = int(input())
img1 = int(input())
real2 = int(input())
img2 = int(input())


comp1 = ComplexNumber(real1,img1)
comp2 = ComplexNumber(real2,img2)

print(f"Sum: {comp1 + comp2}")
print(f"Product: {comp1 * comp2}")


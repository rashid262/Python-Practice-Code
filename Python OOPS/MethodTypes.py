# Instance Method

"""
These are the most common type of methods.
They operate on an instance of the class and can access and modify the instance's attributes.
Instance methods require a reference to the instance (self) as the first parameter.
"""
from operators import result


class Person:
    #Construtor
    def __init__(self,name, age):
        self.name = name
        self.age = age  
    #Instance Method
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person = Person("Rashid",24)
print(person.greet())

#Class Method

""" 
Class methods operate on the class itself,
not on instances of the class. 
They are defined using the @classmethod decorator and take cls as the first parameter,
which represents the class.
"""

class Circle:
    pi = 3.14
    
    def __init__(self,radius):
        self.radius = radius
    #Class Method
    @classmethod
    def from_diameter(cls,diameter):
        radius = diameter/2
        return cls(radius)

# Create an instance using the class method
circle = Circle.from_diameter(10)
print(circle.radius)  # Output: 5.0

#Static Method

"""
Static methods don’t operate on an instance or class.
They behave like regular functions but belong to the class's namespace.
These are defined using the @staticmethod decorator and do not take self or cls as a parameter.
"""

class MathUtils:
    @staticmethod
    def add(a,b):
        return a+b
result = MathUtils.add(25,65)
print(result)

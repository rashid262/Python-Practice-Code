#Polymorphism using method overriding
class Calculator:
    def calculate(self,a,b):
        print("Calculation of a and b")
class Add(Calculator):
    def calculate(self,a,b):
        print("Addition:",a+b)
class Sub(Calculator):
    def calculate(self,a,b):
        print("Subtraction:",a-b)
class Mul(Calculator):
    pass

ref = Calculator()
ref.calculate(25,52)
ref = Add()
ref.calculate(25,45)
ref = Sub()
ref.calculate(6,3)
ref = Mul()
ref.calculate(54,65)
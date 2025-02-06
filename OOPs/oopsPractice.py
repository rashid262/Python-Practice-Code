# class A:
#     def method_A(self):
#         print("From Class A Method_A")
# class B(A):
#     def method_B(self):
#         print("From Class B Method_B")
# class C(B):
#     def method_C(self):
#         print("From Class C Method_C")
#
# c1 = C()
# c1.method_A()
# c1.method_B()
# c1.method_C()

class Person:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        print(f"My name is {self.name}")

class Employee:
        def work(self):
            print("Employee Work")
class Manager(Person,Employee):
    def __init__(self,name):
        super().__init__(name)
    def manage(self):
        print("Manager Manages")

manager = Manager("Rashid")
manager.introduce()
manager.work()
manager.manage()
from traceback import print_tb


class GrandParent:
    def __init__(self):
        self.x = 100
class Parent(GrandParent):
    def __init__(self):
        self.y = 200
        super().__init__()
class Child(Parent):
    def __init__(self):
        self.z = 300
        super().__init__()

ch = Child()
print(ch.z)
print(ch.y)
print(ch.x)


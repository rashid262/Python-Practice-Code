class GrandParent:
    def cook(self):
        print("Grandparent Can cook Biryani")


class Parent(GrandParent):
    def cook(self):
        print("Parent can cook maggie")


class Child(Parent):
    def cook(self):
        super(Parent,self).cook()
        super().cook()
        print("Child won't  cook")


ch = Child()
ch.cook()
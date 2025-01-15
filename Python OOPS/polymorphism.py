class Bird:
    def fly(self):
        print("Birds can generally fly")
class Penguin(Bird):
    def fly(self):
        print("Penguins can't fly but can swim")
myBird = Bird()
myBird.fly()
myPeng = Penguin()
myPeng.fly()
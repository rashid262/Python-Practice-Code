# class Dog:
#     def speak(self):
#         print("Bhaw Bhaw")
# class Cat:
#     def speak(self):
#         print("Meao Meaw")
# class Horse:
#     def speak(self):
#         print("Hiinnnnnn")
#
# def make_it_speak(animal):
#     animal.speak()
#
# dog1 = Dog()
# cat1 = Cat()
# horse1 = Horse()
#
# make_it_speak(dog1)
# make_it_speak(cat1)
# make_it_speak(horse1)


class Bird:
    def fly(self):
        print("Bird is flying")
class Aeroplane:
    def fly(self):
        print("Aeroplane is flying")

def make_it_fly(flying):
    flying.fly()

bird1 = Bird()
aeroplane1 = Aeroplane()

make_it_fly(bird1)
make_it_fly(aeroplane1)

class Demo1:
    def __init__(self,name):
        self.__name = name

d1 = Demo1("Akash")
#print(d1.__name) #error
print(d1._Demo1__name) #NameMangling

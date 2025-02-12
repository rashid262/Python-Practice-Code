# def decor(func):
#     def inner(name):
#         if name == "Ayush":
#             print(name, "Is Learning Java")
#         else:
#             func(name)
#     return inner
#
# @decor
# def choice(name):
#     print(name,"Is Learning Python")
#
# choice("Ayush")
# choice("Akash")

# def smartdiv(func):
#     def inner(a,b):
#         if b == 0:
#             print("B should not be 0")
#         else:
#             func(a,b)
#         return inner
# @smartdiv
# def div(a,b):
#     print("Division is: ",a/b)
#
# div(10,2)
# div(25,0)
#
#
# def repeatDecor(func):
#     def inner(a,b):
#         if b == 0:
#             print("B should not be 0")
#         else:
#             func(a,b)
#         return inner
# @smartdiv
# def div(a,b):
#     print("Division is: ",a/b)
#
# div(10,2)
# div(25,0)

def repeat(num):
    def outer(func):
        def inner():
            for i in range(num):
                func()
        return inner
    return outer

@repeat(num = 3)
def msg():
    print("Hello")
msg()
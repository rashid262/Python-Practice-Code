# function without parameter and without return statement
def add():
    a = 10
    b = 20
    print("Addition of two number is: ",a+b)

#function with parameter and without return statement

def add1(a,b):
    print("Addition of two number is:",a+b)


#function without parameter and with return statement

def add2():
    return 10+20

#function with  parameter and with return statement

def add3(a,b):
    return a+ b

add()
add1(10,20)
print(add2())
print((add3(25,35)))

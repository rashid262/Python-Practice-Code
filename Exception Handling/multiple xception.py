def disp(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("ZeroDivision Occurred and Handled")
    except NameError:
        print("Name error occurred and handled")
    except TypeError:
        print("Type error occurred and handled")
    except:
        print("Some error occurred and handled")
    #this is default except block this will always in last
    #if no upper exception matches then default block will catch


disp(15,0)
disp(15,45)
disp(15,"b")

def disp(a,b):
    try:
        print("Task Started")
        print(a / b)
    except:
        print("Some error occurred and handled")
    else:
        print("Task Executed without any exception")
    finally:
        print("Task Ended")


disp(25,0)
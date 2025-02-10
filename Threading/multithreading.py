# single thread is controlling ths code in a sequential manner

import threading
import time
li1 = [1,2,3,4,5,6,7,8,9]
li2 = ['a','b','c','d','e']

def displayDigit(li1):
    print(threading.current_thread())
    for i in li1:
        print(i,end=" ")
        time.sleep(0.5)
def displayAlpha(li2):
    print(threading.current_thread())
    for i in li2:
        print(i,end=" ")
        time.sleep(0.5)

t1 = threading.Thread(target=displayAlpha,args=(li2,),name="Tester")
print()
t2 = threading.Thread(target=displayDigit,args=(li1,),name="Developer")

t1.start()
t2.start()




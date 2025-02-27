# # single thread is controlling ths code in a sequential manner
#
# import threading
# import time
#
# li1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# li2 = ['a', 'b', 'c', 'd', 'e']
#
# def displayDigit(li):
#     print(threading.current_thread().name)
#     for i in li:
#         print(i, end=" ")
#         time.sleep(1)
#     print()
#
# def displayAlpha(li):
#     print(threading.current_thread().name)
#     for i in li:
#         print(i, end=" ")
#         time.sleep(1)
#     print()
#
# # Correct way: Pass function reference and arguments using args=
# t1 = threading.Thread(target=displayDigit, args=(li1,))
# t2 = threading.Thread(target=displayAlpha, args=(li2,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#


import threading
import time

def task():
    for i in range(5):
        print(f"Task running: {i}")
        time.sleep(1)

t = threading.Thread(target=task)
t.start()  # 🚀 Thread starts running

print("Main thread is free!")  # 🏃‍♂️ Main thread does not wait for `t`
print("Main thread finished!")  # 💨 Main thread exits while `t` is still running


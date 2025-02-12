# import threading
# #1. Start()
# def print_hello():
#     print("Hello from thread!")
#
# # Create a thread
# thread = threading.Thread(target=print_hello)
# thread.start()  # Start the thread

#2. Join()
# import threading
#
# def print_numbers():
#     for i in range(1, 4):
#         print(f"Number: {i}")
#
# # Create a thread
# thread = threading.Thread(target=print_numbers)
# thread.start()
# thread.join()  # Wait until thread completes
#
# print("Thread has completed, continuing the program.")
#is_alive()

# import threading
# import time
#
# def print_message():
#     time.sleep(2)
#     print("Message from thread!")
#
# # Create and start a thread
# thread = threading.Thread(target=print_message)
# thread.start()
#
# # Check if the thread is alive
# print(f"Is thread alive? {thread.is_alive()}")

import threading
import time


def print_task(task_name):
    print(f"Task '{task_name}' started.")
    # Simulate a delay representing the time taken to print
    time.sleep(2)  # Adjust this value for longer or shorter task simulation
    print(f"Task '{task_name}' completed.")


def main():
    tasks = []
    num_tasks = int(input("Enter the number of print tasks: "))

    for i in range(num_tasks):
        task_name = input(f"Enter the name for task {i + 1}: ")
        tasks.append(task_name)

    threads = []

    for task in tasks:
        # Create a thread for each print task
        thread = threading.Thread(target=print_task, args=(task,))
        threads.append(thread)
        thread.start()  # Start the thread

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All tasks are completed.")


if __name__ == "__main__":
    main()
#Manual way to do this task
# def greet():
#     print("Hello")
#
# def enhanced_greet():
#     print("Welcome")
#     greet()
#
# enhanced_greet()

#Now Decorator
#first we create decorator function
# def decorator_function(original_function):
#     def wrapper_function():
#         print("Welcome")
#         original_function()
#     return wrapper_function()
#
# @decorator_function
# def greet():
#     print("Hello")

def repeat_decorator(times):
    def decorator_function(original_function):
        def wrapper():
            for _ in range(times):
                original_function()
        return wrapper
    return decorator_function

@repeat_decorator(3)
def greet():
    print("Hello World")

greet()









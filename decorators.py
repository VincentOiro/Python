# A decorator is a function that takes another function as its argument
# and extends or modifies its behavior without explicitly modifying it

def my_decorator(original_func):
   # The wrapper function is defined to wrap the original function
   def wrapper():
       # Code before the original function
       print("Before calling the function")

       # Call the original function
       original_func()

       # Code after the original function
       print("After calling the function")

   # The wrapper function is returned and replaces the original function
   return wrapper

# The say_hello function is decorated with my_decorator
@my_decorator
def say_hello():
   print('hello world is decorated!')

# The say_hello function is called and the output includes the output from the decorator
say_hello()
# Output:
# Before calling the function
# hello world is decorated!
# After calling the function
# PYTHON DECORATORS - Complete Guide

"""
What is a Decorator?

A DECORATOR is a function that WRAPS another function or class
and modifies its behavior WITHOUT changing the original function.

Think of it like:
    - Original function = Gift (function code)
    - Decorator = Gift wrapper (adds functionality around the gift)
    - Result = Same gift, but with added decoration/functionality

Syntax:
    @decorator_name
    def my_function():
        pass
    
This is equivalent to:
    def my_function():
        pass
    my_function = decorator_name(my_function)
"""

print("=" * 60)
print("1. SIMPLE DECORATOR EXAMPLE")
print("=" * 60 + "\n")

# Step 1: Create a simple decorator
def my_decorator(func):
    """
    This is a decorator function.
    It takes a function as input and returns a modified version.
    """
    def wrapper():
        print("BEFORE function runs")
        func()  # Call the original function
        print("AFTER function runs")
    return wrapper


# Step 2: Use the decorator
@my_decorator
def say_hello():
    print("Hello World!")


# When we call say_hello(), the decorator wrapper is called instead
print("Calling say_hello():")
say_hello()


print("\n" + "=" * 60)
print("2. DECORATOR WITH ARGUMENTS")
print("=" * 60 + "\n")

def my_decorator_with_args(func):
    def wrapper(*args, **kwargs):
        """
        *args   = captures positional arguments
        **kwargs = captures keyword arguments
        """
        print(f"Function {func.__name__} was called with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)  # Call original function
        print(f"Function returned: {result}")
        return result
    return wrapper


@my_decorator_with_args
def add(a, b):
    """Add two numbers"""
    return a + b


print("Calling add(5, 10):")
result = add(5, 10)

print("\nCalling add(3, 7):")
result = add(3, 7)


print("\n" + "=" * 60)
print("3. TIMING DECORATOR (Practical Example)")
print("=" * 60 + "\n")

import time

def timer_decorator(func):
    """This decorator measures how long a function takes to run"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(f"[TIMER] {func.__name__} took {execution_time:.4f} seconds")
        return result
    return wrapper


@timer_decorator
def slow_function():
    print("Running slow function...")
    time.sleep(0.5)
    print("Done!")


print("Calling slow_function():")
slow_function()


print("\n" + "=" * 60)
print("4. LOGGING DECORATOR")
print("=" * 60 + "\n")

def logging_decorator(func):
    """This decorator logs when a function is called and what it returns"""
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling function: {func.__name__}")
        print(f"[LOG] Arguments: {args}, {kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"[LOG] Returned: {result}")
        return result
    return wrapper


@logging_decorator
def multiply(a, b):
    return a * b


print("Calling multiply(3, 4):")
multiply(3, 4)


print("\n" + "=" * 60)
print("5. MULTIPLE DECORATORS (Decorator Stacking)")
print("=" * 60 + "\n")

def decorator1(func):
    def wrapper():
        print("1. Decorator 1 - BEFORE")
        func()
        print("1. Decorator 1 - AFTER")
    return wrapper


def decorator2(func):
    def wrapper():
        print("2. Decorator 2 - BEFORE")
        func()
        print("2. Decorator 2 - AFTER")
    return wrapper


@decorator1
@decorator2
def greet():
    print("HELLO!")


print("Calling greet() with multiple decorators:")
print("Note: Decorators are applied bottom-to-top\n")
greet()


print("\n" + "=" * 60)
print("6. DECORATOR WITH PARAMETERS")
print("=" * 60 + "\n")

def repeat(times):
    """Decorator that repeats function execution"""
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            result = None
            for i in range(times):
                print(f"[Execution {i+1}/{times}]")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(times=3)
def say_name():
    print("My name is Sagiruddin")


print("Calling say_name() with @repeat(times=3):\n")
say_name()


print("\n" + "=" * 60)
print("7. VALIDATION DECORATOR (Real-world Example)")
print("=" * 60 + "\n")

def validate_positive(func):
    """Decorator that validates function arguments are positive"""
    def wrapper(*args, **kwargs):
        # Check if all args are positive
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                print(f"ERROR: {func.__name__} received negative number: {arg}")
                return None
        
        # If validation passes, call the function
        result = func(*args, **kwargs)
        return result
    return wrapper


@validate_positive
def calculate_square_root(num):
    return num ** 0.5


print("Calling calculate_square_root(16):")
print(f"Result: {calculate_square_root(16)}")

print("\nCalling calculate_square_root(-4) [should fail validation]:")
print(f"Result: {calculate_square_root(-4)}")


print("\n" + "=" * 60)
print("8. CLASS DECORATOR")
print("=" * 60 + "\n")

def add_method(cls):
    """Decorator that adds a method to a class"""
    def new_method(self):
        return f"Hello from {cls.__name__}"
    
    cls.greet = new_method
    return cls


@add_method
class Person:
    def __init__(self, name):
        self.name = name


person = Person("Ali")
print(f"person.greet() = {person.greet()}")


print("\n" + "=" * 60)
print("KEY CONCEPTS SUMMARY")
print("=" * 60)
print("""
1. DECORATOR BASICS:
   - Takes a function/class as input
   - Wraps it with additional functionality
   - Returns the modified version
   - Uses @ syntax for clean code

2. DECORATOR STRUCTURE:
   def decorator(func):
       def wrapper(*args, **kwargs):
           # Code BEFORE function
           result = func(*args, **kwargs)
           # Code AFTER function
           return result
       return wrapper

3. USE CASES:
   - Timing/Performance measurement
   - Logging and debugging
   - Input validation
   - Caching/Memoization
   - Access control/Authentication
   - Modifying function behavior
   - Adding features without changing original code

4. ADVANTAGES:
   - Reusable code
   - Clean syntax with @
   - No modification to original function
   - Easy to stack multiple decorators
   - Separation of concerns
""")

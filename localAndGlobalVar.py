# =============================================
# LOCAL AND GLOBAL VARIABLES IN PYTHON
# =============================================

# =============================================
# 1. GLOBAL VARIABLES
# =============================================

# Variables defined outside functions are GLOBAL
# They can be accessed from anywhere in the program

name = "Alice"  # GLOBAL variable
age = 25  # GLOBAL variable


def display_global():
    """Function that accesses global variables"""
    print(f"Global name: {name}")
    print(f"Global age: {age}")


display_global()


# =============================================
# 2. LOCAL VARIABLES
# =============================================

# Variables defined inside functions are LOCAL
# They only exist inside that function

def greet():
    """Function with local variables"""
    message = "Hello!"  # LOCAL variable (only exists in this function)
    local_age = 30  # LOCAL variable
    print(message)
    print(local_age)


greet()

# Trying to access local variables outside the function will cause an error
# print(message)  # ERROR! NameError: name 'message' is not defined


# =============================================
# 3. GLOBAL vs LOCAL SCOPE
# =============================================

country = "Australia"  # GLOBAL


def show_scope():
    city = "Karachi"  # LOCAL
    print(f"Global country: {country}")  # Can access global
    print(f"Local city: {city}")


show_scope()
print(country)  # Works - it's global
# print(city)  # ERROR - it's local to function


# =============================================
# 4. SHADOWING (Local variable hides global)
# =============================================

x = 10  # GLOBAL


def example_shadowing():
    x = 20  # LOCAL variable with same name (shadows global)
    print(f"Inside function - x: {x}")  # Prints 20


example_shadowing()
print(f"Outside function - x: {x}")  # Prints 10 (global not changed)


# =============================================
# 5. USING GLOBAL KEYWORD TO MODIFY GLOBAL
# =============================================

counter = 0  # GLOBAL variable


def increment_counter():
    """Without 'global', we can't modify global variable"""
    global counter  # Tell Python to use global variable
    counter += 1  # Modify the global variable
    print(f"Counter: {counter}")


increment_counter()  # Prints 1
increment_counter()  # Prints 2
increment_counter()  # Prints 3
print(f"Final counter: {counter}")  # Prints 3


# =============================================
# 6. COMMON MISTAKE: MODIFYING GLOBAL WITHOUT 'global'
# =============================================

total = 100  # GLOBAL


def wrong_way():
    """This will cause an error without 'global' keyword"""
    # total += 10  # UnboundLocalError! Python sees assignment, treats total as local
    # print(total)


# To fix it, use the global keyword:
def right_way():
    global total
    total += 10
    print(f"Total: {total}")


right_way()


# =============================================
# 7. FUNCTION PARAMETERS (also LOCAL)
# =============================================

def add(a, b):
    """Parameters are local variables"""
    result = a + b  # result is local
    return result


sum_result = add(5, 3)
print(f"Sum: {sum_result}")
# print(a)  # ERROR - parameter 'a' is local


# =============================================
# 8. NESTED FUNCTIONS (ENCLOSURE)
# =============================================

def outer_function():
    outer_var = "Outer"  # Outer scope variable
    
    def inner_function():
        inner_var = "Inner"  # Local to inner function
        print(f"Inner var: {inner_var}")
        print(f"Outer var (from inner): {outer_var}")  # Can access outer scope
    
    inner_function()
    # print(inner_var)  # ERROR - not accessible from outer function


outer_function()


# =============================================
# 9. NONLOCAL KEYWORD (for nested functions)
# =============================================

def outer():
    count = 0
    
    def inner():
        nonlocal count  # Refers to count in outer function
        count += 1
        print(f"Count: {count}")
    
    inner()
    inner()
    inner()


outer()


# =============================================
# 10. PRACTICAL EXAMPLE: BANK ACCOUNT
# =============================================

balance = 1000  # GLOBAL balance


def deposit(amount):
    """Add money to account"""
    global balance
    balance += amount
    print(f"Deposited: ${amount}. New balance: ${balance}")


def withdraw(amount):
    """Remove money from account"""
    global balance
    if balance >= amount:
        balance -= amount
        print(f"Withdrew: ${amount}. New balance: ${balance}")
    else:
        print("Insufficient funds!")


deposit(500)  # Balance: 1500
withdraw(200)  # Balance: 1300
withdraw(2000)  # Insufficient funds!
print(f"Final balance: ${balance}")


# =============================================
# 11. VARIABLE SCOPE CHEAT SHEET
# =============================================

"""
SCOPE HIERARCHY (from closest to farthest):
1. LOCAL - Inside a function
2. ENCLOSING - In outer function (nested functions)
3. GLOBAL - Outside all functions
4. BUILT-IN - Python's built-in functions (print, len, etc.)

Use LEGB rule to remember!
"""


# =============================================
# 12. CHECKING VARIABLE SCOPE WITH dir()
# =============================================

def check_scope():
    local_var = 50
    print("Local variables:", dir())  # Shows variables in this scope


check_scope()


# =============================================
# 13. EXAMPLE: COUNTER WITH CLOSURE
# =============================================

def make_counter():
    """Returns a function that counts"""
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter


my_counter = make_counter()
print(f"Call 1: {my_counter()}")
print(f"Call 2: {my_counter()}")
print(f"Call 3: {my_counter()}")

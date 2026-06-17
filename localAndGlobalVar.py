# =============================================================================
# LOCAL AND GLOBAL VARIABLES IN PYTHON
# =============================================================================
# Global variables: Accessible from anywhere (outside any function)
# Local variables: Accessible only within the function where they're defined

print("=" * 60)
print("LOCAL AND GLOBAL VARIABLES")
print("=" * 60)

# ===== 1. GLOBAL VARIABLES =====
print("\n1. GLOBAL VARIABLES\n")

# Variables defined outside functions are GLOBAL
# They can be accessed from anywhere in the program
name = "Alice"  # GLOBAL variable
age = 25  # GLOBAL variable

print(f"Global variables: name={name}, age={age}")

def display_global():
    """Function that accesses global variables"""
    print(f"  Inside function - Global name: {name}")
    print(f"  Inside function - Global age: {age}")

print("Calling display_global():")
display_global()


# ===== 2. LOCAL VARIABLES =====
print("\n" + "=" * 60)
print("2. LOCAL VARIABLES")
print("=" * 60 + "\n")

# Variables defined inside functions are LOCAL
# They only exist inside that function
def local_example():
    """Function with local variables"""
    local_name = "Bob"  # LOCAL variable
    local_age = 30  # LOCAL variable
    
    print(f"  Inside function - Local name: {local_name}")
    print(f"  Inside function - Local age: {local_age}")

print("Calling local_example():")
local_example()

# Try to access local variable outside function (will error)
try:
    print(f"Outside function - local_name: {local_name}")
except NameError:
    print("ERROR: local_name is not accessible outside the function")


# ===== 3. GLOBAL vs LOCAL SCOPE =====
print("\n" + "=" * 60)
print("3. GLOBAL vs LOCAL SCOPE")
print("=" * 60 + "\n")

city = "New York"  # GLOBAL

def city_function():
    """Demonstrates scope"""
    city = "London"  # LOCAL - shadows global variable
    print(f"  Inside function: city = {city}")

print(f"Before function call: city = {city}")
city_function()
print(f"After function call: city = {city}")


# ===== 4. MODIFYING GLOBAL VARIABLES =====
print("\n" + "=" * 60)
print("4. MODIFYING GLOBAL VARIABLES USING 'global' KEYWORD")
print("=" * 60 + "\n")

counter = 0  # GLOBAL variable

def increment_counter():
    """Modify global variable using global keyword"""
    global counter  # Tell Python to use the global counter
    counter += 1
    print(f"  Inside function: counter = {counter}")

print(f"Initial counter: {counter}")
print("Calling increment_counter():")
increment_counter()
print(f"After function call: counter = {counter}")
increment_counter()
print(f"After second call: counter = {counter}")


# ===== 5. NONLOCAL VARIABLES (NESTED FUNCTIONS) =====
print("\n" + "=" * 60)
print("5. NONLOCAL VARIABLES (NESTED FUNCTIONS)")
print("=" * 60 + "\n")

def outer_function():
    """Outer function"""
    x = 10  # Variable in outer function scope
    
    def inner_function():
        """Inner function that modifies outer function's variable"""
        nonlocal x  # Access variable from enclosing function
        x += 5
        print(f"  Inside inner function: x = {x}")
    
    print(f"Before inner function: x = {x}")
    inner_function()
    print(f"After inner function: x = {x}")

print("Calling outer_function():")
outer_function()


# ===== 6. SCOPE HIERARCHY =====
print("\n" + "=" * 60)
print("6. PYTHON SCOPE HIERARCHY (LEGB RULE)")
print("=" * 60 + "\n")

print("""
LEGB Rule for variable lookup:
1. L (Local) - Inside the current function
2. E (Enclosing) - In outer function (for nested functions)
3. G (Global) - At the top level of the script
4. B (Built-in) - Python's built-in scope (e.g., len, print, etc.)

When Python looks for a variable, it follows this order:
Local -> Enclosing -> Global -> Built-in

Example:
    x = "global"  # Global scope
    
    def outer():
        x = "enclosing"  # Enclosing scope
        
        def inner():
            x = "local"  # Local scope
            print(x)  # Will print "local"
        
        inner()
    
    outer()
""")

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

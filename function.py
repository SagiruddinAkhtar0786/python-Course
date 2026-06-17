# =============================================================================
# PYTHON FUNCTIONS - COMPREHENSIVE GUIDE
# =============================================================================
# Functions are reusable blocks of code that perform specific tasks
# They help in code organization and reduce repetition

print("=" * 60)
print("PYTHON FUNCTIONS")
print("=" * 60)

# ===== 1. SIMPLE FUNCTIONS =====
print("\n1. BASIC FUNCTIONS\n")

# Function to calculate circle area
def calculate_area(radius):
    """Calculate area of a circle given radius"""
    pi = 3.14159
    area = pi * (radius ** 2)
    return area

# Function to calculate circle perimeter
def calculate_perimeter(radius):
    """Calculate perimeter of a circle given radius"""
    pi = 3.14159
    perimeter = 2 * pi * radius
    return perimeter

# Using the functions
r = int(input("Enter the radius of the circle: "))
area = calculate_area(r)
perimeter = calculate_perimeter(r)

print(f"Area of circle with radius {r}: {area:.2f}")
print(f"Perimeter of circle with radius {r}: {perimeter:.2f}")


# ===== 2. CONDITIONAL FUNCTION =====
print("\n" + "=" * 60)
print("2. FUNCTION WITH CONDITIONAL LOGIC")
print("=" * 60 + "\n")

def check_greater(a, b):
    """Return the greater of two numbers"""
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Both numbers are equal"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = check_greater(num1, num2)
print(f"The greater number is: {result}")


# ===== 3. FUNCTION WITH VARIABLE ARGUMENTS (*args) =====
print("\n" + "=" * 60)
print("3. FUNCTION WITH VARIABLE ARGUMENTS (*args)")
print("=" * 60 + "\n")

# *args allows function to accept any number of positional arguments
def average(*numbers):
    """Calculate average of any number of arguments"""
    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return avg

print(f"Average of (1, 2, 3, 4, 5): {average(1, 2, 3, 4, 5)}")
print(f"Average of (10, 20, 30): {average(10, 20, 30)}")
print(f"Average of (100, 200): {average(100, 200)}")


# ===== 4. FUNCTION WITH KEYWORD ARGUMENTS (**kwargs) =====
print("\n" + "=" * 60)
print("4. FUNCTION WITH KEYWORD ARGUMENTS (**kwargs)")
print("=" * 60 + "\n")

def print_details(**info):
    """Print key-value pairs passed as keyword arguments"""
    for key, value in info.items():
        print(f"  {key}: {value}")

print("Printing details:")
print_details(name="Ali", age=25, city="New York", job="Engineer")


# ===== 5. FUNCTION WITH DICTIONARY =====
print("\n" + "=" * 60)
print("5. FUNCTION WITH DICTIONARY")
print("=" * 60 + "\n")

student_grades = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

def get_grade(name):
    """Get grade for a student, return 'Not found' if student doesn't exist"""
    return student_grades.get(name, "Student not found")

print(f"Alice's grade: {get_grade('Alice')}")
print(f"Bob's grade: {get_grade('Bob')}")
print(f"David's grade: {get_grade('David')}")  # Not in dictionary


# ===== 6. FUNCTION WITH DEFAULT PARAMETERS =====
print("\n" + "=" * 60)
print("6. FUNCTION WITH DEFAULT PARAMETERS")
print("=" * 60 + "\n")

def greet(name, greeting="Hello"):
    """Greet someone with optional greeting message"""
    return f"{greeting}, {name}!"

print(greet("Ali"))  # Uses default greeting
print(greet("Bob", "Hi"))  # Custom greeting
print(greet("Charlie", "Good morning"))  # Custom greeting


# ===== 7. RETURNING MULTIPLE VALUES =====
print("\n" + "=" * 60)
print("7. RETURNING MULTIPLE VALUES FROM FUNCTION")
print("=" * 60 + "\n")

def get_info(num):
    """Return square, cube, and square root of a number"""
    return num**2, num**3, num**0.5

square, cube, sqrt = get_info(4)
print(f"For number 4:")
print(f"  Square: {square}")
print(f"  Cube: {cube}")
print(f"  Square Root: {sqrt}")


# ===== 8. RECURSIVE FUNCTION =====
print("\n" + "=" * 60)
print("8. RECURSIVE FUNCTION")
print("=" * 60 + "\n")

def factorial(n):
    """Calculate factorial of n recursively"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 0: {factorial(0)}")
print(f"Factorial of 10: {factorial(10)}") 
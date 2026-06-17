# =============================================================================
# PYTHON DEMO - COMPREHENSIVE OVERVIEW OF PYTHON FEATURES
# =============================================================================
# This file demonstrates key Python concepts and features

print("=" * 60)
print("PYTHON COMPREHENSIVE DEMO")
print("=" * 60)

# ===== 1. BASIC DATA TYPES =====
print("\n1. BASIC DATA TYPES\n")

integer = 42
floating = 3.14
string = "Python is awesome!"
boolean = True

print(f"Integer: {integer} (type: {type(integer).__name__})")
print(f"Float: {floating} (type: {type(floating).__name__})")
print(f"String: {string} (type: {type(string).__name__})")
print(f"Boolean: {boolean} (type: {type(boolean).__name__})")


# ===== 2. COLLECTIONS =====
print("\n" + "=" * 60)
print("2. COLLECTIONS: LIST, TUPLE, SET, DICT")
print("=" * 60 + "\n")

# List (mutable)
my_list = [1, 2, 3, 4, 5]
print(f"List: {my_list}")
my_list.append(6)
print(f"After append(6): {my_list}")

# Tuple (immutable)
my_tuple = (10, 20, 30)
print(f"\nTuple: {my_tuple}")
print(f"Tuple is immutable - cannot modify")

# Set (unique values)
my_set = {1, 2, 2, 3, 3, 4}
print(f"\nSet: {my_set} (duplicates removed)")

# Dictionary (key-value pairs)
my_dict = {"name": "Alice", "age": 25, "city": "Boston"}
print(f"\nDictionary: {my_dict}")
print(f"Accessing: my_dict['name'] = {my_dict['name']}")


# ===== 3. CONTROL FLOW =====
print("\n" + "=" * 60)
print("3. CONTROL FLOW: if/elif/else")
print("=" * 60 + "\n")

age = 20

if age < 13:
    category = "Child"
elif age < 18:
    category = "Teenager"
elif age < 65:
    category = "Adult"
else:
    category = "Senior"

print(f"Age {age} = {category}")


# ===== 4. LOOPS =====
print("\n" + "=" * 60)
print("4. LOOPS: for and while")
print("=" * 60 + "\n")

print("For loop - print 0 to 4:")
for i in range(5):
    print(f"  {i}", end=" ")
print()

print("\nFor loop with enumerate:")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

print("\nWhile loop - count to 3:")
count = 0
while count < 3:
    print(f"  count = {count}")
    count += 1


# ===== 5. FUNCTIONS =====
print("\n" + "=" * 60)
print("5. FUNCTIONS")
print("=" * 60 + "\n")

def greet(name, greeting="Hello"):
    """Function with default parameter"""
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))


def calculate_sum(*numbers):
    """Function with variable arguments"""
    total = sum(numbers)
    return total

result = calculate_sum(1, 2, 3, 4, 5)
print(f"\nSum of 1,2,3,4,5 = {result}")


# ===== 6. LIST COMPREHENSION =====
print("\n" + "=" * 60)
print("6. LIST COMPREHENSION")
print("=" * 60 + "\n")

# Create list of squares
squares = [x**2 for x in range(1, 6)]
print(f"Squares 1-5: {squares}")

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")


# ===== 7. LAMBDA FUNCTIONS =====
print("\n" + "=" * 60)
print("7. LAMBDA FUNCTIONS (Anonymous Functions)")
print("=" * 60 + "\n")

# Lambda function - simple function in one line
square = lambda x: x ** 2
print(f"Lambda: square(5) = {square(5)}")

# Lambda with map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Map lambda to list: {squared}")

# Lambda with filter
filtered = list(filter(lambda x: x > 3, numbers))
print(f"Filter lambda (>3): {filtered}")


# ===== 8. STRING MANIPULATION =====
print("\n" + "=" * 60)
print("8. STRING MANIPULATION")
print("=" * 60 + "\n")

text = "Python Programming"
print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Replace: {text.replace('Python', 'Java')}")
print(f"Split: {text.split()}")

# F-string
name = "Python"
version = 3.14
print(f"\nF-string: {name} version {version}")


# ===== 9. EXCEPTION HANDLING =====
print("\n" + "=" * 60)
print("9. EXCEPTION HANDLING")
print("=" * 60 + "\n")

try:
    result = 10 / 2
    print(f"10 / 2 = {result}")
    
    result = 10 / 0  # This will raise an error
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
finally:
    print("Exception handling demo completed")


# ===== 10. IMPORTING MODULES =====
print("\n" + "=" * 60)
print("10. IMPORTING MODULES")
print("=" * 60 + "\n")

import math
import random

print(f"Math functions:")
print(f"  math.sqrt(16) = {math.sqrt(16)}")
print(f"  math.pi = {math.pi}")

print(f"\nRandom functions:")
print(f"  random.randint(1,100) = {random.randint(1, 100)}")
print(f"  random.choice([1,2,3,4,5]) = {random.choice([1, 2, 3, 4, 5])}")


print("\n" + "=" * 60)
print("✓ PYTHON DEMO COMPLETED!")
print("=" * 60)
# =============================================================================
# BASIC CALCULATOR - ARITHMETIC OPERATIONS & STRING MANIPULATION
# =============================================================================
# This file demonstrates:
# 1. Basic arithmetic operations (addition, subtraction, multiplication, division)
# 2. String manipulation and character iteration
# 3. Type conversion and comparison operations

print("=" * 60)
print("BASIC CALCULATOR - ARITHMETIC OPERATIONS")
print("=" * 60)

# ===== 1. BASIC ARITHMETIC OPERATIONS =====
print("\n1. BASIC ARITHMETIC OPERATIONS\n")

a = 5
b = 10

# Addition
print(f"Addition: {a} + {b} = {a + b}")

# Subtraction
print(f"Subtraction: {a} - {b} = {a - b}")

# Multiplication
print(f"Multiplication: {a} * {b} = {a * b}")

# Division (returns float)
print(f"Division: {a} / {b} = {a / b}")

# Floor Division (removes decimal)
print(f"Floor Division: {a} // {b} = {a // b}")

# Modulus (remainder)
print(f"Modulus: {a} % {b} = {a % b}")

# Exponentiation (power)
print(f"Exponentiation: {a} ** {b} = {a ** b}")


# ===== 2. STRING MANIPULATION =====
print("\n" + "=" * 60)
print("2. STRING MANIPULATION AND CHARACTER ITERATION")
print("=" * 60 + "\n")

name = "sagiruddin"

print(f"String: '{name}'")
print(f"Length: {len(name)}")

# Iterate through each character
print("\nIterating through string without index:")
for char in name:
    print(f"  {char}")

# Iterate with index using range
print("\nIterating with index using range():")
for i in range(0, len(name)):
    print(f"  Index {i}: {name[i]}")


# ===== 3. USER INPUT & TYPE CONVERSION =====
print("\n" + "=" * 60)
print("3. USER INPUT & TYPE CONVERSION")
print("=" * 60 + "\n")

try:
    a = input("Enter a number: ")
    print(f"Type of '{a}': {type(a)}")  # Will be string
    
    b = input("Enter another number: ")
    print(f"Type of '{b}': {type(b)}")  # Will be string
    
    # Convert to integer for arithmetic
    sum_ab = int(a) + int(b)
    print(f"Sum of {a} + {b} = {sum_ab}")
    
except ValueError:
    print("ERROR: Please enter valid numbers!")


# ===== 4. COMPARISON OPERATIONS =====
print("\n" + "=" * 60)
print("4. COMPARISON OPERATIONS")
print("=" * 60 + "\n")

try:
    num_a = int(input("\nEnter first number: "))
    num_b = int(input("Enter second number: "))
    
    print(f"\nComparison Results:")
    print(f"  {num_a} > {num_b}: {num_a > num_b}")
    print(f"  {num_a} < {num_b}: {num_a < num_b}")
    print(f"  {num_a} == {num_b}: {num_a == num_b}")
    
    # If-else condition
    if num_a > num_b:
        print(f"\n{num_a} is greater than {num_b}")
    else:
        print(f"\n{num_b} is greater than or equal to {num_a}")
        
except ValueError:
    print("ERROR: Please enter valid integers!")
# =============================================================================
# EXCEPTION HANDLING IN PYTHON
# =============================================================================
# Exceptions are errors that occur during program execution
# try-except blocks handle exceptions gracefully without crashing

print("=" * 60)
print("EXCEPTION HANDLING IN PYTHON")
print("=" * 60)

# ===== 1. BASIC try-except =====
print("\n1. BASIC try-except\n")

try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("ERROR: That's not a valid integer!")


# ===== 2. ValueError HANDLING =====
print("\n" + "=" * 60)
print("2. ValueError HANDLING")
print("=" * 60 + "\n")

try:
    num = input("Enter a number: ")
    num = int(num)  # Attempt to convert to integer
    print(f"You entered the number: {num}")
    
    if num < 0:
        raise ValueError("Negative numbers are not allowed!")
        
except ValueError as e:
    print(f"ERROR: Invalid input - {e}")


# ===== 3. ZeroDivisionError HANDLING =====
print("\n" + "=" * 60)
print("3. ZeroDivisionError HANDLING")
print("=" * 60 + "\n")

try:
    divisor = int(input("Enter a divisor (non-zero): "))
    result = 10 / divisor
    print(f"Result of 10 / {divisor} = {result}")
except ZeroDivisionError:
    print("ERROR: Cannot divide by zero!")
except ValueError:
    print("ERROR: Please enter a valid number!")


# ===== 4. IndexError HANDLING =====
print("\n" + "=" * 60)
print("4. IndexError HANDLING")
print("=" * 60 + "\n")

l = [3, 4, 5, 73, 3]
print(f"List: {l}")

try:
    for i, value in enumerate(l):
        print(f"  Index {i}: {value}")
    
    # Try to access index out of bounds
    print(f"Trying to access index {len(l) + 1}...")
    print(l[len(l) + 1])
    
except IndexError as e:
    print(f"ERROR: Index out of range - {e}")


# ===== 5. try-except-finally =====
print("\n" + "=" * 60)
print("5. try-except-finally BLOCK")
print("=" * 60 + "\n")

print("The 'finally' block ALWAYS executes, whether exception occurs or not:\n")

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"Result: {result}")
except ZeroDivisionError:
    print("ERROR: Cannot divide by zero!")
except ValueError:
    print("ERROR: Invalid input!")
finally:
    print("Finally block: Cleanup code always runs!")


# ===== 6. MULTIPLE EXCEPTION HANDLERS =====
print("\n" + "=" * 60)
print("6. MULTIPLE EXCEPTION HANDLERS")
print("=" * 60 + "\n")

try:
    user_input = input("\nEnter a number: ")
    num = int(user_input)
    result = 100 / num
    print(f"Result: {result}")
except ValueError:
    print("ERROR: Please enter a valid integer")
except ZeroDivisionError:
    print("ERROR: Cannot divide by zero")
except Exception as e:
    print(f"ERROR: An unexpected error occurred - {e}")


# ===== 7. RAISING CUSTOM EXCEPTIONS =====
print("\n" + "=" * 60)
print("7. RAISING CUSTOM EXCEPTIONS")
print("=" * 60 + "\n")

try:
    a = int(input("\nEnter a value between 5 and 9: "))
    if a < 5 or a > 9:
        raise ValueError("Value must be between 5 and 9!")
    print(f"Valid input: {a}")
except ValueError as e:
    print(f"ERROR: {e}")


# ===== 8. EXCEPTION TYPES =====
print("\n" + "=" * 60)
print("8. COMMON EXCEPTION TYPES")
print("=" * 60 + "\n")

print("""
COMMON EXCEPTIONS:
1. ValueError - Invalid value passed to function
2. ZeroDivisionError - Division by zero
3. TypeError - Wrong data type
4. IndexError - Index out of range
5. KeyError - Dictionary key not found
6. AttributeError - Attribute doesn't exist
7. FileNotFoundError - File doesn't exist
8. NameError - Variable not defined
9. ImportError - Module not found
10. RuntimeError - General runtime error

EXCEPTION HIERARCHY:
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── StopIteration
    ├── ArithmeticError (ZeroDivisionError)
    ├── LookupError (IndexError, KeyError)
    ├── NameError
    ├── TypeError
    ├── ValueError
    └── ... many more
""")
# =============================================================================
# OUTERIMPORT.PY - CUSTOM MODULE FOR IMPORTING
# =============================================================================
# This file demonstrates creating a custom module that can be imported
# by other Python files in the same directory

print("=" * 60)
print("OuterImport.py - CUSTOM MODULE")
print("=" * 60)


# ===== 1. MODULE VARIABLES =====
print("\n1. MODULE VARIABLES\n")

sagir = "A good boy"
print(f"Variable 'sagir': {sagir}")

# Additional variables
author = "Sagir"
status = "Learning Python"
print(f"Author: {author}")
print(f"Status: {status}")


# ===== 2. MODULE FUNCTIONS =====
print("\n" + "=" * 60)
print("2. MODULE FUNCTIONS")
print("=" * 60 + "\n")


def welcome():
    """Return a simple welcome message."""
    message = "Hey, welcome to the board!"
    print(message)
    return message


def goodbye():
    """Return a goodbye message."""
    message = "Thanks for visiting!"
    print(message)
    return message


def greet(name):
    """Greet a specific person."""
    message = f"Hello, {name}! Welcome!"
    print(message)
    return message


# ===== 3. CALL FUNCTIONS IN THIS MODULE =====
print("\nCalling functions in this module:\n")

welcome()
goodbye()
greet("Sagir")


# ===== 4. HOW THIS MODULE IS USED =====
print("\n" + "=" * 60)
print("4. HOW THIS MODULE IS USED")
print("=" * 60 + "\n")

print("""
This module can be imported in other Python files:

METHOD 1: Import entire module
    import OuterImport
    OuterImport.welcome()
    print(OuterImport.sagir)

METHOD 2: Import with alias
    import OuterImport as OI
    OI.welcome()
    OI.goodbye()

METHOD 3: Import specific items
    from OuterImport import welcome, sagir
    welcome()
    print(sagir)

METHOD 4: Import everything (not recommended)
    from OuterImport import *
    welcome()
    print(sagir)
""")


# ===== 5. MODULE INFO =====
print("\n" + "=" * 60)
print("5. MODULE INFORMATION")
print("=" * 60 + "\n")

print(f"Module name: {__name__}")
print(f"Module file: {__file__}")

# List available items in this module
import sys
current_module = sys.modules[__name__]
items = dir(current_module)
print(f"\nAvailable items in this module:")
for item in items:
    if not item.startswith('_'):
        print(f"  - {item}")
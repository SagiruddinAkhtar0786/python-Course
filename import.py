# =============================================================================
# IMPORTING MODULES IN PYTHON
# =============================================================================
# Modules are files containing Python code
# Packages are directories containing modules

print("=" * 60)
print("IMPORTING MODULES IN PYTHON")
print("=" * 60)

# ===== 1. IMPORT ENTIRE MODULE =====
print("\n1. IMPORT ENTIRE MODULE\n")

# Method 1: Import specific functions
# from math import sqrt, pi
# result = sqrt(9) * pi
# print(f"sqrt(9) * pi = {result}")

# Method 2: Import module with alias
# import math as m
# result = m.sqrt(9) * m.pi
# print(f"sqrt(9) * pi = {result}")


# ===== 2. VIEW MODULE CONTENTS =====
print("\n" + "=" * 60)
print("2. VIEW MODULE CONTENTS USING dir()")
print("=" * 60 + "\n")

import math

print("Functions and constants in math module:")
print(dir(math))

print(f"\nSome useful math functions:")
print(f"  math.sqrt(16) = {math.sqrt(16)}")
print(f"  math.pi = {math.pi}")
print(f"  math.sin(0) = {math.sin(0)}")
print(f"  math.cos(0) = {math.cos(0)}")
print(f"  math.ceil(3.2) = {math.ceil(3.2)}")
print(f"  math.floor(3.8) = {math.floor(3.8)}")


# ===== 3. IMPORT FROM CUSTOM MODULE =====
print("\n" + "=" * 60)
print("3. IMPORT FROM CUSTOM MODULE (OuterImport)")
print("=" * 60 + "\n")

# Method 1: Import specific items
# from OuterImport import welcome, sagir
# welcome()
# print(sagir)

# Method 2: Import module with alias
import OuterImport as OI

print("Calling welcome() from OuterImport:")
OI.welcome()

print(f"\nAccessing variable sagir from OuterImport:")
print(f"  OI.sagir = {OI.sagir}")


# ===== 4. IMPORT METHODS =====
print("\n" + "=" * 60)
print("4. IMPORT METHODS")
print("=" * 60 + "\n")

print("""
METHOD 1: Import entire module
    import math
    result = math.sqrt(9)
    
METHOD 2: Import module with alias
    import math as m
    result = m.sqrt(9)

METHOD 3: Import specific items
    from math import sqrt, pi
    result = sqrt(9) * pi

METHOD 4: Import all items (not recommended)
    from math import *
    result = sqrt(9) * pi

METHOD 5: Import custom module
    import OuterImport
    OuterImport.welcome()

METHOD 6: Import with alias
    import OuterImport as OI
    OI.welcome()

METHOD 7: Import specific items from custom module
    from OuterImport import welcome, sagir
    welcome()
    print(sagir)
""")


# ===== 5. BUILT-IN MODULES =====
print("\n" + "=" * 60)
print("5. COMMONLY USED BUILT-IN MODULES")
print("=" * 60 + "\n")

print("""
Common Python Built-in Modules:

1. math
   - Mathematical functions: sqrt, sin, cos, ceil, floor, etc.
   - Constants: pi, e, inf, nan
   
2. random
   - Generate random numbers: random(), randint(), choice(), shuffle()
   
3. time
   - Time-related functions: time(), sleep(), strftime()
   - Get current time: localtime(), gmtime()
   
4. os
   - Operating system functions: listdir(), getcwd(), path.exists()
   
5. sys
   - System functions: exit(), argv, path
   
6. datetime
   - Date and time objects: datetime(), date(), time()
   
7. json
   - JSON processing: dumps(), loads()
   
8. csv
   - CSV file handling: reader(), writer()
   
9. requests
   - HTTP requests (external library)
   
10. numpy, pandas
    - Data science libraries (external)
""")



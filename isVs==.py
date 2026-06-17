# =====================================================
# == vs is IN PYTHON
# =====================================================

# == checks VALUE equality (does content match?)
# is checks IDENTITY equality (are they the same object?)


# =====================================================
# 1. BASIC DIFFERENCE
# =====================================================

print("1. BASIC DIFFERENCE")
print("-" * 50)

# Example 1: Numbers
a = 10
b = 10

print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")  # True - values are the same
print(f"a is b: {a is b}")   # True - small integers cached by Python


# Example 2: Lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(f"\nlist1 = {list1}")
print(f"list2 = {list2}")
print(f"list1 == list2: {list1 == list2}")  # True - same content
print(f"list1 is list2: {list1 is list2}")   # False - different objects


# =====================================================
# 2. UNDERSTANDING OBJECT IDENTITY
# =====================================================

print("\n2. UNDERSTANDING OBJECT IDENTITY")
print("-" * 50)

# Get memory address using id()
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(f"id(x) = {id(x)}")
print(f"id(y) = {id(y)}")
print(f"id(z) = {id(z)}")

print(f"\nx == y: {x == y}")  # True - same content
print(f"x is y: {x is y}")   # False - different objects in memory

print(f"\nx == z: {x == z}")  # True - same content
print(f"x is z: {x is z}")   # True - z points to same object as x


# =====================================================
# 3. == vs is WITH DIFFERENT DATA TYPES
# =====================================================

print("\n3. == vs is WITH DIFFERENT DATA TYPES")
print("-" * 50)

# STRINGS
str1 = "Hello"
str2 = "Hello"
str3 = str1

print("STRINGS:")
print(f"str1 = '{str1}', str2 = '{str2}'")
print(f"str1 == str2: {str1 == str2}")  # True
print(f"str1 is str2: {str1 is str2}")   # True (string interning)

print(f"\nstr1 = '{str1}', str3 = '{str3}'")
print(f"str1 == str3: {str1 == str3}")  # True
print(f"str1 is str3: {str1 is str3}")   # True (same reference)


# TUPLES
t1 = (1, 2, 3)
t2 = (1, 2, 3)
t3 = t1

print("\nTUPLES:")
print(f"t1 == t2: {t1 == t2}")  # True - same content
print(f"t1 is t2: {t1 is t2}")   # Might be True or False (tuples can be cached)

print(f"t1 == t3: {t1 == t3}")  # True
print(f"t1 is t3: {t1 is t3}")   # True (same object)


# DICTIONARIES
d1 = {"name": "Ali"}
d2 = {"name": "Ali"}
d3 = d1

print("\nDICTIONARIES:")
print(f"d1 == d2: {d1 == d2}")  # True - same content
print(f"d1 is d2: {d1 is d2}")   # False - different objects

print(f"d1 == d3: {d1 == d3}")  # True
print(f"d1 is d3: {d1 is d3}")   # True (same object)


# =====================================================
# 4. NUMBERS AND IDENTITY
# =====================================================

print("\n4. NUMBERS AND IDENTITY")
print("-" * 50)

# Small integers (-5 to 256) are cached by Python
a = 5
b = 5
print(f"a = 5, b = 5")
print(f"a == b: {a == b}")  # True
print(f"a is b: {a is b}")   # True (cached)

# Large integers are NOT cached
x = 257
y = 257
print(f"\nx = 257, y = 257")
print(f"x == y: {x == y}")  # True
print(f"x is y: {x is y}")   # False (not cached)

# But if you assign directly
z = x
print(f"\nz = x")
print(f"x == z: {x == z}")  # True
print(f"x is z: {x is z}")   # True (same reference)


# =====================================================
# 5. NONE COMPARISON
# =====================================================

print("\n5. NONE COMPARISON")
print("-" * 50)

# Always use 'is' for None
a = None
b = None

print(f"a = None, b = None")
print(f"a == b: {a == b}")  # True
print(f"a is b: {a is b}")   # True

# Check if variable is None
x = None
if x is None:  # Correct way
    print("x is None")

if x == None:  # Works but not recommended
    print("x == None")


# =====================================================
# 6. MUTABLE vs IMMUTABLE OBJECTS
# =====================================================

print("\n6. MUTABLE vs IMMUTABLE OBJECTS")
print("-" * 50)

# IMMUTABLE: strings, numbers, tuples
# (Small ones might be cached)
s1 = "test"
s2 = "test"
print(f"Immutable (string): 'test' is 'test' = {s1 is s2}")

# MUTABLE: lists, dicts, sets
# (Always creates new objects)
l1 = [1, 2]
l2 = [1, 2]
print(f"Mutable (list): [1,2] is [1,2] = {l1 is l2}")


# =====================================================
# 7. PRACTICAL EXAMPLES
# =====================================================

print("\n7. PRACTICAL EXAMPLES")
print("-" * 50)

# Example 1: Checking if variable is None
def process_data(data):
    if data is None:  # Correct
        print("No data provided")
    else:
        print(f"Processing: {data}")

process_data(None)
process_data([1, 2, 3])


# Example 2: Comparing values (use ==)
user_input = "10"
if user_input == "10":  # Use == for value comparison
    print("User entered 10")


# Example 3: Checking object type
def check_type(obj):
    if type(obj) is list:  # Can use is for type checking
        print("It's a list")
    elif type(obj) is dict:
        print("It's a dict")


check_type([1, 2])
check_type({"a": 1})


# =====================================================
# 8. WHEN TO USE WHAT
# =====================================================

print("\n8. WHEN TO USE WHAT")
print("-" * 50)
print("""
USE == WHEN:
  - Comparing VALUES (content matters)
  - Comparing numbers: if x == 5
  - Comparing strings: if name == "Ali"
  - Comparing lists: if list1 == list2
  - Comparing objects' content

USE 'is' WHEN:
  - Comparing with None: if x is None
  - Checking if it's the SAME object
  - Checking object identity
  - Comparing with True/False (careful!)
  
EXAMPLE:
  num = 10
  if num == 10:        # Is the value 10? (YES)
  if num is 10:        # Is it the exact same object? (Maybe)
  
  list1 = [1, 2]
  list2 = [1, 2]
  if list1 == list2:   # Same content? (YES)
  if list1 is list2:   # Same object? (NO)
""")


# =====================================================
# 9. COMMON MISTAKES
# =====================================================

print("\n9. COMMON MISTAKES")
print("-" * 50)

# WRONG: Comparing lists with 'is'
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(f"WRONG: l1 is l2 = {l1 is l2}")  # False (bad for content check)
print(f"RIGHT: l1 == l2 = {l1 == l2}")  # True (correct)

# WRONG: Not using 'is' for None
value = None
print(f"\nWRONG: value == None = {value == None}")  # Works but not preferred
print(f"RIGHT: value is None = {value is None}")   # Correct


# =====================================================
# 10. QUICK SUMMARY TABLE
# =====================================================

print("\n10. QUICK SUMMARY")
print("-" * 50)
print("""
┌─────────────────┬──────────────────┬────────────────────┐
│   Operator      │     Checks       │     Example        │
├─────────────────┼──────────────────┼────────────────────┤
│       ==        │  VALUE equality  │ [1,2] == [1,2]→T   │
│       !=        │  VALUE inequality│ 5 != 3 → True      │
│       is        │  IDENTITY (same) │ x is y → ?         │
│      is not     │  IDENTITY (diff) │ x is not y → ?     │
└─────────────────┴──────────────────┴────────────────────┘
""")

print("✓ All examples completed!")

# =============================================================================
# F-STRINGS (FORMATTED STRING LITERALS) - PYTHON 3.6+
# =============================================================================
# F-strings provide a concise and readable way to embed expressions in strings
# Syntax: f"text {expression} more text"

print("=" * 60)
print("F-STRINGS (FORMATTED STRING LITERALS)")
print("=" * 60)

# ===== 1. BASIC F-STRING USAGE =====
print("\n1. BASIC F-STRING USAGE\n")

# Variables
name = "Sagiruddin Akhtar"
country = "India"
age = 25

# Traditional .format() method
letter = "Hey my name is {} and I am from {}"
print("Using .format():")
print(f"  {letter.format(name, country)}")

# F-string (modern approach)
fString = f"Hey my name is {name} and I am from {country}"
print("\nUsing f-string:")
print(f"  {fString}")


# ===== 2. F-STRING METHODS =====
print("\n" + "=" * 60)
print("2. STRING METHODS WITH F-STRINGS")
print("=" * 60 + "\n")

# Upper case
print(f"UPPER: {fString.upper()}")

# Lower case
print(f"LOWER: {fString.lower()}")

# Title case
print(f"TITLE: {fString.title()}")

# Replace text
print(f"REPLACE: {fString.replace('Hey', 'Hello')}")


# ===== 3. EXPRESSIONS IN F-STRINGS =====
print("\n" + "=" * 60)
print("3. EXPRESSIONS IN F-STRINGS")
print("=" * 60 + "\n")

# Mathematical operations
print(f"2 * 6 = {2 * 6}")
print(f"10 / 3 = {10 / 3}")
print(f"5 ** 2 = {5 ** 2}")

# String concatenation
print(f"Full info: {name} is {age} years old and from {country}")


# ===== 4. FORMATTING OPTIONS =====
print("\n" + "=" * 60)
print("4. FORMATTING OPTIONS")
print("=" * 60 + "\n")

# Decimal places
pi = 3.14159265
print(f"Pi with 2 decimals: {pi:.2f}")
print(f"Pi with 4 decimals: {pi:.4f}")

# Width and alignment
num = 42
print(f"Right aligned (width 10): {num:>10}")
print(f"Left aligned (width 10): {num:<10}")
print(f"Center aligned (width 10): {num:^10}")

# Padding with zeros
print(f"Zero padded: {num:05d}")

# Percentage
percentage = 0.85
print(f"As percentage: {percentage:.1%}")


# ===== 5. COMPLEX EXPRESSIONS =====
print("\n" + "=" * 60)
print("5. COMPLEX EXPRESSIONS IN F-STRINGS")
print("=" * 60 + "\n")

# List slicing
colors = "Red, Green, Blue, Yellow"
print(f"First 10 chars: {colors[:10]}")
print(f"Every 2nd char: {colors[::2]}")

# Conditional expression
age = 25
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# Dictionary access
person = {"name": "Ali", "age": 30}
print(f"Person: {person['name']} is {person['age']} years old")

# Function call
def get_greeting(n):
    return f"Hello, {n}!"

print(f"Function result: {get_greeting(name)}")


# ===== 6. DEBUGGING WITH F-STRINGS =====
print("\n" + "=" * 60)
print("6. DEBUGGING WITH F-STRINGS (Python 3.8+)")
print("=" * 60 + "\n")

x = 10
y = 20

# Print variable with its name and value
print(f"x = {x}")
print(f"y = {y}")
print(f"x + y = {x + y}")

# Using = for debugging (shows expression and value)
# Note: Requires Python 3.8+
try:
    print(f"{x=}, {y=}")
except:
    print("Debugging feature requires Python 3.8+")
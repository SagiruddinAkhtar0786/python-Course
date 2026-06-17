# =============================================================================
# IF-ELSE SHORTHAND (TERNARY OPERATOR)
# =============================================================================
# Ternary operator is a concise way to write if-else on a single line
# Syntax: value_if_true if condition else value_if_false

print("=" * 60)
print("IF-ELSE SHORTHAND (TERNARY OPERATOR)")
print("=" * 60)

# ===== 1. BASIC TERNARY OPERATOR =====
print("\n1. BASIC TERNARY OPERATOR\n")

a = 3434
b = 33

# Traditional if-else
if a > b:
    result = f"{a} is greater than {b}"
elif a == b:
    result = "Both are equal"
else:
    result = f"{b} is greater than {a}"

print("Traditional if-else:")
print(f"  Result: {result}")


# ===== 2. SHORTHAND TERNARY =====
print("\n" + "=" * 60)
print("2. SHORTHAND TERNARY (Single line)")
print("=" * 60 + "\n")

# One-liner using ternary operator
result_short = f"{a} is greater" if a > b else f"{b} is greater"
print(f"Ternary operator result: {result_short}")

# Using print directly with ternary
print("Using ternary in print:")
print(f"Result: {a if a > b else b}")


# ===== 3. NESTED TERNARY OPERATORS =====
print("\n" + "=" * 60)
print("3. NESTED TERNARY OPERATORS")
print("=" * 60 + "\n")

# Original nested if-else (from your code)
print("a = ", a, "b = ", b)
print("a : ", a) if a > b else print("=") if a == b else print("b")

# Same as above, more readable
print("\nMore readable version:")
if a > b:
    print(f"a ({a}) is greater than b ({b})")
elif a == b:
    print("a and b are equal")
else:
    print(f"b ({b}) is greater than a ({a})")


# ===== 4. TERNARY IN DIFFERENT CONTEXTS =====
print("\n" + "=" * 60)
print("4. TERNARY IN DIFFERENT CONTEXTS")
print("=" * 60 + "\n")

# In variable assignment
age = 25
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age}, Status: {status}")

# In function arguments
num = 10
print(f"{num} is " + ("even" if num % 2 == 0 else "odd"))

# In list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parity = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(f"Numbers and their parity: {list(zip(numbers, parity))}")


# ===== 5. MULTIPLE CONDITIONS =====
print("\n" + "=" * 60)
print("5. MULTIPLE CONDITIONS WITH TERNARY")
print("=" * 60 + "\n")

x = 15

# Check if positive, negative, or zero
sign = "positive" if x > 0 else ("negative" if x < 0 else "zero")
print(f"{x} is {sign}")

# Grade assignment
score = 85
grade = "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else "F"))
print(f"Score: {score}, Grade: {grade}")


# ===== 6. COMPARISON TABLE =====
print("\n" + "=" * 60)
print("6. COMPARISON: if-else vs ternary")
print("=" * 60 + "\n")

print("""
TRADITIONAL IF-ELSE:
    if condition:
        result = value_if_true
    else:
        result = value_if_false

TERNARY OPERATOR:
    result = value_if_true if condition else value_if_false

NESTED IF-ELSE:
    if condition1:
        result = value1
    elif condition2:
        result = value2
    else:
        result = value3

NESTED TERNARY:
    result = value1 if condition1 else (value2 if condition2 else value3)

ADVANTAGES OF TERNARY:
✓ More concise, one-liner
✓ Better for simple conditions
✓ Can be used in expressions
✗ Less readable for complex conditions
✗ Nested ternary can be confusing

BEST PRACTICE:
- Use ternary for simple, straightforward conditions
- Use if-elif-else for complex logic
- Avoid deeply nested ternary operators
""")
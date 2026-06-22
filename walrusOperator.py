# =============================================================================
# WALRUS OPERATOR (:=) IN PYTHON
# =============================================================================
# The walrus operator allows assignment within expressions (Python 3.8+)
# It assigns a value and returns that value in a single operation

print("=" * 60)
print("WALRUS OPERATOR (:=) - ASSIGNMENT EXPRESSION")
print("=" * 60)

# ===== 1. WALRUS OPERATOR BASICS =====
print("\n1. BASIC WALRUS OPERATOR")
print("=" * 60 + "\n")

# WITHOUT walrus operator (traditional way)
print("WITHOUT Walrus Operator:")
x = 10
if x > 5:
    print(f"x = {x}")

# WITH walrus operator (new way)
print("\nWITH Walrus Operator:")
if (x := 10) > 5:
    print(f"x = {x}")


# ===== 2. WHILE LOOP EXAMPLE =====
print("\n2. WHILE LOOP WITH WALRUS OPERATOR")
print("=" * 60 + "\n")

# Traditional way
print("Traditional way:")
data = [1, 2, 3, 4, 5]
index = 0
while index < len(data):
    print(f"  {data[index]}", end=" ")
    index += 1
print()

# Using walrus operator
print("\nUsing walrus operator:")
data = [1, 2, 3, 4, 5]
index = 0
while (value := data[index]) if index < len(data) else False:
    print(f"  {value}", end=" ")
    index += 1
print()


# ===== 3. FILE READING EXAMPLE =====
print("\n3. FILE READING WITH WALRUS OPERATOR")
print("=" * 60 + "\n")

# Create a test file
with open("sample.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5\n")

# Traditional way
print("Traditional way:")
with open("sample.txt") as f:
    line = f.readline()
    while line:
        print(f"  {line.strip()}")
        line = f.readline()

# Using walrus operator
print("\nUsing walrus operator:")
with open("sample.txt") as f:
    while (line := f.readline()):
        print(f"  {line.strip()}")


# ===== 4. IF-ELIF CHAIN =====
print("\n4. IF-ELIF WITH WALRUS OPERATOR")
print("=" * 60 + "\n")

# Without walrus
print("Without walrus:")
result = 15
if result > 20:
    print("Greater than 20")
elif result > 10:
    print("Greater than 10")
else:
    print("10 or less")

# With walrus
print("\nWith walrus:")
if (result := 15) > 20:
    print("Greater than 20")
elif result > 10:
    print("Greater than 10")
else:
    print("10 or less")


# ===== 5. LIST COMPREHENSION =====
print("\n5. LIST COMPREHENSION WITH WALRUS OPERATOR")
print("=" * 60 + "\n")

# Without walrus - calculating twice
print("Without walrus (calculates twice):")
numbers = [1, 2, 3, 4, 5]
# squared = [x*x for x in numbers if x*x > 10]
# print(f"Squared numbers > 10: {squared}")

# With walrus - calculate once
print("With walrus (calculate once):")
numbers = [1, 2, 3, 4, 5]
squared = [y for x in numbers if (y := x*x) > 10]
print(f"Squared numbers > 10: {squared}")


# ===== 6. FUNCTION CALL IN CONDITION =====
print("\n6. FUNCTION CALL IN CONDITION")
print("=" * 60 + "\n")

def validate_email(email):
    return "@" in email and "." in email

# Without walrus
print("Without walrus:")
email = "user@example.com"
is_valid = validate_email(email)
if is_valid:
    print(f"Email {email} is valid")

# With walrus
print("\nWith walrus:")
if validate_email(email := "user@example.com"):
    print(f"Email {email} is valid")


# ===== 7. REAL-WORLD EXAMPLE =====
print("\n7. REAL-WORLD EXAMPLE: PARSING DATA")
print("=" * 60 + "\n")

data = {
    'name': 'Alice',
    'age': 25,
    'score': None
}

# Without walrus - need to get twice
print("Without walrus:")
score = data.get('score')
if score is not None and score > 80:
    print(f"High score: {score}")
else:
    print("No score or score <= 80")

# With walrus - get once
print("\nWith walrus:")
if (score := data.get('score')) is not None and score > 80:
    print(f"High score: {score}")
else:
    print("No score or score <= 80")


# ===== 8. SUMMARY =====
print("\n" + "=" * 60)
print("WALRUS OPERATOR SUMMARY")
print("=" * 60)
print("""
WHAT IS WALRUS OPERATOR?
• Assignment operator: :=
• Introduced in Python 3.8
• Assigns AND returns value in same expression
• Named ":=" because it looks like a walrus's eyes and tusks

SYNTAX:
    if (variable := expression):
        use_variable

BENEFITS:
✓ Reduces code repetition
✓ Makes code more concise
✓ Useful in loops and conditions
✓ Avoids multiple function calls

COMMON USE CASES:
1. While loops with file reading
2. If conditions with assignments
3. List comprehensions
4. Avoiding repeated calculations
5. Reducing variable declarations

WHEN TO USE:
• When you need to assign and test in one line
• When assignment is meaningful to the logic
• To avoid repeated function calls
• In list/dict comprehensions

WHEN NOT TO USE:
• When it makes code less readable
• In simple cases where clarity is more important
• Multiple assignments in one expression
""")

print("\n" + "=" * 60)
print("✓ WALRUS OPERATOR TUTORIAL COMPLETED!")
print("=" * 60)

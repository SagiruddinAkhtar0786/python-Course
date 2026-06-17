# =============================================================================
# MATCH-CASE STATEMENT (PYTHON 3.10+)
# =============================================================================
# Match-case is Python's version of switch-case statement
# More powerful and flexible than if-elif-else
# Supports pattern matching

print("=" * 60)
print("MATCH-CASE STATEMENT (Python 3.10+)")
print("=" * 60)

# ===== 1. BASIC MATCH-CASE =====
print("\n1. BASIC MATCH-CASE\n")

x = int(input("Enter a number: "))

match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case 2:
        print("x is two")
    case _:  # Default case (underscore means any value)
        print(f"x is {x}")


# ===== 2. MATCH-CASE WITH CONDITIONS =====
print("\n" + "=" * 60)
print("2. MATCH-CASE WITH CONDITIONS (if guards)")
print("=" * 60 + "\n")

y = int(input("\nEnter another number: "))

match y:
    case 0:
        print("y is zero")
    case _ if y != 90:
        print(f"{y} is not 90")
    case _ if y != 80:
        print(f"{y} is not 80")
    case _:
        print("y is either 90 or 80")


# ===== 3. MULTIPLE VALUES IN ONE CASE =====
print("\n" + "=" * 60)
print("3. MULTIPLE VALUES IN ONE CASE")
print("=" * 60 + "\n")

day = int(input("\nEnter day number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6 | 7:  # 6 or 7
        print("Weekend")
    case _:
        print("Invalid day")


# ===== 4. MATCH-CASE WITH RANGES =====
print("\n" + "=" * 60)
print("4. MATCH-CASE WITH RANGES")
print("=" * 60 + "\n")

score = int(input("\nEnter your score (0-100): "))

match score:
    case 0 | 1 | 2 | 3 | 4 | 5:
        grade = "F"
    case 6 | 7:
        grade = "D"
    case 8:
        grade = "C"
    case 9:
        grade = "B"
    case 10:
        grade = "A"
    case _:
        if score < 0 or score > 100:
            grade = "Invalid"
        else:
            grade = "Unknown"

print(f"Score: {score}, Grade: {grade}")


# ===== 5. MATCH-CASE WITH LISTS/TUPLES =====
print("\n" + "=" * 60)
print("5. MATCH-CASE WITH LISTS/TUPLES (PATTERN MATCHING)")
print("=" * 60 + "\n")

def describe_point(point):
    """Describe a point using pattern matching"""
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"On Y-axis at {y}"
        case (x, 0):
            return f"On X-axis at {x}"
        case (x, y):
            return f"Point at ({x}, {y})"
        case _:
            return "Invalid point"

print(describe_point((0, 0)))
print(describe_point((0, 5)))
print(describe_point((3, 0)))
print(describe_point((2, 3)))


# ===== 6. COMPARISON: if-elif-else vs match-case =====
print("\n" + "=" * 60)
print("6. COMPARISON: if-elif-else vs match-case")
print("=" * 60 + "\n")

print("""
Using if-elif-else (Traditional):
    if x == 0:
        print("zero")
    elif x == 1:
        print("one")
    else:
        print("other")

Using match-case (Modern Python 3.10+):
    match x:
        case 0:
            print("zero")
        case 1:
            print("one")
        case _:
            print("other")

ADVANTAGES OF MATCH-CASE:
- Cleaner, more readable code
- Pattern matching support
- Better performance for many conditions
- Easier to maintain
- Can destructure complex data structures
""")

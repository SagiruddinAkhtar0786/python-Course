# =============================================================================
# PYTHON LOOPS - FOR LOOPS WITH enumerate()
# =============================================================================
# Loops are used to iterate over sequences (lists, strings, etc.)
# enumerate() provides both index and value during iteration

print("=" * 60)
print("PYTHON LOOPS")
print("=" * 60)

# ===== 1. BASIC FOR LOOP WITH else =====
print("\n1. BASIC FOR LOOP WITH else CLAUSE\n")

# Basic for loop
print("Loop from 0 to 4:")
for i in range(5):
    print(f"  Iteration {i}: Hello, World!")

print("Loop completed!")


# ===== 2. FOR LOOP WITH BREAK =====
print("\n" + "=" * 60)
print("2. FOR LOOP WITH BREAK")
print("=" * 60 + "\n")

print("Loop with break at i=2:")
for i in range(5):
    print(f"  i = {i}")
    if i == 2:
        print("  BREAK: Exiting loop!")
        break

print("Loop broken!")


# ===== 3. enumerate() - GET INDEX AND VALUE =====
print("\n" + "=" * 60)
print("3. enumerate() - GET INDEX AND VALUE")
print("=" * 60 + "\n")

# List of items
fruits = ["sagir", "rahu", "amit", "ravi"]

print("Using enumerate() - default start index (0):")
for index, fruit in enumerate(fruits):
    print(f"  Index: {index}, Value: {fruit}")

print("\nUsing enumerate() - with start=1:")
for index, fruit in enumerate(fruits, start=1):
    print(f"  Index: {index}, Value: {fruit}")


# ===== 4. MORE LOOP EXAMPLES =====
print("\n" + "=" * 60)
print("4. MORE LOOP EXAMPLES")
print("=" * 60 + "\n")

# Loop with range and step
print("Loop with step of 2 (0, 2, 4, 6, 8):")
for i in range(0, 10, 2):
    print(f"  {i}")

# Nested loops
print("\nNested loops (multiplication table for 3):")
for i in range(1, 6):
    print(f"  3 * {i} = {3 * i}")

# Loop over strings
print("\nIterating over string 'PYTHON':")
for char in "PYTHON":
    print(f"  {char}")


# ===== 5. FOR-ELSE CONSTRUCT =====
print("\n" + "=" * 60)
print("5. FOR-ELSE CONSTRUCT")
print("=" * 60 + "\n")

# The else block runs if loop completes without break
print("Loop completes normally (with else):")
for i in range(3):
    print(f"  i = {i}")
else:
    print("  Loop completed successfully!")

print("\nLoop with break (else doesn't run):")
for i in range(5):
    print(f"  i = {i}")
    if i == 2:
        print("  BREAK!")
        break
else:
    print("  This won't print because of break")

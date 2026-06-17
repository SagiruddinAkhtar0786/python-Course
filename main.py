# =============================================================================
# MAIN.PY - BASIC PYTHON PRINTING AND OUTPUT DEMONSTRATION
# =============================================================================
# Demonstrates print() function with various parameters

print("=" * 60)
print("BASIC PRINTING AND OUTPUT")
print("=" * 60)

# ===== 1. SIMPLE PRINTING =====
print("\n1. SIMPLE PRINTING\n")

print("Hello, World!")


# ===== 2. MATHEMATICAL OPERATIONS IN PRINT =====
print("\n" + "=" * 60)
print("2. MATHEMATICAL OPERATIONS IN PRINT()")
print("=" * 60 + "\n")

result = 12 * 13
print(f"12 * 13 = {result}")


# ===== 3. MULTIPLE VALUES WITH sep PARAMETER =====
print("\n" + "=" * 60)
print("3. MULTIPLE VALUES WITH sep PARAMETER")
print("=" * 60 + "\n")

# sep parameter controls the separator between values
print("Using sep='***':")
print("sagir", 3, 4, sep="***")

print("\nUsing sep=' | ':")
print("apple", "banana", "cherry", sep=" | ")

print("\nUsing sep=' -> ':")
print(1, 2, 3, 4, 5, sep=" -> ")


# ===== 4. END PARAMETER =====
print("\n" + "=" * 60)
print("4. END PARAMETER (Changes line ending)")
print("=" * 60 + "\n")

# end parameter controls what appears at the end of print()
print("This is line 1", end="!!!\n")
print("This is line 2", end=" [END]\n")

print("Using default end='\\n':")
print("Line 1")
print("Line 2")

print("\nUsing end=' ' (same line):")
print("Part 1", end=" ")
print("Part 2", end=" ")
print("Part 3")


# ===== 5. COMBINING sep AND end =====
print("\n" + "=" * 60)
print("5. COMBINING sep AND end PARAMETERS")
print("=" * 60 + "\n")

print("The answer to the Ultimate Question of Life")
print("The Universe, and Everything is", 42, sep=" | ", end="!!!\n")

print("\nAnother example:")
print("Python", "is", "awesome", sep="-", end="!\n")


# ===== 6. ESCAPE CHARACTERS =====
print("\n" + "=" * 60)
print("6. ESCAPE CHARACTERS")
print("=" * 60 + "\n")

print("Line with \\n for newline:")
print("First line\nSecond line\nThird line")

print("\nLine with \\t for tab:")
print("Name\tAge\tCity")
print("Alice\t25\tNew York")
print("Bob\t30\tBoston")

print("\nBackslash escape:")
print("Path: C:\\Users\\Documents\\file.txt")


# ===== 7. COMMENT EXAMPLE =====
# This is a single-line comment
print("\n✓ All printing examples completed!")
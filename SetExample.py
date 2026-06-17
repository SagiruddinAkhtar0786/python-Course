# =============================================================================
# PYTHON SETS - COMPREHENSIVE GUIDE
# =============================================================================
# Sets are unordered collections of UNIQUE items
# Sets are mutable but only contain unique values
# Sets use curly braces {} but empty set is set()

print("=" * 60)
print("PYTHON SETS")
print("=" * 60)

# ===== 1. CREATING SETS =====
print("\n1. CREATING SETS\n")

# Create a set (duplicates are automatically removed)
s = {3, 5, 3, 2, 2, 6, "fsagit", "sagir", True, False, 3.14}
print(f"Set with duplicates: {s}")
print(f"Length of set: {len(s)}")
print(f"Type: {type(s)}")

# Create empty set (note: {} creates dict, not set)
empty_set = set()
print(f"\nEmpty set: {empty_set}")
print(f"Type of empty_set: {type(empty_set)}")

# This creates a dictionary, not a set
dict_example = {}
print(f"Empty dict: {dict_example}")
print(f"Type of empty dict: {type(dict_example)}")


# ===== 2. SET OPERATIONS =====
print("\n" + "=" * 60)
print("2. SET OPERATIONS (UNION, INTERSECTION, DIFFERENCE)")
print("=" * 60 + "\n")

k1 = {1, 2, 3, 4, 5}
k2 = {4, 5, 6, 7, 8}
print(f"Set k1: {k1}")
print(f"Set k2: {k2}\n")

# Union - all elements from both sets
print(f"Union (k1 | k2): {k1 | k2}")  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection - common elements
print(f"Intersection (k1 & k2): {k1 & k2}")  # {4, 5}

# Difference - elements in k1 but not in k2
print(f"Difference (k1 - k2): {k1 - k2}")  # {1, 2, 3}

# Symmetric Difference - elements in either but not both
print(f"Symmetric Difference (k1 ^ k2): {k1 ^ k2}")  # {1, 2, 3, 6, 7, 8}


# ===== 3. SET RELATIONSHIPS =====
print("\n" + "=" * 60)
print("3. SET RELATIONSHIPS")
print("=" * 60 + "\n")

print(f"Is k1 a subset of k2? {k1.issubset(k2)}")  # False
print(f"Is k1 a superset of k2? {k1.issuperset(k2)}")  # False
print(f"Are k1 and k2 disjoint? {k1.isdisjoint(k2)}")  # False (they have common elements)


# ===== 4. SET METHODS (WITH STRINGS) =====
print("\n" + "=" * 60)
print("4. SET METHODS WITH STRING SETS")
print("=" * 60 + "\n")

p1 = {"sagir", "rahul", "akhtar", "python"}
p2 = {"python", "java", "c++", "sagir"}
print(f"Set p1: {p1}")
print(f"Set p2: {p2}\n")

# Union method
print(f"Union using .union(): {p1.union(p2)}")

# Intersection method
print(f"Intersection using .intersection(): {p1.intersection(p2)}")

# Difference method
print(f"Difference using .difference(): {p1.difference(p2)}")

# Symmetric difference method
print(f"Symmetric difference using .symmetric_difference(): {p1.symmetric_difference(p2)}")

# Relationships
print(f"\nIs p1 a subset of p2? {p1.issubset(p2)}")  # False
print(f"Is p1 a superset of p2? {p1.issuperset(p2)}")  # False


# ===== 5. SET MODIFICATION =====
print("\n" + "=" * 60)
print("5. SET MODIFICATION")
print("=" * 60 + "\n")

s = {1, 2, 3}
print(f"Original set: {s}")

# Add single element
s.add(4)
print(f"After add(4): {s}")

# Add multiple elements
s.update([5, 6, 7])
print(f"After update([5, 6, 7]): {s}")

# Remove element (error if not found)
s.remove(3)
print(f"After remove(3): {s}")

# Discard element (no error if not found)
s.discard(10)
print(f"After discard(10): {s}")

# Clear all elements
s_copy = {1, 2, 3, 4, 5}
s_copy.clear()
print(f"After clear(): {s_copy}")
print("Are p1 and p2 disjoint?", p1.isdisjoint(p2))  # Output: False
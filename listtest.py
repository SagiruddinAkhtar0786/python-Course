# =============================================================================
# PYTHON LISTS - COMPREHENSIVE GUIDE
# =============================================================================
# Lists are ordered, mutable (changeable) collections of items
# Lists can contain different data types

print("=" * 60)
print("PYTHON LISTS - OPERATIONS AND METHODS")
print("=" * 60)

# ===== 1. CREATING A LIST =====
print("\n1. CREATING A LIST\n")

marks = [30, 54, 64, 78, 9078, 90, 85, 72, 60, 45, 80]
print(f"Original list: {marks}")


# ===== 2. ITERATING THROUGH LIST =====
print("\n" + "=" * 60)
print("2. ITERATING THROUGH LIST")
print("=" * 60 + "\n")

print("Using enumerate (index and value):")
for index, mark in enumerate(marks):
    print(f"  Index {index}: {mark}")


# ===== 3. LIST MODIFICATION OPERATIONS =====
print("\n" + "=" * 60)
print("3. LIST MODIFICATION OPERATIONS")
print("=" * 60 + "\n")

# append - add element to end
marks.append(95)
print(f"After append(95): {marks}")

# insert - add element at specific index
marks.insert(2, 88)
print(f"After insert(2, 88): {marks}")

# remove - remove first occurrence of value
marks.remove(64)
print(f"After remove(64): {marks}")

# sort - sort in ascending order
marks.sort()
print(f"After sort(): {marks}")

# reverse - reverse the list
marks.reverse()
print(f"After reverse(): {marks}")


# ===== 4. LIST INFORMATION =====
print("\n" + "=" * 60)
print("4. LIST INFORMATION AND STATISTICS")
print("=" * 60 + "\n")

print(f"Length of list: {len(marks)}")
print(f"Maximum mark: {max(marks)}")
print(f"Minimum mark: {min(marks)}")
print(f"Average mark: {sum(marks) / len(marks):.2f}")
print(f"Count of 30: {marks.count(30)}")


# ===== 5. LIST COMPREHENSION =====
print("\n" + "=" * 60)
print("5. LIST COMPREHENSION")
print("=" * 60 + "\n")

# Get marks above 80
marks_above_80 = [mark for mark in marks if mark > 80]
print(f"Marks above 80: {marks_above_80}")
print(f"Number of marks above 80: {len(marks_above_80)}")

# Get marks between 50 and 80
marks_50_to_80 = [mark for mark in marks if 50 <= mark <= 80]
print(f"Marks between 50 and 80: {marks_50_to_80}")

# Sort in different orders
print(f"Marks in ascending order: {sorted(marks)}")
print(f"Marks in descending order: {sorted(marks, reverse=True)}")


# ===== 6. CONVERTING TO OTHER DATA TYPES =====
print("\n" + "=" * 60)
print("6. CONVERTING TO OTHER DATA TYPES")
print("=" * 60 + "\n")

print(f"Original list: {marks}")
print(f"As set (unique values): {set(marks)}")
print(f"As tuple: {tuple(marks)}")
print(f"As string: {str(marks)}")


# ===== 7. MORE LIST OPERATIONS =====
print("\n" + "=" * 60)
print("7. MORE LIST OPERATIONS")
print("=" * 60 + "\n")

# Slicing
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original: {test_list}")
print(f"First 5 elements: {test_list[:5]}")
print(f"Last 3 elements: {test_list[-3:]}")
print(f"Every 2nd element: {test_list[::2]}")
print(f"Reversed: {test_list[::-1]}")

# extend - add multiple elements
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(f"After extend: {list1}")

# copy - create a copy
original = [1, 2, 3]
copy = original.copy()
copy[0] = 999
print(f"Original: {original}, Copy: {copy}")
marks2 = [23,21,32]
joined_marks = marks + marks2
print("Joined marks:", joined_marks)

marks.extend(marks2)
print("Extended marks:", marks)
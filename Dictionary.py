# =============================================================================
# PYTHON DICTIONARIES - COMPREHENSIVE GUIDE
# =============================================================================
# A dictionary is an unordered collection of key-value pairs
# Dictionary is mutable (can be changed) and indexed by keys

print("=" * 60)
print("PYTHON DICTIONARIES")
print("=" * 60)

# ===== 1. CREATING AND BASIC OPERATIONS =====
print("\n1. CREATING AND BASIC OPERATIONS\n")

# Create a dictionary
dic = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "designation": "Software Engineer"
}

print("Dictionary:")
print(dic)
print(f"\nType: {type(dic)}")

# Access values by key
print(f"\nAccessing values by key:")
print(f"  dic['name'] = {dic['name']}")
print(f"  dic['age'] = {dic['age']}")
print(f"  dic['city'] = {dic['city']}")


# ===== 2. DICTIONARY METHODS =====
print("\n" + "=" * 60)
print("2. DICTIONARY METHODS")
print("=" * 60 + "\n")

# Get all keys
print("Keys in dictionary:")
for key in dic.keys():
    print(f"  - {key}")

# Get all values
print("\nValues in dictionary:")
for value in dic.values():
    print(f"  - {value}")

# Get key-value pairs
print("\nKey-Value pairs:")
for key, value in dic.items():
    print(f"  {key}: {value}")

# Using f-string to format
print(f"\nFormatted output:")
printquote = f"{dic['name']} is a {dic['age']} year old {dic['designation']} living in {dic['city']}."
print(f"  {printquote}")


# ===== 3. CREATING DICTIONARY FROM TUPLES =====
print("\n" + "=" * 60)
print("3. CREATING DICTIONARY FROM TUPLES")
print("=" * 60 + "\n")

# Convert list of tuples to dictionary
dic_from_tuples = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print("Dictionary from tuples:")
print(dic_from_tuples)
print(f"Type: {type(dic_from_tuples)}")


# ===== 4. MORE DICTIONARY OPERATIONS =====
print("\n" + "=" * 60)
print("4. MORE DICTIONARY OPERATIONS")
print("=" * 60 + "\n")

# Add new key-value pair
dic['salary'] = 150000
print(f"After adding salary: {dic}")

# Update existing value
dic['age'] = 31
print(f"After updating age: {dic}")

# Remove key-value pair
del dic['salary']
print(f"After deleting salary: {dic}")

# Get with default value
print(f"\nUsing .get() method:")
print(f"  dic.get('name'): {dic.get('name')}")
print(f"  dic.get('salary'): {dic.get('salary')}")
print(f"  dic.get('salary', 'Not found'): {dic.get('salary', 'Not found')}")

# Check if key exists
print(f"\nUsing 'in' operator:")
print(f"  'name' in dic: {'name' in dic}")
print(f"  'salary' in dic: {'salary' in dic}")


# ===== 5. NESTED DICTIONARIES =====
print("\n" + "=" * 60)
print("5. NESTED DICTIONARIES")
print("=" * 60 + "\n")

students = {
    "student1": {"name": "Ali", "grade": "A", "marks": 95},
    "student2": {"name": "Bob", "grade": "B", "marks": 85},
    "student3": {"name": "Charlie", "grade": "A", "marks": 92}
}

print("Nested Dictionary:")
for student_id, details in students.items():
    print(f"{student_id}: {details}")

print(f"\nAccessing nested values:")
print(f"  student1's name: {students['student1']['name']}")
print(f"  student1's marks: {students['student1']['marks']}")
print(f"  student2's grade: {students['student2']['grade']}")
# =============================================================================
# LAMBDA FUNCTIONS IN PYTHON
# =============================================================================
# Lambda is a small anonymous function
# Syntax: lambda arguments: expression
# Returns the result of the expression

print("=" * 60)
print("LAMBDA FUNCTIONS IN PYTHON")
print("=" * 60)

# ===== 1. BASIC LAMBDA FUNCTION =====
print("\n1. BASIC LAMBDA FUNCTION\n")

# Regular function
def add(a, b):
    return a + b

print(f"Regular function: add(5, 3) = {add(5, 3)}")

# Lambda function (same thing)
add_lambda = lambda a, b: a + b
print(f"Lambda function: add_lambda(5, 3) = {add_lambda(5, 3)}")


# ===== 2. SINGLE ARGUMENT LAMBDA =====
print("\n" + "=" * 60)
print("2. SINGLE ARGUMENT LAMBDA")
print("=" * 60 + "\n")

# Square a number
square = lambda x: x ** 2
print(f"square(5) = {square(5)}")
print(f"square(7) = {square(7)}")

# Check if number is positive
is_positive = lambda x: x > 0
print(f"is_positive(5) = {is_positive(5)}")
print(f"is_positive(-3) = {is_positive(-3)}")


# ===== 3. MULTIPLE ARGUMENTS LAMBDA =====
print("\n" + "=" * 60)
print("3. MULTIPLE ARGUMENTS LAMBDA")
print("=" * 60 + "\n")

# Multiply two numbers
multiply = lambda x, y: x * y
print(f"multiply(4, 6) = {multiply(4, 6)}")

# Find maximum
max_value = lambda a, b: a if a > b else b
print(f"max_value(10, 20) = {max_value(10, 20)}")

# Calculate area of rectangle
area = lambda length, width: length * width
print(f"area(5, 3) = {area(5, 3)}")


# ===== 4. LAMBDA WITH map() =====
print("\n" + "=" * 60)
print("4. LAMBDA WITH map() - APPLY FUNCTION TO ALL ITEMS")
print("=" * 60 + "\n")

numbers = [1, 2, 3, 4, 5]

# Double each number
doubled = list(map(lambda x: x * 2, numbers))
print(f"Original: {numbers}")
print(f"Doubled: {doubled}")

# Square each number
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared: {squared}")

# Convert to string
strings = list(map(lambda x: f"Number: {x}", numbers))
print(f"As strings: {strings}")


# ===== 5. LAMBDA WITH filter() =====
print("\n" + "=" * 60)
print("5. LAMBDA WITH filter() - FILTER ITEMS")
print("=" * 60 + "\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Get numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"Greater than 5: {greater_than_5}")

# Get numbers divisible by 3
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
print(f"Divisible by 3: {divisible_by_3}")


# ===== 6. LAMBDA WITH sort() =====
print("\n" + "=" * 60)
print("6. LAMBDA WITH sorted() - CUSTOM SORT")
print("=" * 60 + "\n")

students = [
    {"name": "Ali", "score": 85},
    {"name": "Sara", "score": 92},
    {"name": "Hassan", "score": 78}
]

# Sort by score
sorted_by_score = sorted(students, key=lambda student: student["score"])
print("Sorted by score (ascending):")
for student in sorted_by_score:
    print(f"  {student['name']}: {student['score']}")

# Sort by name
sorted_by_name = sorted(students, key=lambda student: student["name"])
print("\nSorted by name:")
for student in sorted_by_name:
    print(f"  {student['name']}: {student['score']}")

# Sort in descending order
sorted_desc = sorted(students, key=lambda student: student["score"], reverse=True)
print("\nSorted by score (descending):")
for student in sorted_desc:
    print(f"  {student['name']}: {student['score']}")


# ===== 7. LAMBDA WITH reduce() =====
print("\n" + "=" * 60)
print("7. LAMBDA WITH reduce() - ACCUMULATE RESULTS")
print("=" * 60 + "\n")

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print(f"Sum of {numbers} = {total}")

# Multiply all numbers
product = reduce(lambda x, y: x * y, numbers)
print(f"Product of {numbers} = {product}")

# Find maximum
max_num = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum: {max_num}")

# Concatenate strings
words = ["Hello", "World", "Python"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(f"Concatenated: {sentence}")


# ===== 8. LAMBDA WITH DEFAULT ARGUMENTS =====
print("\n" + "=" * 60)
print("8. LAMBDA WITH DEFAULT ARGUMENTS")
print("=" * 60 + "\n")

# Lambda with default value
greet = lambda name="Guest": f"Hello, {name}!"
print(greet())
print(greet("Ali"))

# Multiply with default multiplier
multiply_by = lambda x, factor=2: x * factor
print(f"multiply_by(5) = {multiply_by(5)}")
print(f"multiply_by(5, 3) = {multiply_by(5, 3)}")


# ===== 9. PRACTICAL EXAMPLES =====
print("\n" + "=" * 60)
print("9. PRACTICAL EXAMPLES")
print("=" * 60 + "\n")

# Example 1: Convert Celsius to Fahrenheit
celsius_list = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius_list))
print(f"Celsius: {celsius_list}")
print(f"Fahrenheit: {fahrenheit}")

# Example 2: Filter words by length
words = ["apple", "py", "javascript", "java", "c", "python"]
long_words = list(filter(lambda w: len(w) > 3, words))
print(f"\nWords longer than 3 chars: {long_words}")

# Example 3: Sort products by price
products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Phone", "price": 20000},
    {"name": "Tablet", "price": 15000}
]
sorted_products = sorted(products, key=lambda p: p["price"])
print("\nProducts sorted by price:")
for product in sorted_products:
    print(f"  {product['name']}: Rs. {product['price']}")

# Example 4: Double even numbers only
numbers = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x * 2 if x % 2 == 0 else x, numbers))
print(f"\nDouble even numbers: {result}")


# ===== 10. LAMBDA VS REGULAR FUNCTION =====
print("\n" + "=" * 60)
print("10. LAMBDA vs REGULAR FUNCTION")
print("=" * 60 + "\n")

# Regular function - more readable for complex logic
def is_even(x):
    """Check if number is even"""
    return x % 2 == 0

# Lambda function
is_even_lambda = lambda x: x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

print("Using regular function:")
evens_regular = list(filter(is_even, numbers))
print(f"  evens: {evens_regular}")

print("\nUsing lambda:")
evens_lambda = list(filter(is_even_lambda, numbers))
print(f"  evens: {evens_lambda}")


# ===== 11. WHEN TO USE LAMBDA =====
print("\n" + "=" * 60)
print("11. WHEN TO USE LAMBDA")
print("=" * 60 + "\n")

print("""
✓ USE LAMBDA WHEN:
  - Function is used only once
  - Function is simple (one line)
  - Used as argument to map(), filter(), sorted(), reduce()
  - Short callback functions

✗ DON'T USE LAMBDA WHEN:
  - Function is complex or multiple lines
  - Function is reused multiple times
  - Needs comments or documentation
  - Want clear error messages and debugging

Better to use regular def functions in those cases!
""")

print("\n✓ Lambda tutorial completed!")

# Lambda version - shorter
is_even_lambda = lambda x: x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
print(f"Filter with regular function: {list(filter(is_even, numbers))}")
print(f"Filter with lambda: {list(filter(is_even_lambda, numbers))}")
print("Both work, but choose based on readability!")


print("\n✓ All Lambda examples completed!")

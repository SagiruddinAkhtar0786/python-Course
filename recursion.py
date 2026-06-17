# =============================================================================
# RECURSION IN PYTHON
# =============================================================================
# Recursion is when a function calls itself
# Every recursive function must have:
# 1. Base case (stop condition)
# 2. Recursive case (function calls itself with different argument)

print("=" * 60)
print("RECURSION IN PYTHON")
print("=" * 60)

# ===== 1. FACTORIAL FUNCTION =====
print("\n1. FACTORIAL USING RECURSION\n")

def factorial(n):
    """Calculate factorial of n recursively
    
    Factorial of n = n * (n-1) * (n-2) * ... * 1
    Example: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
    
    Base case: factorial(0) = 1, factorial(1) = 1
    Recursive case: factorial(n) = n * factorial(n-1)
    """
    # Base case: stop the recursion
    if n == 0 or n == 1:
        return 1
    # Recursive case: call function with smaller value
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number to find its factorial: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")

# Show some examples
print("\nFactorial examples:")
for i in range(6):
    print(f"  factorial({i}) = {factorial(i)}")


# ===== 2. FIBONACCI SEQUENCE =====
print("\n" + "=" * 60)
print("2. FIBONACCI SEQUENCE USING RECURSION")
print("=" * 60 + "\n")

def fibonacci(n):
    """Generate nth Fibonacci number recursively
    
    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    Each number is sum of the two preceding numbers
    
    Base case: fib(0)=0, fib(1)=1
    Recursive case: fib(n) = fib(n-1) + fib(n-2)
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("First 10 Fibonacci numbers:")
for i in range(10):
    print(f"  fib({i}) = {fibonacci(i)}")


# ===== 3. SUM OF DIGITS =====
print("\n" + "=" * 60)
print("3. SUM OF DIGITS USING RECURSION")
print("=" * 60 + "\n")

def sum_of_digits(n):
    """Calculate sum of digits of n recursively
    
    Example: sum_of_digits(123) = 1 + 2 + 3 = 6
    
    Base case: if n < 10, return n
    Recursive case: return (n % 10) + sum_of_digits(n // 10)
    """
    if n < 10:
        return n
    else:
        return (n % 10) + sum_of_digits(n // 10)

test_num = int(input("\nEnter a number to find sum of its digits: "))
digit_sum = sum_of_digits(test_num)
print(f"Sum of digits of {test_num} is {digit_sum}")

print("\nSum of digits examples:")
for num in [15, 123, 456, 999]:
    print(f"  sum_of_digits({num}) = {sum_of_digits(num)}")


# ===== 4. POWER FUNCTION =====
print("\n" + "=" * 60)
print("4. POWER FUNCTION USING RECURSION")
print("=" * 60 + "\n")

def power(base, exp):
    """Calculate base^exp recursively
    
    Example: power(2, 3) = 2 * 2 * 2 = 8
    
    Base case: if exp == 0, return 1
    Recursive case: return base * power(base, exp - 1)
    """
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

print("Power examples:")
for b in [2, 3, 5]:
    for e in [1, 2, 3]:
        print(f"  power({b}, {e}) = {power(b, e)}")


# ===== 5. HOW RECURSION WORKS =====
print("\n" + "=" * 60)
print("5. HOW RECURSION WORKS - CALL STACK")
print("=" * 60 + "\n")

print("Tracing factorial(4):")
print("""
factorial(4) calls factorial(3)
  factorial(3) calls factorial(2)
    factorial(2) calls factorial(1)
      factorial(1) returns 1 (BASE CASE)
    factorial(2) = 2 * 1 = 2
  factorial(3) = 3 * 2 = 6
factorial(4) = 4 * 6 = 24

Call Stack (going down, then up):
  factorial(4)
    factorial(3)
      factorial(2)
        factorial(1) <- BASE CASE
      result = 2
    result = 6
  result = 24
""")

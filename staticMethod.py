# =============================================================================
# STATIC METHODS IN PYTHON
# =============================================================================
# Static methods are methods that belong to a class rather than an instance
# They don't have access to instance data (self) or class data (cls)
# Use @staticmethod decorator

print("=" * 60)
print("STATIC METHODS IN PYTHON")
print("=" * 60)

# ===== 1. BASIC STATIC METHOD =====
print("\n1. BASIC STATIC METHOD")
print("=" * 60 + "\n")


class MathOperations:
    """Class with static methods for math operations"""
    
    @staticmethod
    def add(a, b):
        """Static method - no access to self or cls"""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Static method"""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """Static method"""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """Static method with validation"""
        if b == 0:
            return "Cannot divide by zero"
        return a / b


# Call static methods without creating an instance
print(f"Add: {MathOperations.add(10, 5)}")
print(f"Subtract: {MathOperations.subtract(10, 5)}")
print(f"Multiply: {MathOperations.multiply(10, 5)}")
print(f"Divide: {MathOperations.divide(10, 5)}")
print(f"Divide by zero: {MathOperations.divide(10, 0)}")

# Can also call from instance (but not recommended)
math_obj = MathOperations()
print(f"\nFrom instance: {math_obj.add(7, 3)}")


# ===== 2. INSTANCE METHOD vs STATIC METHOD =====
print("\n2. INSTANCE METHOD vs STATIC METHOD")
print("=" * 60 + "\n")


class Temperature:
    """Demonstrates difference between instance and static methods"""
    
    def __init__(self, celsius):
        self.celsius = celsius
    
    # Instance method (has access to self)
    def to_fahrenheit(self):
        """Instance method - uses self"""
        return (self.celsius * 9/5) + 32
    
    # Static method (no access to self)
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Static method - doesn't use self"""
        return (celsius * 9/5) + 32
    
    # Instance method (no parameters except self)
    def get_celsius(self):
        """Instance method"""
        return self.celsius


# Using instance method
temp = Temperature(25)
print(f"Instance method - celsius: {temp.celsius}°C")
print(f"Instance method - to_fahrenheit(): {temp.to_fahrenheit()}°F")

# Using static method
print(f"\nStatic method - celsius_to_fahrenheit(25): {Temperature.celsius_to_fahrenheit(25)}°F")
print(f"Static method - celsius_to_fahrenheit(0): {Temperature.celsius_to_fahrenheit(0)}°F")
print(f"Static method - celsius_to_fahrenheit(100): {Temperature.celsius_to_fahrenheit(100)}°F")


# ===== 3. WHEN TO USE STATIC METHODS =====
print("\n3. WHEN TO USE STATIC METHODS")
print("=" * 60 + "\n")


class StringUtils:
    """Utility class with static methods"""
    
    @staticmethod
    def reverse_string(text):
        """Reverse a string"""
        return text[::-1]
    
    @staticmethod
    def count_vowels(text):
        """Count vowels in a string"""
        vowels = "aeiouAEIOU"
        return sum(1 for char in text if char in vowels)
    
    @staticmethod
    def is_palindrome(text):
        """Check if string is palindrome"""
        cleaned = text.lower().replace(" ", "")
        return cleaned == cleaned[::-1]
    
    @staticmethod
    def capitalize_words(text):
        """Capitalize each word"""
        return " ".join(word.capitalize() for word in text.split())


# These methods don't need instance data
print(f"Reverse: {StringUtils.reverse_string('hello')}")
print(f"Vowels in 'python': {StringUtils.count_vowels('python')}")
print(f"Is 'racecar' palindrome: {StringUtils.is_palindrome('racecar')}")
print(f"Capitalize: {StringUtils.capitalize_words('hello world from python')}")


# ===== 4. CLASS METHOD vs STATIC METHOD =====
print("\n4. CLASS METHOD vs STATIC METHOD")
print("=" * 60 + "\n")


class Counter:
    """Demonstrates @classmethod vs @staticmethod"""
    
    count = 0  # Class variable
    
    def __init__(self, name):
        self.name = name
        Counter.count += 1
    
    @classmethod
    def get_total_count(cls):
        """Class method - has access to cls (class)"""
        return f"Total Counter objects: {cls.count}"
    
    @classmethod
    def create_from_dict(cls, data):
        """Class method - factory pattern"""
        return cls(data['name'])
    
    @staticmethod
    def describe_class():
        """Static method - no access to cls or self"""
        return "Counter class is used to count objects"


# Create instances
c1 = Counter("Counter1")
c2 = Counter("Counter2")
c3 = Counter("Counter3")

# Class method can access class variables
print(f"Class method: {Counter.get_total_count()}")

# Static method cannot access class variables
print(f"Static method: {Counter.describe_class()}")

# Factory pattern with class method
new_counter = Counter.create_from_dict({'name': 'NewCounter'})
print(f"Created from dict: {new_counter.name}")
print(f"Class method after new creation: {Counter.get_total_count()}")


# ===== 5. STATIC METHODS IN INHERITANCE =====
print("\n5. STATIC METHODS IN INHERITANCE")
print("=" * 60 + "\n")


class Parent:
    """Parent class with static method"""
    
    @staticmethod
    def static_method():
        return "Parent static method"
    
    def instance_method(self):
        return "Parent instance method"


class Child(Parent):
    """Child class inheriting static method"""
    
    @staticmethod
    def static_method():
        return "Child static method"  # Override
    
    def instance_method(self):
        return "Child instance method"  # Override


# Static methods can be overridden in child class
print(f"Parent.static_method(): {Parent.static_method()}")
print(f"Child.static_method(): {Child.static_method()}")

# But they're not truly polymorphic (don't use self)
obj = Child()
print(f"\nCalling from Child instance:")
print(f"obj.static_method(): {obj.static_method()}")


# ===== 6. PRACTICAL EXAMPLE: CALCULATOR =====
print("\n6. PRACTICAL EXAMPLE: CALCULATOR WITH STATIC METHODS")
print("=" * 60 + "\n")


class Calculator:
    """Calculator with various static methods"""
    
    @staticmethod
    def power(base, exponent):
        """Calculate power"""
        return base ** exponent
    
    @staticmethod
    def square_root(num):
        """Calculate square root"""
        if num < 0:
            return "Cannot calculate square root of negative number"
        return num ** 0.5
    
    @staticmethod
    def factorial(n):
        """Calculate factorial"""
        if n < 0:
            return "Factorial not defined for negative numbers"
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    @staticmethod
    def is_even(num):
        """Check if number is even"""
        return num % 2 == 0
    
    @staticmethod
    def gcd(a, b):
        """Calculate Greatest Common Divisor"""
        while b:
            a, b = b, a % b
        return a


print(f"2^5 = {Calculator.power(2, 5)}")
print(f"√16 = {Calculator.square_root(16)}")
print(f"5! = {Calculator.factorial(5)}")
print(f"Is 10 even? {Calculator.is_even(10)}")
print(f"GCD(48, 18) = {Calculator.gcd(48, 18)}")


# ===== 7. PRACTICAL EXAMPLE: DATE UTILITIES =====
print("\n7. PRACTICAL EXAMPLE: DATE UTILITIES")
print("=" * 60 + "\n")


class DateUtils:
    """Utility class with date-related static methods"""
    
    @staticmethod
    def is_leap_year(year):
        """Check if year is leap year"""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    @staticmethod
    def days_in_month(month, year):
        """Get number of days in a month"""
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 29 if DateUtils.is_leap_year(year) else 28
        else:
            return "Invalid month"
    
    @staticmethod
    def format_date(day, month, year):
        """Format date as string"""
        return f"{day:02d}/{month:02d}/{year}"
    
    @staticmethod
    def get_day_name(day_num):
        """Get day name from number (0=Monday, 6=Sunday)"""
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[day_num % 7] if 0 <= day_num < 7 else "Invalid day"


print(f"Is 2024 leap year? {DateUtils.is_leap_year(2024)}")
print(f"Is 2023 leap year? {DateUtils.is_leap_year(2023)}")
print(f"Days in February 2024: {DateUtils.days_in_month(2, 2024)}")
print(f"Days in February 2023: {DateUtils.days_in_month(2, 2023)}")
print(f"Formatted date: {DateUtils.format_date(15, 3, 2024)}")
print(f"Day name: {DateUtils.get_day_name(2)}")


# ===== 8. PRACTICAL EXAMPLE: VALIDATION =====
print("\n8. PRACTICAL EXAMPLE: VALIDATION UTILITIES")
print("=" * 60 + "\n")


class Validator:
    """Validation utility class with static methods"""
    
    @staticmethod
    def is_valid_email(email):
        """Check if email is valid (simple check)"""
        return "@" in email and "." in email
    
    @staticmethod
    def is_valid_phone(phone):
        """Check if phone is valid"""
        return len(phone) >= 10 and phone.replace("-", "").isdigit()
    
    @staticmethod
    def is_strong_password(password):
        """Check if password is strong"""
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*" for c in password)
        return len(password) >= 8 and has_upper and has_lower and has_digit
    
    @staticmethod
    def is_valid_username(username):
        """Check if username is valid"""
        return 3 <= len(username) <= 20 and username.replace("_", "").isalnum()


print(f"Valid email 'user@example.com': {Validator.is_valid_email('user@example.com')}")
print(f"Valid email 'invalid-email': {Validator.is_valid_email('invalid-email')}")
print(f"Valid phone '1234567890': {Validator.is_valid_phone('1234567890')}")
print(f"Valid phone '123-456-7890': {Validator.is_valid_phone('123-456-7890')}")
print(f"Strong password 'Pass123!': {Validator.is_strong_password('Pass123!')}")
print(f"Strong password 'weak': {Validator.is_strong_password('weak')}")
print(f"Valid username 'john_doe': {Validator.is_valid_username('john_doe')}")
print(f"Valid username 'a': {Validator.is_valid_username('a')}")


# ===== 9. STATIC METHOD CALLED FROM OTHER METHODS =====
print("\n9. STATIC METHOD CALLED FROM OTHER METHODS")
print("=" * 60 + "\n")


class BankAccount:
    """Bank account with static and instance methods"""
    
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    @staticmethod
    def is_valid_amount(amount):
        """Static method for validation"""
        return isinstance(amount, (int, float)) and amount > 0
    
    def deposit(self, amount):
        """Instance method calling static method"""
        if BankAccount.is_valid_amount(amount):
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
            return True
        else:
            print(f"Invalid amount: ${amount}")
            return False
    
    def withdraw(self, amount):
        """Instance method calling static method"""
        if not BankAccount.is_valid_amount(amount):
            print(f"Invalid amount: ${amount}")
            return False
        
        if amount > self.balance:
            print("Insufficient balance!")
            return False
        
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")
        return True


account = BankAccount("ACC123", 1000)
account.deposit(500)
account.withdraw(300)
account.deposit(-100)  # Invalid
account.withdraw(2000)  # Insufficient


# ===== 10. SUMMARY =====
print("\n" + "=" * 60)
print("SUMMARY: STATIC METHODS")
print("=" * 60)
print("""
KEY POINTS:
✓ Static methods use @staticmethod decorator
✓ Don't have access to self or cls
✓ Called on class, not on instance
✓ Useful for utility functions related to the class
✓ Can be inherited but can't access class variables
✓ Don't participate in polymorphism

SYNTAX:
    class MyClass:
        @staticmethod
        def my_static_method(param1, param2):
            return param1 + param2
    
    # Call on class
    result = MyClass.my_static_method(10, 20)
    
    # Or on instance (but not recommended)
    obj = MyClass()
    result = obj.my_static_method(10, 20)

WHEN TO USE:
• Utility functions related to a class
• No access to instance or class state needed
• Functions that logically belong to a class
• Factory methods (use @classmethod instead)
• Helper/validation methods

COMPARISON:
┌──────────────┬─────────────────┬──────────────────┬────────────────┐
│ Method Type  │ Decorator       │ Parameters       │ Access         │
├──────────────┼─────────────────┼──────────────────┼────────────────┤
│ Instance     │ None            │ self, *args      │ self, cls      │
│ Class        │ @classmethod    │ cls, *args       │ cls only       │
│ Static       │ @staticmethod   │ *args (no self)  │ Nothing        │
└──────────────┴─────────────────┴──────────────────┴────────────────┘
""")

print("\n" + "=" * 60)
print("✓ STATIC METHODS TUTORIAL COMPLETED!")
print("=" * 60)

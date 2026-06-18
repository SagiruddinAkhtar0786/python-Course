# =============================================================================
# GETTERS AND SETTERS IN PYTHON
# =============================================================================
# Getters and setters provide controlled access to object attributes
# Python offers multiple approaches using methods and decorators

print("=" * 60)
print("GETTERS AND SETTERS IN PYTHON")
print("=" * 60)

# ===== 1. BASIC GETTER AND SETTER METHODS =====
print("\n1. BASIC GETTER AND SETTER METHODS\n")


class Person:
    """Person class with basic getter and setter methods"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Getter method for name
    def get_name(self):
        return self.name
    
    # Setter method for name
    def set_name(self, name):
        self.name = name
    
    # Getter method for age
    def get_age(self):
        return self.age
    
    # Setter method for age
    def set_age(self, age):
        self.age = age


# Using basic getter and setter
person = Person("Alice", 25)
print(f"Name: {person.get_name()}")
print(f"Age: {person.get_age()}")

person.set_name("Bob")
person.set_age(30)
print(f"Updated Name: {person.get_name()}")
print(f"Updated Age: {person.get_age()}")


# ===== 2. USING @property DECORATOR =====
print("\n" + "=" * 60)
print("2. USING @property DECORATOR")
print("=" * 60 + "\n")


class Student:
    """Student class using @property decorator (Python way)"""
    
    def __init__(self, name, marks):
        self._name = name  # Convention: _ prefix for "private" attributes
        self._marks = marks
    
    # Getter for name using @property
    @property
    def name(self):
        """Get student name"""
        return self._name
    
    # Getter for marks
    @property
    def marks(self):
        """Get student marks"""
        return self._marks


student = Student("Charlie", 95)
print(f"Student name: {student.name}")
print(f"Student marks: {student.marks}")

# Note: You can read using . notation like regular attributes
# This is more Pythonic than get_name()


# ===== 3. USING @property WITH SETTER =====
print("\n" + "=" * 60)
print("3. USING @property WITH SETTER")
print("=" * 60 + "\n")


class BankAccount:
    """Bank account with property getter and setter"""
    
    def __init__(self, account_holder, balance):
        self._account_holder = account_holder
        self._balance = balance
    
    @property
    def balance(self):
        """Get account balance"""
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        """Set account balance with validation"""
        if amount < 0:
            print("Error: Balance cannot be negative!")
            return
        self._balance = amount
    
    @property
    def account_holder(self):
        return self._account_holder
    
    @account_holder.setter
    def account_holder(self, name):
        if not name.strip():
            print("Error: Name cannot be empty!")
            return
        self._account_holder = name


# Using property with setter
account = BankAccount("Alice", 1000)
print(f"Account holder: {account.account_holder}")
print(f"Balance: {account.balance}")

# Modify using setter
account.balance = 1500
print(f"Updated balance: {account.balance}")

# Try invalid balance (will show error)
account.balance = -500
print(f"Balance after invalid attempt: {account.balance}")


# ===== 4. VALIDATION IN SETTERS =====
print("\n" + "=" * 60)
print("4. VALIDATION IN SETTERS")
print("=" * 60 + "\n")


class Product:
    """Product with validation in setters"""
    
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        """Price must be positive"""
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        self._price = value
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        """Quantity must be non-negative"""
        if value < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        """Name cannot be empty"""
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value
    
    def display(self):
        print(f"Product: {self._name}")
        print(f"  Price: ${self._price}")
        print(f"  Quantity: {self._quantity}")


product = Product("Laptop", 1000, 5)
product.display()

print("\nUpdating product details...")
product.price = 1200
product.quantity = 3
product.display()

# Try invalid values
print("\nTrying to set invalid price...")
try:
    product.price = -100
except ValueError as e:
    print(f"Error: {e}")


# ===== 5. NAME MANGLING (PRIVATE ATTRIBUTES) =====
print("\n" + "=" * 60)
print("5. NAME MANGLING (PRIVATE ATTRIBUTES)")
print("=" * 60 + "\n")


class BankCard:
    """Bank card with private PIN using name mangling"""
    
    def __init__(self, card_number, pin):
        self._card_number = card_number
        self.__pin = pin  # Double underscore for name mangling
    
    @property
    def card_number(self):
        """Get last 4 digits of card"""
        return self._card_number[-4:]
    
    @property
    def pin(self):
        """Prevent direct access to PIN"""
        raise AttributeError("PIN is private and cannot be accessed directly")
    
    def verify_pin(self, entered_pin):
        """Verify if entered PIN is correct"""
        return self.__pin == entered_pin


card = BankCard("1234567890123456", "1234")
print(f"Card number (last 4 digits): {card.card_number}")

# Try to access PIN
print("\nTrying to access PIN directly...")
try:
    print(card.pin)
except AttributeError as e:
    print(f"Error: {e}")

# Verify PIN (correct way)
print("\nVerifying PIN:")
print(f"PIN is correct: {card.verify_pin('1234')}")
print(f"PIN is correct: {card.verify_pin('9999')}")


# ===== 6. GETTER ONLY (READ-ONLY PROPERTY) =====
print("\n" + "=" * 60)
print("6. GETTER ONLY (READ-ONLY PROPERTY)")
print("=" * 60 + "\n")


class Circle:
    """Circle with read-only calculated properties"""
    
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def diameter(self):
        """Calculated property - read-only"""
        return 2 * self._radius
    
    @property
    def area(self):
        """Calculated property - read-only"""
        import math
        return math.pi * self._radius ** 2
    
    @property
    def circumference(self):
        """Calculated property - read-only"""
        import math
        return 2 * math.pi * self._radius


circle = Circle(5)
print(f"Radius: {circle.radius}")
print(f"Diameter: {circle.diameter}")
print(f"Area: {circle.area:.2f}")
print(f"Circumference: {circle.circumference:.2f}")

# You can modify radius, but not diameter/area/circumference
circle.radius = 10
print(f"\nAfter changing radius to 10:")
print(f"Diameter: {circle.diameter}")
print(f"Area: {circle.area:.2f}")


# ===== 7. COMPARISON: DIRECT VS PROPERTY =====
print("\n" + "=" * 60)
print("7. COMPARISON: DIRECT ACCESS VS PROPERTY")
print("=" * 60 + "\n")

print("""
DIRECT ATTRIBUTE ACCESS (Not recommended for control):
    class Person:
        def __init__(self, age):
            self.age = age
    
    person = Person(25)
    person.age = -5  # No validation!

USING PROPERTY (Recommended for validation):
    class Person:
        def __init__(self, age):
            self._age = age
        
        @property
        def age(self):
            return self._age
        
        @age.setter
        def age(self, value):
            if value < 0:
                raise ValueError("Age cannot be negative")
            self._age = value
    
    person = Person(25)
    person.age = -5  # Raises ValueError!

BENEFITS OF PROPERTIES:
✓ Validation of values
✓ Calculated/derived values
✓ Change internal representation without breaking API
✓ Add side effects (logging, triggering actions)
✓ Read-only properties (getter only)
✓ Pythonic interface (looks like attribute access)
""")


# ===== 8. PRACTICAL EXAMPLE: USER PROFILE =====
print("\n" + "=" * 60)
print("8. PRACTICAL EXAMPLE: USER PROFILE")
print("=" * 60 + "\n")


class UserProfile:
    """User profile with comprehensive getters and setters"""
    
    def __init__(self, username, email, age):
        self._username = username
        self._email = email
        self._age = age
        self._login_count = 0
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters")
        self._username = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email format")
        self._email = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 13 or value > 120:
            raise ValueError("Age must be between 13 and 120")
        self._age = value
    
    @property
    def login_count(self):
        """Read-only property"""
        return self._login_count
    
    def login(self):
        """Increment login count"""
        self._login_count += 1
        print(f"{self._username} logged in (total: {self._login_count})")
    
    def profile_info(self):
        print(f"Username: {self._username}")
        print(f"Email: {self._email}")
        print(f"Age: {self._age}")
        print(f"Logins: {self._login_count}")


user = UserProfile("alice123", "alice@example.com", 25)
user.profile_info()

print("\nLogging in...")
user.login()
user.login()
user.login()

print("\nUpdating profile...")
user.email = "alice.new@example.com"
user.age = 26
user.profile_info()


print("\n" + "=" * 60)
print("✓ GETTERS AND SETTERS TUTORIAL COMPLETED!")
print("=" * 60)

# =============================================================================
# CLASS METHODS AS ALTERNATE CONSTRUCTORS
# =============================================================================
# Class methods can act as alternative constructors to create instances
# in different ways using @classmethod decorator

print("=" * 70)
print("CLASS METHODS AS ALTERNATE CONSTRUCTORS")
print("=" * 70)

# ===== 1. BASIC CONSTRUCTOR (__init__) =====
print("\n1. BASIC CONSTRUCTOR (__init__)")
print("=" * 70 + "\n")


class Person:
    """Person class with basic constructor"""
    
    def __init__(self, name, age):
        """Primary constructor - requires name and age"""
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Create person using __init__
person1 = Person("Alice", 25)
person1.display()


# ===== 2. ALTERNATE CONSTRUCTOR FROM STRING =====
print("\n2. ALTERNATE CONSTRUCTOR FROM STRING")
print("=" * 70 + "\n")


class Student:
    """Student class with alternate constructor"""
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    @classmethod
    def from_string(cls, student_info):
        """Alternate constructor - create from 'name,grade' string"""
        name, grade = student_info.split(",")
        return cls(name, int(grade))
    
    def display(self):
        print(f"Student: {self.name}, Grade: {self.grade}")


# Create student using primary constructor
s1 = Student("Alice", 10)
s1.display()

# Create student using alternate constructor from string
s2 = Student.from_string("Bob,11")
s2.display()

s3 = Student.from_string("Charlie,12")
s3.display()


# ===== 3. ALTERNATE CONSTRUCTOR FROM DICTIONARY =====
print("\n3. ALTERNATE CONSTRUCTOR FROM DICTIONARY")
print("=" * 70 + "\n")


class Product:
    """Product class with alternate constructors"""
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    @classmethod
    def from_dict(cls, data):
        """Alternate constructor - create from dictionary"""
        return cls(data['name'], data['price'], data['quantity'])
    
    def display(self):
        print(f"Product: {self.name}")
        print(f"  Price: ${self.price}")
        print(f"  Quantity: {self.quantity}")
        print(f"  Total Value: ${self.price * self.quantity}")


# Create product using primary constructor
p1 = Product("Laptop", 1000, 5)
p1.display()

print()

# Create product using alternate constructor from dictionary
product_data = {
    'name': 'Mouse',
    'price': 25,
    'quantity': 50
}
p2 = Product.from_dict(product_data)
p2.display()


# ===== 4. MULTIPLE ALTERNATE CONSTRUCTORS =====
print("\n4. MULTIPLE ALTERNATE CONSTRUCTORS")
print("=" * 70 + "\n")


class Date:
    """Date class with multiple alternate constructors"""
    
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    @classmethod
    def from_string(cls, date_string):
        """From 'dd-mm-yyyy' format"""
        day, month, year = date_string.split("-")
        return cls(int(day), int(month), int(year))
    
    @classmethod
    def from_iso(cls, iso_string):
        """From 'yyyy-mm-dd' format (ISO 8601)"""
        year, month, day = iso_string.split("-")
        return cls(int(day), int(month), int(year))
    
    @classmethod
    def today(cls):
        """Current date (hardcoded for demo)"""
        return cls(22, 6, 2026)
    
    def display(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")
    
    def __str__(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"


# Different ways to create a Date
d1 = Date(15, 3, 2024)
print(f"Primary constructor: {d1}")

d2 = Date.from_string("15-03-2024")
print(f"From string (dd-mm-yyyy): {d2}")

d3 = Date.from_iso("2024-03-15")
print(f"From ISO format (yyyy-mm-dd): {d3}")

d4 = Date.today()
print(f"Today's date: {d4}")


# ===== 5. ALTERNATE CONSTRUCTOR FROM JSON STRING =====
print("\n5. ALTERNATE CONSTRUCTOR FROM JSON STRING")
print("=" * 70 + "\n")

import json


class Employee:
    """Employee class with JSON constructor"""
    
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary
    
    @classmethod
    def from_json(cls, json_string):
        """Create from JSON string"""
        data = json.loads(json_string)
        return cls(data['name'], data['designation'], data['salary'])
    
    def to_json(self):
        """Convert to JSON string"""
        data = {
            'name': self.name,
            'designation': self.designation,
            'salary': self.salary
        }
        return json.dumps(data)
    
    def display(self):
        print(f"{self.name}")
        print(f"  Designation: {self.designation}")
        print(f"  Salary: ${self.salary:,}")


# Create employee from JSON
json_data = '{"name": "John Doe", "designation": "Senior Developer", "salary": 120000}'
emp1 = Employee.from_json(json_data)
emp1.display()

print()

# Create employee normally and convert to JSON
emp2 = Employee("Jane Smith", "Project Manager", 95000)
emp2.display()
print(f"\nJSON representation: {emp2.to_json()}")


# ===== 6. ALTERNATE CONSTRUCTOR FOR UNIT CONVERSION =====
print("\n6. ALTERNATE CONSTRUCTOR FOR UNIT CONVERSION")
print("=" * 70 + "\n")


class Distance:
    """Distance class with multiple unit constructors"""
    
    def __init__(self, kilometers):
        """Primary constructor - stores in kilometers"""
        self.kilometers = kilometers
    
    @classmethod
    def from_meters(cls, meters):
        """Create from meters"""
        return cls(meters / 1000)
    
    @classmethod
    def from_miles(cls, miles):
        """Create from miles"""
        return cls(miles * 1.60934)
    
    @classmethod
    def from_feet(cls, feet):
        """Create from feet"""
        return cls(feet * 0.0003048)
    
    def to_meters(self):
        return self.kilometers * 1000
    
    def to_miles(self):
        return self.kilometers / 1.60934
    
    def to_feet(self):
        return self.kilometers / 0.0003048
    
    def display(self):
        print(f"Distance: {self.kilometers} km")
        print(f"  = {self.to_meters():.2f} meters")
        print(f"  = {self.to_miles():.2f} miles")
        print(f"  = {self.to_feet():.2f} feet")


# Create distances using different units
d1 = Distance.from_kilometers = Distance(5)  # 5 km

d2 = Distance.from_meters(5000)  # 5000 meters = 5 km
print("5 km:")
d2.display()

print()

d3 = Distance.from_miles(3.10686)  # ~5 km
print("~3.1 miles:")
d3.display()

print()

d4 = Distance.from_feet(16404.2)  # ~5 km
print("~16404 feet:")
d4.display()


# ===== 7. ALTERNATE CONSTRUCTOR FOR PARSING CSV =====
print("\n7. ALTERNATE CONSTRUCTOR FOR PARSING CSV")
print("=" * 70 + "\n")


class Book:
    """Book class with CSV parsing constructor"""
    
    def __init__(self, title, author, isbn, pages):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.pages = pages
    
    @classmethod
    def from_csv_line(cls, csv_line):
        """Parse CSV line: title,author,isbn,pages"""
        title, author, isbn, pages = csv_line.split(",")
        return cls(title, author, isbn, int(pages))
    
    def display(self):
        print(f"Title: {self.title}")
        print(f"  Author: {self.author}")
        print(f"  ISBN: {self.isbn}")
        print(f"  Pages: {self.pages}")


# CSV data
csv_line1 = "Python Basics,John Smith,ISBN-001,350"
csv_line2 = "Advanced Python,Jane Doe,ISBN-002,450"

book1 = Book.from_csv_line(csv_line1)
book1.display()

print()

book2 = Book.from_csv_line(csv_line2)
book2.display()


# ===== 8. ALTERNATE CONSTRUCTOR WITH VALIDATION =====
print("\n8. ALTERNATE CONSTRUCTOR WITH VALIDATION")
print("=" * 70 + "\n")


class Email:
    """Email class with validation"""
    
    def __init__(self, address):
        if "@" not in address or "." not in address:
            raise ValueError("Invalid email format")
        self.address = address
    
    @classmethod
    def from_parts(cls, username, domain):
        """Create email from username and domain parts"""
        email_address = f"{username}@{domain}"
        return cls(email_address)
    
    def display(self):
        print(f"Email: {self.address}")


# Create email using primary constructor
e1 = Email("john@example.com")
e1.display()

# Create email using alternate constructor
e2 = Email.from_parts("jane", "example.com")
e2.display()

print("\nTrying invalid format:")
try:
    e3 = Email("invalid-email")
except ValueError as e:
    print(f"Error: {e}")


# ===== 9. FACTORY PATTERN WITH MULTIPLE TYPES =====
print("\n9. FACTORY PATTERN - CREATING DIFFERENT USER TYPES")
print("=" * 70 + "\n")


class User:
    """Base user class with alternate constructors for different roles"""
    
    def __init__(self, username, email, role, permissions=None):
        self.username = username
        self.email = email
        self.role = role
        self.permissions = permissions or []
    
    @classmethod
    def admin(cls, username, email):
        """Create admin user"""
        return cls(username, email, "admin", 
                  ["read", "write", "delete", "manage_users"])
    
    @classmethod
    def moderator(cls, username, email):
        """Create moderator user"""
        return cls(username, email, "moderator",
                  ["read", "write", "delete"])
    
    @classmethod
    def user(cls, username, email):
        """Create regular user"""
        return cls(username, email, "user",
                  ["read", "write"])
    
    @classmethod
    def guest(cls, username):
        """Create guest user"""
        return cls(username, f"{username}@guest.local", "guest",
                  ["read"])
    
    def display(self):
        print(f"Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Role: {self.role}")
        print(f"  Permissions: {', '.join(self.permissions)}")


# Create different types of users
admin = User.admin("admin_user", "admin@example.com")
admin.display()

print()

moderator = User.moderator("mod_user", "moderator@example.com")
moderator.display()

print()

regular = User.user("john", "john@example.com")
regular.display()

print()

guest = User.guest("visitor")
guest.display()


# ===== 10. CHAINING ALTERNATE CONSTRUCTORS =====
print("\n10. CHAINING WITH ALTERNATE CONSTRUCTORS")
print("=" * 70 + "\n")


class Temperature:
    """Temperature class with multiple constructors"""
    
    def __init__(self, celsius):
        self.celsius = celsius
    
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        """Create from Fahrenheit"""
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)
    
    @classmethod
    def from_kelvin(cls, kelvin):
        """Create from Kelvin"""
        celsius = kelvin - 273.15
        return cls(celsius)
    
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    def to_kelvin(self):
        return self.celsius + 273.15
    
    def display(self):
        print(f"Temperature:")
        print(f"  Celsius: {self.celsius:.2f}°C")
        print(f"  Fahrenheit: {self.to_fahrenheit():.2f}°F")
        print(f"  Kelvin: {self.to_kelvin():.2f}K")


# Create temperatures using different units
t1 = Temperature(25)
print("From Celsius (25°C):")
t1.display()

print()

t2 = Temperature.from_fahrenheit(77)
print("From Fahrenheit (77°F):")
t2.display()

print()

t3 = Temperature.from_kelvin(298.15)
print("From Kelvin (298.15K):")
t3.display()


# ===== 11. PRACTICAL EXAMPLE: CONFIGURATION LOADER =====
print("\n11. PRACTICAL EXAMPLE: CONFIGURATION LOADER")
print("=" * 70 + "\n")


class Config:
    """Configuration class with multiple constructors"""
    
    def __init__(self, host, port, database, debug):
        self.host = host
        self.port = port
        self.database = database
        self.debug = debug
    
    @classmethod
    def development(cls):
        """Development configuration"""
        return cls("localhost", 5000, "dev_db", True)
    
    @classmethod
    def production(cls):
        """Production configuration"""
        return cls("api.example.com", 443, "prod_db", False)
    
    @classmethod
    def testing(cls):
        """Testing configuration"""
        return cls("test-server", 8000, "test_db", False)
    
    @classmethod
    def from_dict(cls, config_dict):
        """Load from dictionary"""
        return cls(
            config_dict.get('host'),
            config_dict.get('port'),
            config_dict.get('database'),
            config_dict.get('debug', False)
        )
    
    def display(self):
        print(f"Host: {self.host}")
        print(f"Port: {self.port}")
        print(f"Database: {self.database}")
        print(f"Debug: {self.debug}")


print("Development Configuration:")
dev_config = Config.development()
dev_config.display()

print("\nProduction Configuration:")
prod_config = Config.production()
prod_config.display()

print("\nTesting Configuration:")
test_config = Config.testing()
test_config.display()

print("\nFrom Dictionary:")
custom_config = Config.from_dict({
    'host': 'custom-host',
    'port': 9000,
    'database': 'custom_db',
    'debug': True
})
custom_config.display()


# ===== 12. SUMMARY =====
print("\n" + "=" * 70)
print("SUMMARY: CLASS METHODS AS ALTERNATE CONSTRUCTORS")
print("=" * 70)
print("""
WHAT ARE ALTERNATE CONSTRUCTORS?
• Additional ways to create objects using @classmethod
• Provide flexibility in object creation
• Different input formats or data sources

COMMON USE CASES:
✓ Parse from string (CSV, JSON, formatted strings)
✓ Unit conversion (meters to kilometers, etc.)
✓ Factory patterns (create different object types)
✓ Load from dictionaries or external data
✓ Pre-configured instances (dev, prod, test configs)

SYNTAX:
    class MyClass:
        def __init__(self, param1, param2):
            self.param1 = param1
            self.param2 = param2
        
        @classmethod
        def from_string(cls, data_string):
            param1, param2 = data_string.split(",")
            return cls(param1, param2)
        
        @classmethod
        def from_dict(cls, data_dict):
            return cls(data_dict['param1'], data_dict['param2'])

USAGE:
    # Normal constructor
    obj1 = MyClass("value1", "value2")
    
    # Alternate constructors
    obj2 = MyClass.from_string("value1,value2")
    obj3 = MyClass.from_dict({'param1': 'value1', 'param2': 'value2'})

BENEFITS:
✓ More flexible object creation
✓ Cleaner code for complex initialization
✓ Easy to add new creation methods
✓ Better code organization
✓ Supports multiple data formats
""")

print("\n" + "=" * 70)
print("✓ ALTERNATE CONSTRUCTORS TUTORIAL COMPLETED!")
print("=" * 70)

# =============================================================================
# METHOD OVERLOADING AND METHOD OVERRIDING IN PYTHON
# =============================================================================
# Method Overriding: Redefining a method in a child class
# Method Overloading: Having multiple methods with same name (not in Python)

print("=" * 70)
print("METHOD OVERLOADING AND METHOD OVERRIDING IN PYTHON")
print("=" * 70)

# ===== 1. METHOD OVERRIDING (BASIC) =====
print("\n1. METHOD OVERRIDING (BASIC)")
print("=" * 70 + "\n")

print("""
METHOD OVERRIDING:
• Child class redefines a method from parent class
• Allows customization of inherited behavior
• Child's method replaces parent's method
""")


class Animal:
    """Parent class"""
    
    def make_sound(self):
        print("Some generic sound")
    
    def move(self):
        print("Moving...")


class Dog(Animal):
    """Child class overriding make_sound"""
    
    def make_sound(self):  # Override parent method
        print("Woof! Woof!")


class Cat(Animal):
    """Child class overriding make_sound"""
    
    def make_sound(self):  # Override parent method
        print("Meow! Meow!")


# Create instances
dog = Dog()
cat = Cat()
animal = Animal()

print("Animal sounds:")
animal.make_sound()
dog.make_sound()
cat.make_sound()


# ===== 2. METHOD OVERRIDING WITH SUPER() =====
print("\n2. METHOD OVERRIDING WITH SUPER()")
print("=" * 70 + "\n")


class Vehicle:
    """Parent class"""
    
    def __init__(self, brand):
        self.brand = brand
    
    def display_info(self):
        print(f"Brand: {self.brand}")
    
    def start(self):
        print("Vehicle starting...")


class Car(Vehicle):
    """Child class overriding with super()"""
    
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent constructor
        self.model = model
    
    def display_info(self):
        super().display_info()  # Call parent method
        print(f"Model: {self.model}")  # Add child-specific info
    
    def start(self):
        super().start()  # Call parent method
        print("Car engine started!")


class Bike(Vehicle):
    """Another child class"""
    
    def __init__(self, brand, engine_type):
        super().__init__(brand)
        self.engine_type = engine_type
    
    def display_info(self):
        super().display_info()
        print(f"Engine: {self.engine_type}")
    
    def start(self):
        super().start()
        print("Bike engine roaring!")


car = Car("Toyota", "Camry")
bike = Bike("Harley", "V-Twin")

print("Car information:")
car.display_info()
car.start()

print("\nBike information:")
bike.display_info()
bike.start()


# ===== 3. PRACTICAL EXAMPLE: EMPLOYEE TYPES =====
print("\n3. PRACTICAL EXAMPLE: EMPLOYEE TYPES")
print("=" * 70 + "\n")


class Employee:
    """Base employee class"""
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def calculate_bonus(self):
        """Default bonus calculation"""
        return self.salary * 0.05  # 5% bonus
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary:,}")
        print(f"Bonus: ${self.calculate_bonus():,.2f}")


class Manager(Employee):
    """Manager class overriding bonus calculation"""
    
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    
    def calculate_bonus(self):
        """Managers get 10% + team bonus"""
        base_bonus = self.salary * 0.10
        team_bonus = self.team_size * 100
        return base_bonus + team_bonus
    
    def display_info(self):
        super().display_info()
        print(f"Team Size: {self.team_size}")


class Developer(Employee):
    """Developer class overriding bonus calculation"""
    
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    
    def calculate_bonus(self):
        """Developers get 8% bonus"""
        return self.salary * 0.08
    
    def display_info(self):
        super().display_info()
        print(f"Language: {self.language}")


class Intern(Employee):
    """Intern class overriding bonus calculation"""
    
    def calculate_bonus(self):
        """Interns get 2% bonus"""
        return self.salary * 0.02


emp = Employee("John", 50000)
mgr = Manager("Alice", 80000, 5)
dev = Developer("Bob", 70000, "Python")
intern = Intern("Charlie", 20000)

print("Employee bonuses:")
emp.display_info()
print()
mgr.display_info()
print()
dev.display_info()
print()
intern.display_info()


# ===== 4. POLYMORPHISM THROUGH OVERRIDING =====
print("\n4. POLYMORPHISM THROUGH OVERRIDING")
print("=" * 70 + "\n")

print("""
POLYMORPHISM:
• Objects of different classes respond to the same method call
• Each class implements the method differently
• Same interface, different behavior
""")


class Shape:
    """Base shape class"""
    
    def area(self):
        return 0
    
    def display(self):
        print(f"Area: {self.area()}")


class Circle(Shape):
    """Circle overriding area calculation"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    """Rectangle overriding area calculation"""
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width


class Triangle(Shape):
    """Triangle overriding area calculation"""
    
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height


# Polymorphism: Same method, different behavior
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4)
]

print("Shape areas (polymorphism):")
for shape in shapes:
    shape.display()


# ===== 5. METHOD OVERLOADING IN PYTHON (DEFAULT PARAMETERS) =====
print("\n5. METHOD OVERLOADING IN PYTHON (DEFAULT PARAMETERS)")
print("=" * 70 + "\n")

print("""
NOTE: Python doesn't support traditional method overloading
(multiple methods with same name but different parameters).

Instead, use:
1. Default parameters
2. Variable-length arguments (*args, **kwargs)
3. Type checking
""")


class Calculator:
    """Calculator with flexible add method"""
    
    def add(self, a, b, c=0, d=0):
        """Add 2, 3, or 4 numbers"""
        return a + b + c + d


calc = Calculator()
print(f"add(5, 3) = {calc.add(5, 3)}")
print(f"add(5, 3, 2) = {calc.add(5, 3, 2)}")
print(f"add(5, 3, 2, 1) = {calc.add(5, 3, 2, 1)}")


# ===== 6. METHOD OVERLOADING WITH *args =====
print("\n6. METHOD OVERLOADING WITH *args")
print("=" * 70 + "\n")


class Printer:
    """Printer with flexible print method"""
    
    def print_items(self, *items):
        """Print any number of items"""
        for item in items:
            print(f"  - {item}")


printer = Printer()

print("Printing 1 item:")
printer.print_items("Apple")

print("\nPrinting 3 items:")
printer.print_items("Apple", "Banana", "Cherry")

print("\nPrinting 5 items:")
printer.print_items("Apple", "Banana", "Cherry", "Date", "Elderberry")


# ===== 7. METHOD OVERLOADING WITH TYPE CHECKING =====
print("\n7. METHOD OVERLOADING WITH TYPE CHECKING")
print("=" * 70 + "\n")


class DataProcessor:
    """Process different data types"""
    
    def process(self, data):
        """Process data based on type"""
        if isinstance(data, list):
            return self._process_list(data)
        elif isinstance(data, dict):
            return self._process_dict(data)
        elif isinstance(data, str):
            return self._process_string(data)
        else:
            return f"Unknown type: {type(data)}"
    
    def _process_list(self, data):
        return f"List with {len(data)} items: {data}"
    
    def _process_dict(self, data):
        return f"Dict with {len(data)} keys: {list(data.keys())}"
    
    def _process_string(self, data):
        return f"String: '{data}' (length: {len(data)})"


processor = DataProcessor()

print(processor.process([1, 2, 3, 4]))
print(processor.process({"name": "Alice", "age": 25}))
print(processor.process("Hello World"))


# ===== 8. ABSTRACT METHODS AND OVERRIDING =====
print("\n8. ABSTRACT METHODS AND OVERRIDING")
print("=" * 70 + "\n")

from abc import ABC, abstractmethod


class Database(ABC):
    """Abstract base class"""
    
    @abstractmethod
    def connect(self):
        """Must be overridden"""
        pass
    
    @abstractmethod
    def query(self, sql):
        """Must be overridden"""
        pass
    
    @abstractmethod
    def close(self):
        """Must be overridden"""
        pass


class MySQLDatabase(Database):
    """MySQL implementation"""
    
    def connect(self):
        print("Connecting to MySQL...")
    
    def query(self, sql):
        print(f"MySQL executing: {sql}")
    
    def close(self):
        print("MySQL connection closed")


class PostgresDatabase(Database):
    """PostgreSQL implementation"""
    
    def connect(self):
        print("Connecting to PostgreSQL...")
    
    def query(self, sql):
        print(f"PostgreSQL executing: {sql}")
    
    def close(self):
        print("PostgreSQL connection closed")


# Use abstract methods
mysql = MySQLDatabase()
mysql.connect()
mysql.query("SELECT * FROM users")
mysql.close()

print()

postgres = PostgresDatabase()
postgres.connect()
postgres.query("SELECT * FROM products")
postgres.close()


# ===== 9. METHOD RESOLUTION ORDER (MRO) =====
print("\n9. METHOD RESOLUTION ORDER (MRO)")
print("=" * 70 + "\n")


class A:
    def method(self):
        print("A's method")


class B(A):
    def method(self):
        print("B's method")


class C(A):
    def method(self):
        print("C's method")


class D(B, C):
    pass


d = D()
d.method()

print(f"\nMRO for D: {D.__mro__}")


# ===== 10. PRACTICAL EXAMPLE: PAYMENT SYSTEM =====
print("\n10. PRACTICAL EXAMPLE: PAYMENT SYSTEM")
print("=" * 70 + "\n")


class Payment(ABC):
    """Abstract payment class"""
    
    def __init__(self, amount):
        self.amount = amount
    
    @abstractmethod
    def process(self):
        pass
    
    @abstractmethod
    def get_fee(self):
        pass


class CreditCardPayment(Payment):
    """Credit card payment"""
    
    def process(self):
        fee = self.get_fee()
        total = self.amount + fee
        print(f"Processing credit card payment: ${self.amount}")
        print(f"Fee: ${fee}")
        print(f"Total: ${total}")
    
    def get_fee(self):
        return self.amount * 0.03  # 3% fee


class PayPalPayment(Payment):
    """PayPal payment"""
    
    def process(self):
        fee = self.get_fee()
        total = self.amount + fee
        print(f"Processing PayPal payment: ${self.amount}")
        print(f"Fee: ${fee}")
        print(f"Total: ${total}")
    
    def get_fee(self):
        return self.amount * 0.02  # 2% fee


class BankTransferPayment(Payment):
    """Bank transfer payment"""
    
    def process(self):
        fee = self.get_fee()
        total = self.amount + fee
        print(f"Processing bank transfer: ${self.amount}")
        print(f"Fee: ${fee}")
        print(f"Total: ${total}")
    
    def get_fee(self):
        return 5.0  # Fixed fee


# Process different payments
payments = [
    CreditCardPayment(100),
    PayPalPayment(100),
    BankTransferPayment(100)
]

for payment in payments:
    payment.process()
    print()


# ===== 11. COMPARISON TABLE =====
print("=" * 70)
print("OVERRIDING vs OVERLOADING")
print("=" * 70)
print("""
OVERRIDING:
✓ Child class redefines parent's method
✓ Same method name, same parameters
✓ Replaces parent's implementation
✓ Supports polymorphism
✓ Happens at runtime
✓ Requires inheritance

OVERLOADING:
✗ NOT DIRECTLY SUPPORTED in Python
✓ Use default parameters instead
✓ Use *args, **kwargs instead
✓ Use type checking instead
✓ Multiple functions with different behavior
✓ Compile-time resolution (Java, C++)

PYTHON ALTERNATIVES TO OVERLOADING:
1. Default parameters:
   def add(self, a, b, c=0): pass

2. Variable arguments:
   def add(self, *args): pass

3. Type checking:
   def process(self, data):
       if isinstance(data, list): ...
       elif isinstance(data, dict): ...

4. Separate methods:
   def add_int(self, a, b): pass
   def add_list(self, a, b): pass
""")

print("\n" + "=" * 70)
print("✓ METHOD OVERRIDING AND OVERLOADING TUTORIAL COMPLETED!")
print("=" * 70)

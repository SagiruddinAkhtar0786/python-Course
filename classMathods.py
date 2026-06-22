# =============================================================================
# CLASS METHODS IN PYTHON
# =============================================================================
# Class methods use @classmethod decorator and receive cls as first parameter
# They can access and modify class variables

print("=" * 70)
print("CLASS METHODS IN PYTHON")
print("=" * 70)

# ===== 0. IMPORTANT: UNDERSTANDING YOUR CODE QUESTION =====
print("\n0. WHY self.name WORKS WITHOUT BEING DECLARED IN __init__")
print("=" * 70 + "\n")

print("""
YOUR QUESTION: How does self.name work if it's not declared in display_info()?

ANSWER: Python allows you to dynamically add attributes to objects anytime!

In your code:
    e1 = Employee()
    e1.name = "John Doe"  ← This CREATES the attribute on the fly
    e1.salary = 50000     ← This CREATES another attribute on the fly

When display_info() runs, it can access these attributes via self.name
because they exist on the object, even though they were created outside __init__!

HOWEVER, this is BAD PRACTICE! You should initialize them in __init__.
""")

# BEFORE (Bad Practice - Your Original Code)
print("\n--- BAD PRACTICE (Your Original Code) ---\n")


class EmployeeBad:    
    company = "Apple"  # Class variable

    def display_info(self):
        # This works only if name and salary were added to the object elsewhere
        print(f"Name: {self.name}, Salary: {self.salary}")  
        
    # BUG: Missing @classmethod decorator!
    def changeCompany(cls, new_company):
        cls.company = new_company


e1_bad = EmployeeBad()
e1_bad.name = "John Doe"  # Adding attributes dynamically (BAD!)
e1_bad.salary = 50000     # Adding attributes dynamically (BAD!)
e1_bad.display_info()
print(f"Company: {e1_bad.company}")

print("\nProblem: What if someone forgets to add name/salary?")
try:
    e2_bad = EmployeeBad()
    e2_bad.display_info()  # ERROR! AttributeError
except AttributeError as e:
    print(f"ERROR: {e}")


# ===== 1. CORRECT WAY: INITIALIZE IN __init__ =====
print("\n" + "=" * 70)
print("1. CORRECT WAY: INITIALIZE IN __init__")
print("=" * 70 + "\n")


class Employee:    
    company = "Apple"  # Class variable

    def __init__(self, name, salary):  # Initialize instance variables here!
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")  
        
    # Correct: Now it has @classmethod decorator
    @classmethod
    def changeCompany(cls, new_company):
        cls.company = new_company  # Change class variable


e1 = Employee("John Doe", 50000)  # Pass values to __init__
e1.display_info()
print(f"Company: {e1.company}")

e2 = Employee("Jane Smith", 60000)
e2.display_info()
print(f"Company: {e2.company}")


# ===== 2. INSTANCE VARIABLES vs LOCAL VARIABLES =====
print("\n" + "=" * 70)
print("2. INSTANCE VARIABLES vs LOCAL VARIABLES")
print("=" * 70 + "\n")


class Car:
    def __init__(self, model):
        self.model = model  # INSTANCE variable (with self.)
        color = "red"       # LOCAL variable (without self.)
    
    def display(self):
        print(f"Model: {self.model}")  # This works (instance variable)
        # print(color)  # ERROR! LOCAL variables don't persist
    
    def check_color(self):
        print("Can I access color here?")
        try:
            print(f"Color: {color}")  # This will fail!
        except NameError as e:
            print(f"ERROR: {e}")


car = Car("Honda")
car.display()
car.check_color()

print("\nKEY DIFFERENCE:")
print("✓ self.model persists - it's an instance variable")
print("✗ color doesn't persist - it's just a local variable in __init__")


# ===== 3. BASIC CLASS METHOD =====
print("\n" + "=" * 70)
print("3. BASIC CLASS METHOD")
print("=" * 70 + "\n")


class Student:
    school_name = "Lincoln High"  # Class variable
    total_students = 0  # Class variable
    
    def __init__(self, name, grade):
        self.name = name  # Instance variable
        self.grade = grade  # Instance variable
        Student.total_students += 1  # Increment class variable
    
    def display_info(self):
        print(f"{self.name} - Grade: {self.grade}, School: {self.school_name}")
    
    @classmethod
    def get_total_students(cls):
        """Class method - receives cls instead of self"""
        return cls.total_students
    
    @classmethod
    def change_school_name(cls, new_name):
        """Class method - can modify class variables"""
        cls.school_name = new_name
    
    @classmethod
    def create_from_string(cls, student_info):
        """Class method - factory pattern"""
        name, grade = student_info.split(",")
        return cls(name, int(grade))


# Create students
s1 = Student("Alice", 10)
s2 = Student("Bob", 11)
s3 = Student("Charlie", 10)

s1.display_info()
s2.display_info()

print(f"\nTotal students: {Student.get_total_students()}")

# Use class method to change class variable
Student.change_school_name("Lincoln High School")

print("\nAfter changing school name:")
s1.display_info()
s2.display_info()

# Use class method as factory
s4 = Student.create_from_string("Diana,12")
s4.display_info()
print(f"Total students now: {Student.get_total_students()}")


# ===== 4. INSTANCE METHOD vs CLASS METHOD vs STATIC METHOD =====
print("\n" + "=" * 70)
print("4. INSTANCE METHOD vs CLASS METHOD vs STATIC METHOD")
print("=" * 70 + "\n")


class Calculator:
    pi = 3.14159  # Class variable
    
    def __init__(self, name):
        self.name = name  # Instance variable
    
    # INSTANCE METHOD - has access to self (instance data)
    def describe(self):
        print(f"I am {self.name}")
    
    # CLASS METHOD - has access to cls (class data)
    @classmethod
    def get_pi(cls):
        return cls.pi
    
    @classmethod
    def update_pi(cls, new_pi):
        cls.pi = new_pi
    
    # STATIC METHOD - has access to neither self nor cls
    @staticmethod
    def add(a, b):
        return a + b


calc = Calculator("MyCalc")
calc.describe()  # Instance method

print(f"Pi: {Calculator.get_pi()}")  # Class method
print(f"Add 5 + 3: {Calculator.add(5, 3)}")  # Static method

Calculator.update_pi(3.14159265)  # Class method
print(f"Updated Pi: {Calculator.get_pi()}")


# ===== 5. CLASS METHOD MODIFYING CLASS VARIABLES =====
print("\n" + "=" * 70)
print("5. CLASS METHOD MODIFYING CLASS VARIABLES")
print("=" * 70 + "\n")


class BankAccount:
    bank_name = "MyBank"
    interest_rate = 0.05
    total_accounts = 0
    
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        BankAccount.total_accounts += 1
    
    def display(self):
        print(f"{self.account_holder}: ${self.balance} ({BankAccount.bank_name})")
    
    @classmethod
    def set_interest_rate(cls, rate):
        """Class method to change interest rate for all accounts"""
        cls.interest_rate = rate
        print(f"Interest rate updated to {rate * 100}%")
    
    @classmethod
    def get_bank_status(cls):
        """Class method to get bank information"""
        return f"{cls.bank_name}: {cls.total_accounts} accounts, {cls.interest_rate * 100}% interest"


acc1 = BankAccount("Alice", 5000)
acc2 = BankAccount("Bob", 10000)
acc3 = BankAccount("Charlie", 7500)

acc1.display()
acc2.display()

print(f"\n{BankAccount.get_bank_status()}")

BankAccount.set_interest_rate(0.07)

print(f"{BankAccount.get_bank_status()}")


# ===== 6. CLASS METHOD VS ACCESSING CLASS DIRECTLY =====
print("\n" + "=" * 70)
print("6. CLASS METHOD vs ACCESSING CLASS DIRECTLY")
print("=" * 70 + "\n")


class Configuration:
    app_version = "1.0"
    debug_mode = False
    
    @classmethod
    def set_version(cls, version):
        """Using class method"""
        cls.app_version = version


print("Method 1: Using class method")
Configuration.set_version("2.0")
print(f"Version: {Configuration.app_version}")

print("\nMethod 2: Direct access (also works but less flexible)")
Configuration.app_version = "3.0"
print(f"Version: {Configuration.app_version}")

print("""
Why use class methods?
✓ Encapsulation - validation logic can be added
✓ Inheritance - subclasses can override the method
✓ Polymorphism - different classes can behave differently
✓ Clearer intent - shows this modifies class state
""")


# ===== 7. INHERITANCE WITH CLASS METHODS =====
print("\n" + "=" * 70)
print("7. INHERITANCE WITH CLASS METHODS")
print("=" * 70 + "\n")


class Animal:
    species_count = 0
    
    def __init__(self, name):
        self.name = name
        Animal.species_count += 1
    
    @classmethod
    def get_species_count(cls):
        return f"{cls.__name__}: {cls.species_count}"


class Dog(Animal):
    species_count = 0  # Separate counter for Dog


class Cat(Animal):
    species_count = 0  # Separate counter for Cat


d1 = Dog("Rex")
d2 = Dog("Buddy")

c1 = Cat("Whiskers")
c2 = Cat("Mittens")
c3 = Cat("Fluffy")

print(Dog.get_species_count())
print(Cat.get_species_count())
print(Animal.get_species_count())


# ===== 8. CLASS METHOD AS FACTORY (DESIGN PATTERN) =====
print("\n" + "=" * 70)
print("8. CLASS METHOD AS FACTORY (DESIGN PATTERN)")
print("=" * 70 + "\n")


class User:
    def __init__(self, username, email, role="user"):
        self.username = username
        self.email = email
        self.role = role
    
    @classmethod
    def from_dict(cls, data):
        """Factory method - create from dictionary"""
        return cls(data['username'], data['email'], data.get('role', 'user'))
    
    @classmethod
    def from_string(cls, user_string):
        """Factory method - create from string"""
        parts = user_string.split(",")
        return cls(parts[0], parts[1], parts[2] if len(parts) > 2 else "user")
    
    @classmethod
    def admin(cls, username, email):
        """Factory method - create admin user"""
        return cls(username, email, "admin")
    
    def display(self):
        print(f"{self.username} ({self.email}) - Role: {self.role}")


# Create users using different factory methods
user1 = User("alice", "alice@example.com")
user1.display()

user2 = User.from_dict({'username': 'bob', 'email': 'bob@example.com', 'role': 'moderator'})
user2.display()

user3 = User.from_string("charlie,charlie@example.com,user")
user3.display()

user4 = User.admin("diana", "diana@example.com")
user4.display()


# ===== 9. PRACTICAL EXAMPLE: CONFIGURATION MANAGER =====
print("\n" + "=" * 70)
print("9. PRACTICAL EXAMPLE: CONFIGURATION MANAGER")
print("=" * 70 + "\n")


class Config:
    """Global configuration manager using class methods"""
    
    # Class variables
    env = "development"
    debug = True
    database_url = "localhost:5432"
    max_connections = 10
    
    @classmethod
    def load_production(cls):
        """Load production configuration"""
        cls.env = "production"
        cls.debug = False
        cls.database_url = "prod-db.example.com:5432"
        cls.max_connections = 100
        print("✓ Production configuration loaded")
    
    @classmethod
    def load_development(cls):
        """Load development configuration"""
        cls.env = "development"
        cls.debug = True
        cls.database_url = "localhost:5432"
        cls.max_connections = 10
        print("✓ Development configuration loaded")
    
    @classmethod
    def load_testing(cls):
        """Load testing configuration"""
        cls.env = "testing"
        cls.debug = False
        cls.database_url = "test-db:5432"
        cls.max_connections = 5
        print("✓ Testing configuration loaded")
    
    @classmethod
    def get_config(cls):
        """Get current configuration"""
        return f"""
Configuration: {cls.env.upper()}
  Debug: {cls.debug}
  Database: {cls.database_url}
  Max Connections: {cls.max_connections}
"""


print("Current configuration:")
print(Config.get_config())

Config.load_production()
print("After loading production:")
print(Config.get_config())

Config.load_testing()
print("After loading testing:")
print(Config.get_config())


# ===== 10. SUMMARY =====
print("\n" + "=" * 70)
print("SUMMARY: CLASS METHODS")
print("=" * 70)
print("""
CLASS METHODS:
✓ Use @classmethod decorator
✓ First parameter is cls (not self)
✓ Access and modify class variables
✓ Can't access instance variables
✓ Called on class or instance
✓ Inherited by subclasses

SYNTAX:
    class MyClass:
        class_var = 10
        
        @classmethod
        def my_class_method(cls):
            return cls.class_var

WHEN TO USE:
• Factory methods (create instances in different ways)
• Modifying class variables
• Operations on the class itself
• Alternative constructors
• Configuration management

COMPARISON TABLE:
╔──────────────┬──────────────┬─────────────┬────────────────╗
║ Method Type  │ Decorator    │ Parameter   │ Access         ║
╠──════────────╬──────────────╬─────────────╬────────────────╣
║ Instance     │ None         │ self        │ Instance data  ║
║ Class        │ @classmethod │ cls         │ Class data     ║
║ Static       │ @staticmethod│ None        │ Nothing        ║
╚──────────────╩──────────────╩─────────────╩────────────────╝

ABOUT YOUR CODE:
Problem 1: Instance variables should be initialized in __init__
   ✓ Good: self.name set in __init__
   ✗ Bad: e1.name = "..." set after object creation

Problem 2: changeCompany method is missing @classmethod decorator
   ✗ Should be: @classmethod def changeCompany(cls, ...)
   ✓ Then call: Employee.changeCompany("NewCompany")
""")

print("\n" + "=" * 70)
print("✓ CLASS METHODS TUTORIAL COMPLETED!")
print("=" * 70)
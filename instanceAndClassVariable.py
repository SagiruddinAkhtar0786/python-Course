# =============================================================================
# INSTANCE AND CLASS VARIABLES IN PYTHON
# =============================================================================
# Instance variables: unique to each object
# Class variables: shared across all objects of the class

print("=" * 70)
print("INSTANCE AND CLASS VARIABLES IN PYTHON")
print("=" * 70)

# ===== 1. INSTANCE VARIABLES =====
print("\n1. INSTANCE VARIABLES")
print("=" * 70 + "\n")
print("Instance variables are unique to each object")
print("Each instance has its own copy of the variable\n")


class Student:
    """Student class with instance variables"""
    
    def __init__(self, name, marks):
        # Instance variables - each object has its own copy
        self.name = name
        self.marks = marks
    
    def display_info(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


# Create instances
student1 = Student("Alice", 85)
student2 = Student("Bob", 92)
student3 = Student("Charlie", 78)

print("Instance variables are unique to each object:\n")
print("Student 1:")
student1.display_info()  # Alice, 85

print("\nStudent 2:")
student2.display_info()  # Bob, 92

print("\nStudent 3:")
student3.display_info()  # Charlie, 78

print("\nChanging student1's marks doesn't affect others:")
student1.marks = 95
student1.display_info()

print("Student 2 still has original marks:")
student2.display_info()


# ===== 2. CLASS VARIABLES =====
print("\n" + "=" * 70)
print("2. CLASS VARIABLES")
print("=" * 70 + "\n")
print("Class variables are shared across all instances\n")


class Employee:
    """Employee class with class variable"""
    
    # Class variable - shared by all instances
    company_name = "TechCorp"
    total_employees = 0
    
    def __init__(self, name, salary):
        # Instance variables
        self.name = name
        self.salary = salary
        
        # Modify class variable
        Employee.total_employees += 1
    
    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {self.company_name}")


# Create employees
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
emp3 = Employee("Charlie", 55000)

print("Employees created:")
emp1.display_info()
emp2.display_info()
emp3.display_info()

print(f"\nTotal employees (class variable): {Employee.total_employees}")
print(f"Company name (class variable): {Employee.company_name}")

print("\nChanging class variable affects all instances:")
Employee.company_name = "NewTechCorp"
emp1.display_info()
emp2.display_info()
emp3.display_info()


# ===== 3. INSTANCE vs CLASS VARIABLES =====
print("\n" + "=" * 70)
print("3. INSTANCE vs CLASS VARIABLES - COMPARISON")
print("=" * 70 + "\n")


class Car:
    """Car class to demonstrate both types of variables"""
    
    # CLASS VARIABLES (defined outside __init__)
    total_cars = 0  # Shared by all instances
    brand = "Generic"
    manufacturing_year = 2025
    
    def __init__(self, model, color, price):
        # INSTANCE VARIABLES (defined with self)
        self.model = model  # Unique to each car
        self.color = color  # Unique to each car
        self.price = price  # Unique to each car
        self.owner = None   # Unique to each car
        
        # Increment class variable
        Car.total_cars += 1
    
    def display_info(self):
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Price: ${self.price}")
        print(f"Owner: {self.owner}")
        print(f"Brand: {self.brand} (class variable)")
        print(f"Year: {self.manufacturing_year} (class variable)")
    
    def set_owner(self, owner_name):
        self.owner = owner_name


# Create cars
car1 = Car("Civic", "Red", 25000)
car2 = Car("Accord", "Blue", 35000)
car3 = Car("CR-V", "Black", 40000)

print("Car 1:")
car1.display_info()

print("\nCar 2:")
car2.display_info()

print(f"\nTotal cars (class variable): {Car.total_cars}")

# Modify instance variables
car1.set_owner("Alice")
car2.set_owner("Bob")

print("\nAfter setting owners:")
print(f"Car 1 owner: {car1.owner}")
print(f"Car 2 owner: {car2.owner}")
print(f"Car 3 owner: {car3.owner}")  # None, as owner not set

# Modify class variable
Car.brand = "Toyota"
print("\nAfter changing brand to 'Toyota':")
print(f"Car 1 brand: {car1.brand}")
print(f"Car 2 brand: {car2.brand}")
print(f"Car 3 brand: {car3.brand}")


# ===== 4. ACCESSING VARIABLES =====
print("\n" + "=" * 70)
print("4. ACCESSING INSTANCE AND CLASS VARIABLES")
print("=" * 70 + "\n")


class Product:
    """Product class"""
    
    # Class variables
    store_name = "MyStore"
    tax_rate = 0.10
    
    def __init__(self, name, price):
        # Instance variables
        self.name = name
        self.price = price


product1 = Product("Laptop", 1000)
product2 = Product("Mouse", 50)

print("ACCESS INSTANCE VARIABLES:")
print(f"product1.name: {product1.name}")
print(f"product1.price: {product1.price}")
print(f"product2.name: {product2.name}")

print("\nACCESS CLASS VARIABLES:")
print(f"Product.store_name: {Product.store_name}")
print(f"Product.tax_rate: {Product.tax_rate}")

print("\nAccess class variable through instance (not recommended but works):")
print(f"product1.store_name: {product1.store_name}")
print(f"product1.tax_rate: {product1.tax_rate}")

print("\nAccess via __dict__:")
print(f"Instance __dict__: {product1.__dict__}")
print(f"Class __dict__ (partial): {list(Product.__dict__.keys())}")


# ===== 5. MODIFYING VARIABLES =====
print("\n" + "=" * 70)
print("5. MODIFYING INSTANCE AND CLASS VARIABLES")
print("=" * 70 + "\n")


class BankAccount:
    """Bank account class"""
    
    # Class variable
    bank_name = "MyBank"
    interest_rate = 0.05
    total_accounts = 0
    
    def __init__(self, account_holder, balance):
        # Instance variables
        self.account_holder = account_holder
        self.balance = balance
        BankAccount.total_accounts += 1
    
    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")
        print(f"Bank: {self.bank_name}")
        print(f"Interest Rate: {self.interest_rate * 100}%")


# Create accounts
account1 = BankAccount("Alice", 5000)
account2 = BankAccount("Bob", 10000)

print("Original accounts:")
print(f"Account 1 - {account1.account_holder}, Balance: ${account1.balance}")
print(f"Account 2 - {account2.account_holder}, Balance: ${account2.balance}")
print(f"Total accounts: {BankAccount.total_accounts}")

print("\nModify instance variable:")
account1.balance = 7500
print(f"Account 1 balance after modification: ${account1.balance}")
print(f"Account 2 balance (unchanged): ${account2.balance}")

print("\nModify class variable:")
BankAccount.interest_rate = 0.07
print(f"New interest rate: {BankAccount.interest_rate * 100}%")
print(f"Both accounts see the new rate:")
account1.display()
print()
account2.display()


# ===== 6. IMPORTANT: INSTANCE VARIABLE SHADOWING =====
print("\n" + "=" * 70)
print("6. INSTANCE VARIABLE SHADOWING (IMPORTANT!)")
print("=" * 70 + "\n")
print("If you create an instance variable with same name as class variable,")
print("it shadows the class variable for that instance\n")


class Counter:
    """Counter class demonstrating shadowing"""
    
    # Class variable
    count = 0
    
    def __init__(self, name):
        self.name = name
        Counter.count += 1


c1 = Counter("Counter1")
c2 = Counter("Counter2")

print(f"Class variable 'count': {Counter.count}")
print(f"c1.count: {c1.count}")
print(f"c2.count: {c2.count}")

print("\nNow create instance variable 'count' for c1:")
c1.count = 100  # This creates an instance variable, doesn't modify class variable!

print(f"\nAfter c1.count = 100:")
print(f"Class variable 'count': {Counter.count}")
print(f"c1.count (instance variable): {c1.count}")
print(f"c2.count (class variable): {c2.count}")

print("\nThis shows c1 has its own 'count' variable:")
print(f"'count' in c1.__dict__: {'count' in c1.__dict__}")
print(f"'count' in c2.__dict__: {'count' in c2.__dict__}")
print(f"'count' in Counter.__dict__: {'count' in Counter.__dict__}")


# ===== 7. MODIFYING CLASS VARIABLES FROM INSTANCE =====
print("\n" + "=" * 70)
print("7. MODIFYING CLASS VARIABLES (correct way)")
print("=" * 70 + "\n")


class Player:
    """Player class"""
    
    # Class variable
    total_players = 0
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
        # Correct way to modify class variable
        Player.total_players += 1
    
    @staticmethod
    def get_total_players():
        return Player.total_players


p1 = Player("Alice", 100)
p2 = Player("Bob", 150)
p3 = Player("Charlie", 120)

print(f"Total players: {Player.get_total_players()}")

print("\nDON'T DO THIS (creates instance variable, doesn't modify class variable):")
p1.total_players = 999
print(f"After p1.total_players = 999:")
print(f"Class variable: {Player.total_players}")
print(f"Instance variable p1.total_players: {p1.total_players}")

print("\nDO THIS (modifies class variable):")
Player.total_players = 5
print(f"After Player.total_players = 5:")
print(f"Player.total_players: {Player.total_players}")
print(f"p1.total_players: {p1.total_players}")  # Sees class variable
print(f"p2.total_players: {p2.total_players}")  # Sees class variable


# ===== 8. MUTABLE CLASS VARIABLES (CAUTION!) =====
print("\n" + "=" * 70)
print("8. MUTABLE CLASS VARIABLES (CAUTION!)")
print("=" * 70 + "\n")


class Team:
    """Team class with mutable class variable"""
    
    # Mutable class variable (LIST)
    members = []
    
    def __init__(self, name):
        self.name = name
    
    def add_member(self, member_name):
        Team.members.append(member_name)
    
    def display_members(self):
        print(f"Team: {self.name}, Members: {Team.members}")


team1 = Team("Team A")
team2 = Team("Team B")

print("Adding members to team1:")
team1.add_member("Alice")
team1.add_member("Bob")
team1.display_members()

print("\nAdding members to team2:")
team2.add_member("Charlie")
team2.add_member("Diana")
team2.display_members()

print("\nPROBLEM: Both teams share the same list!")
print(f"team1 members: {Team.members}")
print(f"team2 members: {Team.members}")

print("\nSOLUTION: Initialize list in __init__ (as instance variable):\n")


class TeamFixed:
    """Team class with proper instance list"""
    
    def __init__(self, name):
        self.name = name
        self.members = []  # Instance variable, not class variable
    
    def add_member(self, member_name):
        self.members.append(member_name)
    
    def display_members(self):
        print(f"Team: {self.name}, Members: {self.members}")


team3 = TeamFixed("Team C")
team4 = TeamFixed("Team D")

team3.add_member("Alice")
team3.add_member("Bob")
team3.display_members()

team4.add_member("Charlie")
team4.display_members()

print("Now each team has its own member list!")


# ===== 9. PRACTICAL EXAMPLE: LIBRARY SYSTEM =====
print("\n" + "=" * 70)
print("9. PRACTICAL EXAMPLE: LIBRARY SYSTEM")
print("=" * 70 + "\n")


class Book:
    """Book class with instance and class variables"""
    
    # Class variables
    library_name = "City Library"
    total_books = 0
    available_books = 0
    
    def __init__(self, title, author, isbn):
        # Instance variables
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.borrowed_by = None
        
        # Update class variables
        Book.total_books += 1
        Book.available_books += 1
    
    def borrow_book(self, member_name):
        """Borrow the book"""
        if self.is_available:
            self.is_available = False
            self.borrowed_by = member_name
            Book.available_books -= 1
            print(f"✓ {self.title} borrowed by {member_name}")
        else:
            print(f"✗ {self.title} is already borrowed by {self.borrowed_by}")
    
    def return_book(self):
        """Return the book"""
        if not self.is_available:
            print(f"✓ {self.title} returned by {self.borrowed_by}")
            self.is_available = True
            self.borrowed_by = None
            Book.available_books += 1
        else:
            print(f"✗ {self.title} is not borrowed")
    
    def display_status(self):
        status = "Available" if self.is_available else f"Borrowed by {self.borrowed_by}"
        print(f"{self.title} by {self.author} [{self.isbn}]: {status}")
    
    @classmethod
    def library_status(cls):
        print(f"\n{cls.library_name} Status:")
        print(f"  Total books: {cls.total_books}")
        print(f"  Available: {cls.available_books}")
        print(f"  Borrowed: {cls.total_books - cls.available_books}")


# Create books
book1 = Book("Python Basics", "John Smith", "ISBN001")
book2 = Book("Advanced Python", "Jane Doe", "ISBN002")
book3 = Book("Web Development", "Bob Johnson", "ISBN003")

Book.library_status()

print("\nBooks in library:")
book1.display_status()
book2.display_status()
book3.display_status()

print("\nBorrowing books:")
book1.borrow_book("Alice")
book2.borrow_book("Bob")

Book.library_status()

print("\nBook status after borrowing:")
book1.display_status()
book2.display_status()
book3.display_status()

print("\nReturning book:")
book1.return_book()

Book.library_status()


# ===== 10. SUMMARY TABLE =====
print("\n" + "=" * 70)
print("SUMMARY: INSTANCE vs CLASS VARIABLES")
print("=" * 70)
print("""
╔══════════════════╦═════════════════════╦═════════════════════╗
║   Aspect         ║  Instance Variable  ║  Class Variable     ║
╠══════════════════╬═════════════════════╬═════════════════════╣
║ Definition       ║ Inside __init__     ║ Inside class body   ║
║                  ║ with self.name      ║ name = value        ║
╠══════════════════╬═════════════════════╬═════════════════════╣
║ Scope            ║ Each object has its ║ Shared by all       ║
║                  ║ own copy            ║ instances           ║
╠══════════════════╬═════════════════════╬═════════════════════╣
║ Access           ║ self.name           ║ ClassName.name      ║
║                  ║ object.name         ║ self.name           ║
╠══════════════════╬═════════════════════╬═════════════════════╣
║ Modification     ║ Changes one object  ║ Changes all objects ║
║                  ║ only                ║ (unless shadowed)   ║
╠══════════════════╬═════════════════════╬═════════════════════╣
║ Memory           ║ Stored separately   ║ Stored once in      ║
║                  ║ for each instance   ║ class               ║
╠══════════════════╬═════════════════════╬═════════════════════╣
║ Use Case         ║ Object-specific     ║ Shared properties,  ║
║                  ║ data (age, salary)  ║ counters, constants ║
╚══════════════════╩═════════════════════╩═════════════════════╝

KEY POINTS:
✓ Instance variables unique to each object (self.name)
✓ Class variables shared by all objects (ClassName.name)
✓ Modifying instance variable doesn't affect other objects
✓ Modifying class variable affects all objects
✓ Be careful with mutable class variables (lists, dicts)
✓ Instance variable with same name shadows class variable
✓ Use ClassName.variable to modify class variables
✓ Use self.variable to access/modify instance variables
""")

print("\n" + "=" * 70)
print("✓ INSTANCE AND CLASS VARIABLES TUTORIAL COMPLETED!")
print("=" * 70)
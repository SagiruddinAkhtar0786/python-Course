# =============================================================================
# MAGIC METHODS (DUNDER METHODS) IN PYTHON
# =============================================================================
# Magic methods are special methods that start and end with double underscores
# They allow customization of how objects interact with Python operators
# and built-in functions

print("=" * 70)
print("MAGIC METHODS (DUNDER METHODS) IN PYTHON")
print("=" * 70)

# ===== 1. INTRODUCTION TO MAGIC METHODS =====
print("\n1. INTRODUCTION TO MAGIC METHODS")
print("=" * 70 + "\n")

print("""
Magic methods (dunder methods):
• Start and end with double underscores: __method__
• Called automatically by Python
• Allow customization of object behavior
• Make objects work with operators and built-in functions

Examples:
• __init__ - Constructor
• __str__ - String representation
• __add__ - Addition operator (+)
• __len__ - Length function
• __getitem__ - Indexing operator []
""")


# ===== 2. __init__ AND __del__ =====
print("\n2. __init__ AND __del__ (CONSTRUCTOR AND DESTRUCTOR)")
print("=" * 70 + "\n")


class Car:
    """Car class with __init__ and __del__"""
    
    def __init__(self, brand, model):
        """Constructor - called when object is created"""
        self.brand = brand
        self.model = model
        print(f"✓ Car created: {self.brand} {self.model}")
    
    def __del__(self):
        """Destructor - called when object is deleted"""
        print(f"✗ Car deleted: {self.brand} {self.model}")


print("Creating car:")
car1 = Car("Toyota", "Camry")

print("\nDeleting car:")
del car1


# ===== 3. __str__ AND __repr__ =====
print("\n3. __str__ AND __repr__ (STRING REPRESENTATIONS)")
print("=" * 70 + "\n")


class Person:
    """Person class with string representations"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """Informal string - used by print() and str()"""
        return f"{self.name} is {self.age} years old"
    
    def __repr__(self):
        """Official string - used by repr() and debugging"""
        return f"Person('{self.name}', {self.age})"


person = Person("Alice", 25)

print(f"str(): {str(person)}")  # Calls __str__
print(f"repr(): {repr(person)}")  # Calls __repr__
print(f"print(): {person}")  # Calls __str__


# ===== 4. __len__ AND __bool__ =====
print("\n4. __len__ AND __bool__ (LENGTH AND BOOLEAN)")
print("=" * 70 + "\n")


class ShoppingCart:
    """Shopping cart with length and boolean checks"""
    
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def __len__(self):
        """Return number of items in cart"""
        return len(self.items)
    
    def __bool__(self):
        """Return True if cart is not empty"""
        return len(self.items) > 0
    
    def __str__(self):
        return f"Cart with {len(self)} items"


cart = ShoppingCart()
print(f"Empty cart: {len(cart)} items")
print(f"Is empty? {bool(cart)}")
print(f"Display: {cart}")

cart.add_item("Laptop")
cart.add_item("Mouse")
cart.add_item("Keyboard")

print(f"\nFull cart: {len(cart)} items")
print(f"Is empty? {bool(cart)}")
print(f"Display: {cart}")

print(f"\nUsing in if statement:")
if cart:
    print("Cart has items")
else:
    print("Cart is empty")


# ===== 5. __eq__, __lt__, __gt__ (COMPARISON OPERATORS) =====
print("\n5. COMPARISON OPERATORS (__eq__, __lt__, __gt__, etc.)")
print("=" * 70 + "\n")


class Book:
    """Book class with comparison operators"""
    
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} ({self.pages} pages)"
    
    def __eq__(self, other):
        """Equal to (==)"""
        return self.pages == other.pages
    
    def __lt__(self, other):
        """Less than (<)"""
        return self.pages < other.pages
    
    def __gt__(self, other):
        """Greater than (>)"""
        return self.pages > other.pages
    
    def __le__(self, other):
        """Less than or equal (<=)"""
        return self.pages <= other.pages
    
    def __ge__(self, other):
        """Greater than or equal (>=)"""
        return self.pages >= other.pages
    
    def __ne__(self, other):
        """Not equal (!=)"""
        return self.pages != other.pages


book1 = Book("Python Guide", 300)
book2 = Book("Java Basics", 250)
book3 = Book("Advanced Python", 300)

print(f"book1: {book1}")
print(f"book2: {book2}")
print(f"book3: {book3}")

print(f"\nComparisons:")
print(f"book1 == book3: {book1 == book3}")
print(f"book1 != book2: {book1 != book2}")
print(f"book1 > book2: {book1 > book2}")
print(f"book1 < book2: {book1 < book2}")
print(f"book1 >= book3: {book1 >= book3}")


# ===== 6. ARITHMETIC OPERATORS (__add__, __sub__, __mul__, etc.) =====
print("\n6. ARITHMETIC OPERATORS (__add__, __sub__, __mul__)")
print("=" * 70 + "\n")


class Vector:
    """Vector class with arithmetic operations"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        """Addition: v1 + v2"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Subtraction: v1 - v2"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Multiplication: v * 2"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        """Reverse multiplication: 2 * v"""
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        """Division: v / 2"""
        return Vector(self.x / scalar, self.y / scalar)


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1: {v1}")
print(f"v2: {v2}")

print(f"\nv1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"3 * v2 = {3 * v2}")
print(f"v1 / 2 = {v1 / 2}")


# ===== 7. __getitem__, __setitem__, __delitem__ (INDEXING) =====
print("\n7. INDEXING (__getitem__, __setitem__, __delitem__)")
print("=" * 70 + "\n")


class Playlist:
    """Playlist class with indexing support"""
    
    def __init__(self):
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
    
    def __getitem__(self, index):
        """Get item by index: playlist[0]"""
        return self.songs[index]
    
    def __setitem__(self, index, value):
        """Set item by index: playlist[0] = 'new_song'"""
        self.songs[index] = value
    
    def __delitem__(self, index):
        """Delete item by index: del playlist[0]"""
        del self.songs[index]
    
    def __len__(self):
        return len(self.songs)
    
    def __str__(self):
        return f"Playlist: {', '.join(self.songs)}"


playlist = Playlist()
playlist.add_song("Song A")
playlist.add_song("Song B")
playlist.add_song("Song C")

print(f"Playlist: {playlist}")
print(f"First song: {playlist[0]}")
print(f"Second song: {playlist[1]}")

print("\nChanging second song:")
playlist[1] = "Song X"
print(f"Playlist: {playlist}")

print("\nDeleting first song:")
del playlist[0]
print(f"Playlist: {playlist}")


# ===== 8. __call__ (MAKING OBJECTS CALLABLE) =====
print("\n8. __call__ (MAKING OBJECTS CALLABLE)")
print("=" * 70 + "\n")


class Multiplier:
    """Class that can be called like a function"""
    
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        """Make object callable"""
        return x * self.factor


# Create callable objects
double = Multiplier(2)
triple = Multiplier(3)

print(f"double(5) = {double(5)}")
print(f"double(10) = {double(10)}")
print(f"triple(4) = {triple(4)}")
print(f"triple(7) = {triple(7)}")


class Greeter:
    """Greeter object that is callable"""
    
    def __init__(self, greeting):
        self.greeting = greeting
    
    def __call__(self, name):
        return f"{self.greeting}, {name}!"


hello = Greeter("Hello")
hi = Greeter("Hi")

print(f"\n{hello('Alice')}")
print(f"{hi('Bob')}")


# ===== 9. __contains__ (IN OPERATOR) =====
print("\n9. __contains__ (IN OPERATOR)")
print("=" * 70 + "\n")


class Library:
    """Library class with membership checking"""
    
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def __contains__(self, book):
        """Check if book is in library: book in library"""
        return book in self.books
    
    def __str__(self):
        return f"Library with {len(self.books)} books: {self.books}"


library = Library()
library.add_book("Python 101")
library.add_book("Data Science")
library.add_book("Web Dev")

print(f"{library}")

print(f"\n'Python 101' in library: {'Python 101' in library}")
print(f"'Java' in library: {'Java' in library}")
print(f"'Web Dev' in library: {'Web Dev' in library}")


# ===== 10. __enter__ AND __exit__ (CONTEXT MANAGERS) =====
print("\n10. __enter__ AND __exit__ (CONTEXT MANAGERS)")
print("=" * 70 + "\n")


class FileHandler:
    """File handler with context manager support"""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Called when entering 'with' block"""
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block"""
        print(f"Closing file: {self.filename}")
        if self.file:
            self.file.close()


# Create a test file
with open("test.txt", "w") as f:
    f.write("Hello, World!")

# Use context manager
print("\nUsing context manager:")
with FileHandler("test.txt", "r") as f:
    content = f.read()
    print(f"File content: {content}")

print("File is now closed")


# ===== 11. __iter__ AND __next__ (ITERATORS) =====
print("\n11. __iter__ AND __next__ (ITERATORS)")
print("=" * 70 + "\n")


class CountUp:
    """Countdown iterator"""
    
    def __init__(self, max):
        self.max = max
        self.current = 0
    
    def __iter__(self):
        """Return iterator object"""
        return self
    
    def __next__(self):
        """Return next value"""
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration


print("Count up to 5:")
for num in CountUp(5):
    print(num, end=" ")

print("\n\nCount up to 3:")
for num in CountUp(3):
    print(num, end=" ")


class Fibonacci:
    """Fibonacci sequence iterator"""
    
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a < self.limit:
            value = self.a
            self.a, self.b = self.b, self.a + self.b
            return value
        else:
            raise StopIteration


print("\n\nFibonacci sequence up to 50:")
for num in Fibonacci(50):
    print(num, end=" ")


# ===== 12. __hash__ AND __eq__ (HASHABLE OBJECTS) =====
print("\n\n12. __hash__ AND __eq__ (HASHABLE OBJECTS)")
print("=" * 70 + "\n")


class Point:
    """Point class that can be used as dictionary key"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        """Make object hashable"""
        return hash((self.x, self.y))
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"


p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

# Use points as dictionary keys
locations = {
    p1: "Home",
    p3: "Office"
}

print(f"Point locations: {locations}")
print(f"p1 in locations: {p1 in locations}")
print(f"p2 in locations: {p2 in locations}")  # p2 equals p1
print(f"p3 in locations: {p3 in locations}")


# ===== 13. PRACTICAL EXAMPLE: MONEY CLASS =====
print("\n13. PRACTICAL EXAMPLE: MONEY CLASS")
print("=" * 70 + "\n")


class Money:
    """Money class with multiple magic methods"""
    
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency
    
    def __str__(self):
        return f"{self.amount}{self.currency}"
    
    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"
    
    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)
    
    def __sub__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot subtract different currencies")
        return Money(self.amount - other.amount, self.currency)
    
    def __mul__(self, num):
        return Money(self.amount * num, self.currency)
    
    def __truediv__(self, num):
        return Money(self.amount / num, self.currency)
    
    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency
    
    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot compare different currencies")
        return self.amount < other.amount
    
    def __le__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot compare different currencies")
        return self.amount <= other.amount
    
    def __gt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot compare different currencies")
        return self.amount > other.amount
    
    def __bool__(self):
        return self.amount > 0


m1 = Money(100)
m2 = Money(50)
m3 = Money(100)

print(f"m1: {m1}")
print(f"m2: {m2}")
print(f"m3: {m3}")

print(f"\nm1 + m2 = {m1 + m2}")
print(f"m1 - m2 = {m1 - m2}")
print(f"m1 * 2 = {m1 * 2}")
print(f"m1 / 2 = {m1 / 2}")

print(f"\nm1 == m3: {m1 == m3}")
print(f"m1 > m2: {m1 > m2}")
print(f"m1 < m2: {m1 < m2}")

print(f"\nbool(m1): {bool(m1)}")
print(f"bool(Money(0)): {bool(Money(0))}")


# ===== 14. SUMMARY TABLE =====
print("\n" + "=" * 70)
print("SUMMARY: COMMON MAGIC METHODS")
print("=" * 70)
print("""
╔═════════════════╦════════════════╦═════════════════════════════╗
║ Magic Method    ║ Operator/Call  ║ Purpose                     ║
╠═════════════════╬════════════════╬═════════════════════════════╣
║ __init__        ║ obj = Class()   ║ Constructor                 ║
║ __del__         ║ del obj        ║ Destructor                  ║
╠═════════════════╬════════════════╬═════════════════════════════╣
║ __str__         ║ str(obj)       ║ User-friendly string        ║
║ __repr__        ║ repr(obj)      ║ Official representation     ║
╠═════════════════╬════════════════╬═════════════════════════════╣
║ __len__         ║ len(obj)       ║ Length                      ║
║ __bool__        ║ if obj:        ║ Boolean value               ║
╠═════════════════╬════════════════╬═════════════════════════════╣
║ __eq__          ║ obj1 == obj2   ║ Equality                    ║
║ __lt__          ║ obj1 < obj2    ║ Less than                   ║
║ __gt__          ║ obj1 > obj2    ║ Greater than                ║
║ __le__          ║ obj1 <= obj2   ║ Less than or equal          ║
║ __ge__          ║ obj1 >= obj2   ║ Greater than or equal       ║
║ __ne__          ║ obj1 != obj2   ║ Not equal                   ║
╠═════════════════╬════════════════╬═════════════════════════════╣
║ __add__         ║ obj1 + obj2    ║ Addition                    ║
║ __sub__         ║ obj1 - obj2    ║ Subtraction                 ║
║ __mul__         ║ obj1 * num     ║ Multiplication              ║
║ __truediv__     ║ obj1 / num     ║ Division                    ║
║ __mod__         ║ obj1 % num     ║ Modulus                     ║
║ __pow__         ║ obj1 ** num    ║ Power                       ║
╠═════════════════╬════════════════╬═════════════════════════════╣
║ __getitem__     ║ obj[index]     ║ Get by index                ║
║ __setitem__     ║ obj[i] = val   ║ Set by index                ║
║ __delitem__     ║ del obj[index] ║ Delete by index             ║
╠═════════════════╬════════════════╬═════════════════════════════╣
║ __call__        ║ obj(args)      ║ Call like function          ║
║ __contains__    ║ item in obj    ║ Membership test             ║
╠═════════════════╬════════════════╬═════════════════════════════╣
║ __iter__        ║ for x in obj:  ║ Iterator protocol           ║
║ __next__        ║ next(obj)      ║ Get next item               ║
╠═════════════════╬════════════════╬═════════════════════════════╣
║ __enter__       ║ with obj:      ║ Context manager entry       ║
║ __exit__        ║ (context end)  ║ Context manager exit        ║
╠═════════════════╬════════════════╬═════════════════════════════╣
║ __hash__        ║ hash(obj)      ║ Hash value (for dicts/sets) ║
╚═════════════════╩════════════════╩═════════════════════════════╝

KEY BENEFITS:
✓ Make objects behave like built-in types
✓ Enable operator overloading
✓ Support Pythonic syntax
✓ Cleaner, more intuitive code
✓ Full integration with Python ecosystem
""")

print("\n" + "=" * 70)
print("✓ MAGIC METHODS TUTORIAL COMPLETED!")
print("=" * 70)

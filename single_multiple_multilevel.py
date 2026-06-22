# =============================================================================
# SINGLE, MULTIPLE, AND MULTILEVEL INHERITANCE IN PYTHON
# =============================================================================
# Single Inheritance: Child inherits from one parent
# Multiple Inheritance: Child inherits from multiple parents
# Multilevel Inheritance: Chain of inheritance (grandparent -> parent -> child)

print("=" * 70)
print("SINGLE, MULTIPLE, AND MULTILEVEL INHERITANCE")
print("=" * 70)

# ===== 1. SINGLE INHERITANCE =====
print("\n1. SINGLE INHERITANCE")
print("=" * 70 + "\n")

print("""
SINGLE INHERITANCE:
• One child class inherits from one parent class
• Simplest form of inheritance
• Most common in real applications
""")


class Animal:
    """Parent class"""
    
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    """Child class inheriting from Animal"""
    
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")


# Create and use
dog = Dog("Buddy")
print(f"Name: {dog.name}")
dog.eat()
dog.sleep()
dog.bark()


# ===== 2. SINGLE INHERITANCE WITH METHOD OVERRIDING =====
print("\n2. SINGLE INHERITANCE WITH OVERRIDING")
print("=" * 70 + "\n")


class Vehicle:
    """Parent class"""
    
    def start(self):
        print("Vehicle starting...")
    
    def stop(self):
        print("Vehicle stopping...")


class Car(Vehicle):
    """Child class overriding parent method"""
    
    def start(self):
        print("Car engine starting with key...")
    
    def stop(self):
        print("Car engine stopping...")
    
    def open_trunk(self):
        print("Trunk opened!")


car = Car()
car.start()
car.stop()
car.open_trunk()


# ===== 3. MULTIPLE INHERITANCE =====
print("\n3. MULTIPLE INHERITANCE")
print("=" * 70 + "\n")

print("""
MULTIPLE INHERITANCE:
• Child class inherits from two or more parent classes
• Inherits attributes and methods from all parents
• Can lead to complexity (Diamond Problem)
• Use with caution
""")


class Animal_:
    """First parent class"""
    
    def eat(self):
        print("Eating...")
    
    def sleep(self):
        print("Sleeping...")


class Flyer:
    """Second parent class"""
    
    def fly(self):
        print("Flying in the sky...")


class Bird(Animal_, Flyer):
    """Child class inheriting from two parents"""
    
    def chirp(self):
        print("Chirp! Chirp!")


# Create and use
bird = Bird()
print("Bird capabilities:")
bird.eat()      # From Animal_
bird.sleep()    # From Animal_
bird.fly()      # From Flyer
bird.chirp()    # Own method


# ===== 4. MULTIPLE INHERITANCE - PRACTICAL EXAMPLE =====
print("\n4. MULTIPLE INHERITANCE - PRACTICAL EXAMPLE")
print("=" * 70 + "\n")


class Employee:
    """Employee class"""
    
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    
    def work(self):
        print(f"{self.name} is working")
    
    def get_salary(self):
        print(f"Employee {self.name} salary information")


class Developer:
    """Developer class"""
    
    def __init__(self, language):
        self.language = language
    
    def code(self):
        print(f"Coding in {self.language}")
    
    def debug(self):
        print("Debugging code...")


class SoftwareDeveloper(Employee, Developer):
    """Inherits from both Employee and Developer"""
    
    def __init__(self, name, employee_id, language):
        Employee.__init__(self, name, employee_id)
        Developer.__init__(self, language)
    
    def full_task(self):
        print(f"{self.name} is doing full development task")


dev = SoftwareDeveloper("Alice", 101, "Python")
print(f"Name: {dev.name}")
print(f"ID: {dev.employee_id}")
print(f"Language: {dev.language}")
dev.work()
dev.code()
dev.debug()
dev.full_task()


# ===== 5. MULTIPLE INHERITANCE - METHOD RESOLUTION ORDER (MRO) =====
print("\n5. MULTIPLE INHERITANCE - MRO (METHOD RESOLUTION ORDER)")
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


print("MRO for class D (B, C):")
print(D.__mro__)
print()

d = D()
d.method()  # Will use B's method (left to right)

print("\n" + "=" * 50)

class E(C, B):
    pass


print("MRO for class E (C, B):")
print(E.__mro__)

e = E()
e.method()  # Will use C's method


# ===== 6. MULTILEVEL INHERITANCE =====
print("\n6. MULTILEVEL INHERITANCE")
print("=" * 70 + "\n")

print("""
MULTILEVEL INHERITANCE:
• Grandparent -> Parent -> Child chain
• Child inherits from Parent, Parent inherits from Grandparent
• Can have multiple levels
""")


class LivingBeing:
    """Grandparent class"""
    
    def __init__(self, name):
        self.name = name
    
    def breathe(self):
        print(f"{self.name} is breathing")


class Mammal(LivingBeing):
    """Parent class inheriting from Grandparent"""
    
    def produce_milk(self):
        print(f"{self.name} produces milk")


class Human(Mammal):
    """Child class inheriting from Parent"""
    
    def speak(self):
        print(f"{self.name} is speaking")


# Create and use
human = Human("John")
print(f"Name: {human.name}")
human.breathe()        # From LivingBeing
human.produce_milk()   # From Mammal
human.speak()          # From Human


# ===== 7. MULTILEVEL INHERITANCE - EXTENDED EXAMPLE =====
print("\n7. MULTILEVEL INHERITANCE - EXTENDED")
print("=" * 70 + "\n")


class Vehicle_:
    """Level 1: Grandparent"""
    
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print("Vehicle starting...")


class Car_(Vehicle_):
    """Level 2: Parent"""
    
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def accelerate(self):
        print("Car accelerating...")


class SportsCar(Car_):
    """Level 3: Child"""
    
    def __init__(self, brand, model, top_speed):
        super().__init__(brand, model)
        self.top_speed = top_speed
    
    def nitro_boost(self):
        print(f"Nitro boost activated! Top speed: {self.top_speed} mph")


# Create and use
sports = SportsCar("Ferrari", "F8", 211)
print(f"Brand: {sports.brand}")
print(f"Model: {sports.model}")
print(f"Top Speed: {sports.top_speed}")
sports.start()
sports.accelerate()
sports.nitro_boost()


# ===== 8. MULTILEVEL INHERITANCE - METHOD OVERRIDING =====
print("\n8. MULTILEVEL INHERITANCE - OVERRIDING")
print("=" * 70 + "\n")


class Shape:
    """Level 1: Grandparent"""
    
    def area(self):
        return 0


class Polygon(Shape):
    """Level 2: Parent"""
    
    def area(self):
        print("Calculating polygon area...")
        return 0


class Triangle(Polygon):
    """Level 3: Child"""
    
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        print(f"Calculating triangle area: base={self.base}, height={self.height}")
        return 0.5 * self.base * self.height


triangle = Triangle(10, 5)
print(f"Triangle area: {triangle.area()}")


# ===== 9. HYBRID INHERITANCE =====
print("\n9. HYBRID INHERITANCE (COMBINATION)")
print("=" * 70 + "\n")

print("""
HYBRID INHERITANCE:
• Combination of single, multiple, and multilevel inheritance
• Most complex form
• Can cause diamond problem
""")


class Being:
    """Grandparent"""
    
    def exist(self):
        print("I exist")


class Living(Being):
    """Parent 1"""
    
    def live(self):
        print("I'm alive")


class Working(Being):
    """Parent 2"""
    
    def work(self):
        print("I'm working")


class Person(Living, Working):
    """Child inheriting from two parents"""
    
    def speak(self):
        print("I speak")


person = Person()
person.exist()   # From Being
person.live()    # From Living
person.work()    # From Working
person.speak()   # From Person


# ===== 10. COMPARISON TABLE =====
print("\n" + "=" * 70)
print("INHERITANCE TYPES COMPARISON")
print("=" * 70)
print("""
╔═══════════════════╦══════════════╦════════════════════════════╗
║ Inheritance Type  ║ Structure    ║ Example                    ║
╠═══════════════════╬══════════════╬════════════════════════════╣
║ SINGLE            ║ Parent       ║ class Dog(Animal):         ║
║                   ║    |         ║                            ║
║                   ║  Child       ║                            ║
╠═══════════════════╬══════════════╬════════════════════════════╣
║ MULTIPLE          ║ Parent1      ║ class Bird(Animal, Flyer): ║
║                   ║    \  /      ║                            ║
║                   ║    Child     ║                            ║
║                   ║    /  \      ║                            ║
║                   ║ Parent2      ║                            ║
╠═══════════════════╬══════════════╬════════════════════════════╣
║ MULTILEVEL        ║ Grandparent  ║ class Human(Mammal):       ║
║                   ║    |         ║ class Mammal(LivingBeing): ║
║                   ║   Parent     ║                            ║
║                   ║    |         ║                            ║
║                   ║   Child      ║                            ║
╠═══════════════════╬══════════════╬════════════════════════════╣
║ HYBRID            ║ Multiple +   ║ Multiple + Multilevel      ║
║                   ║ Multilevel   ║ combination                ║
╚═══════════════════╩══════════════╩════════════════════════════╝

KEY POINTS:
✓ Single: Easy to understand and maintain
✓ Multiple: Flexible but can be complex
✓ Multilevel: Good for hierarchical relationships
✓ Hybrid: Combines multiple inheritance types

PROBLEMS TO WATCH FOR:
✗ Diamond Problem: Same method in multiple inheritance paths
✗ Complexity: Too many inheritance levels
✗ Tight Coupling: Difficult to modify parent classes
✗ MRO Issues: Method resolution can be confusing

BEST PRACTICES:
✓ Use composition when inheritance becomes complex
✓ Prefer single inheritance when possible
✓ Use super() to call parent methods
✓ Keep inheritance hierarchies shallow
✓ Document inheritance relationships clearly
""")


# ===== 11. PRACTICAL EXAMPLE: UNIVERSITY SYSTEM =====
print("\n11. PRACTICAL EXAMPLE: UNIVERSITY SYSTEM")
print("=" * 70 + "\n")


class Person_:
    """Grandparent: Level 1"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class UniversityMember(Person_):
    """Parent: Level 2 - Single Inheritance from Person"""
    
    def __init__(self, name, age, member_id):
        super().__init__(name, age)
        self.member_id = member_id
    
    def show_id(self):
        print(f"Member ID: {self.member_id}")


class Teacher(UniversityMember):
    """Child: Level 3 - Multilevel"""
    
    def __init__(self, name, age, member_id, subject):
        super().__init__(name, age, member_id)
        self.subject = subject
    
    def teach(self):
        print(f"{self.name} is teaching {self.subject}")


class Student(UniversityMember):
    """Child: Level 3 - Multilevel"""
    
    def __init__(self, name, age, member_id, major):
        super().__init__(name, age, member_id)
        self.major = major
    
    def study(self):
        print(f"{self.name} is studying {self.major}")


# Another branch - Research
class Researcher:
    """Different hierarchy"""
    
    def research(self):
        print(f"{self.name} is conducting research")


class TeachingAssistant(Student, Researcher):
    """Multiple Inheritance: Student + Researcher"""
    
    def __init__(self, name, age, member_id, major):
        Student.__init__(self, name, age, member_id, major)
    
    def conduct_labs(self):
        print(f"{self.name} is conducting lab sessions")


# Create instances
teacher = Teacher("Dr. Smith", 45, "T101", "Mathematics")
teacher.display_info()
teacher.show_id()
teacher.teach()

print()

student = Student("John", 20, "S101", "Computer Science")
student.display_info()
student.show_id()
student.study()

print()

ta = TeachingAssistant("Emma", 22, "TA101", "Computer Science")
ta.display_info()
ta.show_id()
ta.study()
ta.research()
ta.conduct_labs()


print("\n" + "=" * 70)
print("✓ INHERITANCE TYPES TUTORIAL COMPLETED!")
print("=" * 70)

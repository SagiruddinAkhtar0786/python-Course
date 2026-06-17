# =============================================================================
# DOCSTRINGS IN PYTHON
# =============================================================================
# Docstrings are documentation strings that describe what a function/class does
# They are enclosed in triple quotes (''' ''' or """ """)
# Docstrings are different from comments - they're accessible via __doc__

print("=" * 60)
print("DOCSTRINGS IN PYTHON")
print("=" * 60)

# ===== 1. BASIC DOCSTRING =====
print("\n1. BASIC DOCSTRING\n")

def square(number):
    """Returns the square of a number."""
    return number * number

result = square(7)
print(f"The square of 7 is: {result}")
print(f"Docstring: {square.__doc__}")


# ===== 2. ACCESSING DOCSTRINGS =====
print("\n" + "=" * 60)
print("2. ACCESSING AND USING DOCSTRINGS")
print("=" * 60 + "\n")

print(f"square.__doc__ attribute: {square.__doc__}")


# ===== 3. MULTI-LINE DOCSTRING =====
print("\n" + "=" * 60)
print("3. MULTI-LINE DOCSTRING")
print("=" * 60 + "\n")

def calculate_area(radius):
    """
    Calculate the area of a circle.
    
    Parameters:
        radius (float): The radius of the circle
        
    Returns:
        float: The area of the circle (pi * r^2)
        
    Example:
        >>> calculate_area(5)
        78.5
    """
    pi = 3.14159
    area = pi * radius ** 2
    return area

print(f"calculate_area(5) = {calculate_area(5):.2f}")
print(f"\nMulti-line docstring:\n{calculate_area.__doc__}")


# ===== 4. CLASS DOCSTRING =====
print("\n" + "=" * 60)
print("4. CLASS DOCSTRING")
print("=" * 60 + "\n")

class Student:
    """
    A class to represent a student.
    
    Attributes:
        name (str): Student's name
        age (int): Student's age
        grade (str): Student's grade
    """
    
    def __init__(self, name, age, grade):
        """Initialize a Student object."""
        self.name = name
        self.age = age
        self.grade = grade
    
    def display(self):
        """Display student information."""
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
    
    def promote(self):
        """Promote student to next grade."""
        grades = ['A', 'B', 'C', 'D']
        if self.grade in grades:
            idx = grades.index(self.grade)
            self.grade = grades[max(0, idx - 1)]
            print(f"Promoted to grade {self.grade}")

# Create and use student
student = Student("Ali", 20, "B")
student.display()
print(f"\nClass Docstring:\n{Student.__doc__}")


# ===== 5. USING help() FUNCTION =====
print("\n" + "=" * 60)
print("5. USING help() FUNCTION")
print("=" * 60 + "\n")

print("help(square) output:")
help(square)


# ===== 6. DOCSTRING CONVENTIONS (PEP 257) =====
print("\n" + "=" * 60)
print("6. DOCSTRING CONVENTIONS (PEP 257)")
print("=" * 60 + "\n")

print("""
PEP 257 - Docstring Conventions:

1. ONE-LINE DOCSTRINGS:
   - Fit on one line
   - End with a period
   - Use imperative mood: "Calculate..." not "Calculates..."
   Example: \"\"\"Returns the square of a number.\"\"\"
   
2. MULTI-LINE DOCSTRINGS:
   - First line: summary (brief description)
   - Blank line
   - Detailed description
   - Args section
   - Returns section
   - Example section (optional)
   
3. FORMAT FOR FUNCTIONS:
   def function_name(param1, param2):
       \"\"\"
       Brief one-line description.
       
       Longer description explaining what the function does
       and how it should be used.
       
       Args:
           param1 (type): Description of param1
           param2 (type): Description of param2
           
       Returns:
           type: Description of return value
           
       Raises:
           ExceptionType: When this exception occurs
           
       Example:
           >>> function_name(1, 2)
           3
       \"\"\"
       
4. FORMAT FOR CLASSES:
   class ClassName:
       \"\"\"Brief description of the class.
       
       Attributes:
           attr1 (type): Description
           attr2 (type): Description
       \"\"\"
""")
def calculate_area(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area

def calculate_perimeter(radius):
    pi = 3.14159
    perimeter = 2 * pi * radius
    return perimeter    

r = int(input("Enter the radius of the circle: "))
area = calculate_area(r)
perimeter = calculate_perimeter(r)

print("Area of the circle with radius", r, "is:", area)
print("Perimeter of the circle with radius", r, "is:", perimeter)

def check_greater(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Both numbers are equal"
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))  
result = check_greater(num1, num2)
print("The greater number is:", result)

def average(*numbers): # touple of numbers
    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return avg

# Example usage:
print("Average of 1, 2, 3, 4, 5 is:", average(1, 2, 3, 4, 5))
print("Average of 10, 20, 30 is:", average(10, 20, 30))

# Dictionary example
student_grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
print("Alice's grade:", student_grades["Alice"])

def get_grade(name):
    return student_grades.get(name, "Student not found")

print("Alice's grade:", get_grade("Alice"))
print("David's grade:", get_grade("David")) 
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
        
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        
# Example usage
employee = Employee("John Doe", 50000)
manager = Manager("Jane Smith", 70000, "Engineering")

employee.display_info()
print()
manager.display_info()
print()
print(employee.name)  # Accessing public field
print(manager.department)  # Accessing public field
print()


class PrivateFields():
    def __init__(self, name, salary):
        self.__name = name  # Private field
        self.__salary = salary  # Private field

    def display_info(self):
        print(f"Name: {self.__name}, Salary: {self.__salary}")
        
print()
# Example usage of PrivateFields class  
privateFileds = PrivateFields("Alice Johnson", 60000)
#print(privateFileds.__name)  # This will raise an AttributeError
#below is name mangling to access private field
print("accessing private field: ",privateFileds._PrivateFields__name)  # Accessing private field using name mangling
privateFileds.display_info()
print()

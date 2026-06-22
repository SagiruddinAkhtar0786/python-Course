x = [1,2,3]
print(dir(x))
print(x.__getitem__(0))  # Accessing the first element using __getitem__
print(x[0])  # Accessing the first element using the standard indexing syntax

y = (3,2,1)
print(dir(y))
print(y.__getitem__(0))  # Accessing the first element using __getitem__
print(y[0])  # Accessing the first element using the standard indexing syntax

#__dict__ is a special method that returns a dictionary representation of an object's attributes.
class SampleClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value 

sample_object = SampleClass("Test", 123)
print(sample_object.__dict__)  # Output: {'name': 'Test', 'value':

#help() function is used to display the documentation of modules, classes, functions, and methods. It can also be used to get information about built-in functions and objects.
print(help(list))  # Display documentation for the list class
print(help(SampleClass))  # Display documentation for the SampleClass
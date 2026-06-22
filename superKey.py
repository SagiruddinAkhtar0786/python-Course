#super
class parentClass:
    def __init__(self):
        print("This is parent class constructor")

    def parentMethod(self):
        print("This is parent class method")
        
class childClass(parentClass):
    def __init__(self):
        super().__init__()  # Call the parent class constructor 
        
    def childMethod(self):
        print("This is child class method")
        super().parentMethod()  # Call the parent class method
        
        
# Example usage
child = childClass()    
child.childMethod()  # Call the child class method
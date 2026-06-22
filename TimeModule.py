import time

class TimeModule:
    @staticmethod
    def get_current_time():
        return time.time()  
    
    @staticmethod
    def format_time(timestamp):
        return time.ctime(timestamp)    

TimeModule.get_current_time()
TimeModule.format_time(TimeModule.get_current_time())
# ===== 3. LOCAL VS GLOBAL VARIABLES =====
print("\n" + "=" * 60)  
print("3. LOCAL VS GLOBAL VARIABLES")
print("=" * 60 + "\n")
global_var = "I am a global variable"  # This is a global variable  
def demonstrate_scope():
    local_var = "I am a local variable"  # This is a local variable
    print(f"Inside function: {local_var}")  # Accessing local variable
    print(f"Inside function: {global_var}")  # Accessing global variable
    
print("Calling demonstrate_scope():")
demonstrate_scope()
# Try to access local variable outside function (will raise an error)
try:
    print(local_var)  # This will raise a NameError
    
except NameError:
    print("ERROR: local_var is not accessible outside the function")
    

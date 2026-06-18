# =============================================================================
# ACCESS MODIFIERS IN PYTHON
# =============================================================================
# Access modifiers control the visibility and accessibility of class members
# Python has three levels: Public, Protected, and Private

print("=" * 60)
print("ACCESS MODIFIERS IN PYTHON")
print("=" * 60)

# ===== 1. PUBLIC MEMBERS (No underscore) =====
print("\n1. PUBLIC MEMBERS")
print("=" * 60 + "\n")


class BankAccount:
    """Bank account with public members"""
    
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public
        self.balance = balance  # Public
    
    def display(self):
        print(f"Account: {self.account_number}, Balance: ${self.balance}")


# Public members can be accessed and modified from anywhere
account = BankAccount("123456", 1000)
print(f"Account Number: {account.account_number}")
print(f"Balance: {account.balance}")

# Can be modified directly
account.balance = 500
print(f"Updated Balance: {account.balance}")

# Can be modified to any value (no validation!)
account.balance = -99999  # This shouldn't be allowed but it is!
print(f"Balance after invalid change: {account.balance}")


# ===== 2. PROTECTED MEMBERS (Single underscore) =====
print("\n2. PROTECTED MEMBERS (Single Underscore)")
print("=" * 60 + "\n")


class Car:
    """Car class with protected members"""
    
    def __init__(self, make, model, mileage):
        self.make = make  # Public
        self.model = model  # Public
        self._mileage = mileage  # Protected (convention: internal use)
        self._service_history = []  # Protected
    
    def get_mileage(self):
        """Public method to access protected member"""
        return self._mileage
    
    def add_service(self, service):
        """Public method to modify protected member"""
        self._service_history.append(service)
    
    def show_service_history(self):
        print(f"Service History for {self.make} {self.model}:")
        for service in self._service_history:
            print(f"  - {service}")


car = Car("Toyota", "Camry", 50000)
print(f"Make: {car.make}")
print(f"Model: {car.model}")
print(f"Mileage: {car.get_mileage()}")

car.add_service("Oil change")
car.add_service("Tire rotation")
car.show_service_history()

print("\nAccessing protected member directly (not recommended):")
print(f"_mileage: {car._mileage}")  # Works but signals "don't use this directly"

print("Modifying protected member directly (bad practice):")
car._mileage = -100  # Possible but not recommended
print(f"After modification: {car._mileage}")


# ===== 3. PRIVATE MEMBERS (Double underscore - Name Mangling) =====
print("\n3. PRIVATE MEMBERS (Double Underscore)")
print("=" * 60 + "\n")


class BankAccount_Secure:
    """Bank account with private members using name mangling"""
    
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number  # Public
        self.__pin = pin  # Private (name mangled)
        self.__balance = balance  # Private (name mangled)
    
    def verify_pin(self, entered_pin):
        """Public method to verify PIN"""
        return self.__pin == entered_pin
    
    def get_balance(self, pin):
        """Public method to get balance (requires PIN)"""
        if self.verify_pin(pin):
            return self.__balance
        else:
            print("Invalid PIN!")
            return None
    
    def withdraw(self, pin, amount):
        """Public method to withdraw money"""
        if not self.verify_pin(pin):
            print("Invalid PIN!")
            return False
        
        if amount > self.__balance:
            print("Insufficient balance!")
            return False
        
        self.__balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        return True


account_secure = BankAccount_Secure("987654", "1234", 5000)
print(f"Account Number: {account_secure.account_number}")

# Access private members through public methods
print(f"Balance (with PIN): ${account_secure.get_balance('1234')}")
print(f"Balance (wrong PIN): {account_secure.get_balance('9999')}")

# Withdraw money
account_secure.withdraw("1234", 500)

# Try to access private members directly
print("\nTrying to access private members directly:")
try:
    print(f"__pin: {account_secure.__pin}")
except AttributeError as e:
    print(f"Error: {e}")

print("\nPrivate members use name mangling:")
print(f"Actual attribute name: {dir(account_secure)}")

# You can still access via mangled name (but shouldn't!)
print(f"Via mangled name (BAD!): {account_secure._BankAccount_Secure__pin}")


# ===== 4. PROTECTED vs PRIVATE =====
print("\n4. PROTECTED vs PRIVATE COMPARISON")
print("=" * 60 + "\n")


class Vehicle:
    """Demonstrates protected members"""
    
    def __init__(self, speed):
        self._speed = speed  # Protected
    
    def accelerate(self, amount):
        self._speed += amount
        print(f"Speed: {self._speed}")


class Car_Advanced(Vehicle):
    """Subclass can access protected members of parent"""
    
    def max_speed(self):
        return self._speed * 2  # Can access parent's protected member


car_adv = Car_Advanced(50)
car_adv.accelerate(20)
print(f"Maximum speed: {car_adv.max_speed()}")


class SecureVault:
    """Demonstrates private members"""
    
    def __init__(self, combination):
        self.__combination = combination  # Private
    
    def open_vault(self, entered_code):
        return self.__combination == entered_code


class SubVault(SecureVault):
    """Subclass cannot access private members of parent"""
    
    def try_hack(self):
        try:
            print(self.__combination)  # This will fail!
        except AttributeError as e:
            print(f"Cannot access parent's private member: {e}")


vault = SubVault("5678")
vault.try_hack()


# ===== 5. PROPERTY DECORATOR WITH ACCESS CONTROL =====
print("\n5. PROPERTY DECORATOR WITH ACCESS CONTROL")
print("=" * 60 + "\n")


class Temperature:
    """Temperature with property-based access control"""
    
    def __init__(self, celsius):
        self._celsius = celsius  # Protected
    
    @property
    def celsius(self):
        """Read-only property for celsius"""
        return self._celsius
    
    @property
    def fahrenheit(self):
        """Calculated read-only property"""
        return (self._celsius * 9/5) + 32
    
    @celsius.setter
    def celsius(self, value):
        """Setter with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._celsius = value


temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")

temp.celsius = 30
print(f"\nAfter update:")
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")

print(f"\nTrying invalid temperature:")
try:
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}")


# ===== 6. CLASS-LEVEL ACCESS MODIFIERS =====
print("\n6. CLASS-LEVEL ACCESS MODIFIERS")
print("=" * 60 + "\n")


class Configuration:
    """Class with class-level access modifiers"""
    
    # Public class variable
    APP_NAME = "MyApplication"
    
    # Protected class variable
    _version = "1.0"
    
    # Private class variable
    __debug_mode = True
    
    @classmethod
    def get_version(cls):
        """Public method to access protected class variable"""
        return cls._version
    
    @classmethod
    def is_debug_enabled(cls):
        """Public method to access private class variable"""
        return cls.__debug_mode


print(f"App Name: {Configuration.APP_NAME}")
print(f"Version: {Configuration.get_version()}")
print(f"Debug Mode: {Configuration.is_debug_enabled()}")


# ===== 7. SUMMARY TABLE =====
print("\n7. SUMMARY OF ACCESS MODIFIERS")
print("=" * 60)
print("""
╔════════════╦═══════════╦══════════════╦═══════════════════════╗
║  Modifier  ║  Syntax   ║  Accessible  ║  Used When            ║
╠════════════╬═══════════╬══════════════╬═══════════════════════╣
║  Public    ║  name     ║  Everywhere  ║  Normal attributes    ║
║            ║           ║              ║  and methods          ║
╠════════════╬═══════════╬══════════════╬═══════════════════════╣
║ Protected  ║  _name    ║  Class +     ║  Internal use by      ║
║            ║           ║  Subclasses  ║  class and subclass   ║
╠════════════╬═══════════╬══════════════╬═══════════════════════╣
║  Private   ║  __name   ║  Class only  ║  Sensitive data,      ║
║            ║  (mangled)║  (via        ║  internal methods     ║
║            ║           ║  mangling)   ║  that shouldn't be    ║
║            ║           ║              ║  overridden           ║
╚════════════╩═══════════╩══════════════╩═══════════════════════╝
""")


# ===== 8. PRACTICAL EXAMPLE: USER AUTHENTICATION =====
print("\n8. PRACTICAL EXAMPLE: USER AUTHENTICATION SYSTEM")
print("=" * 60 + "\n")


class User:
    """User with comprehensive access control"""
    
    # Public class variable
    total_users = 0
    
    def __init__(self, username, password):
        self.username = username  # Public
        self._created_at = "2025-01-01"  # Protected (internal info)
        self.__password = password  # Private
        self.__failed_attempts = 0  # Private
        User.total_users += 1
    
    def authenticate(self, password):
        """Public method to verify password"""
        if password == self.__password:
            self.__failed_attempts = 0
            return True
        else:
            self.__failed_attempts += 1
            return False
    
    def change_password(self, old_password, new_password):
        """Public method to change password"""
        if self.authenticate(old_password):
            self.__password = new_password
            print("Password changed successfully")
            return True
        else:
            print("Old password is incorrect")
            return False
    
    def _get_user_info(self):
        """Protected method for internal use"""
        return f"{self.username} (Created: {self._created_at})"
    
    def __check_security(self):
        """Private method"""
        return self.__failed_attempts < 3
    
    def get_status(self):
        """Public method that uses private methods"""
        if self.__check_security():
            return f"User {self.username} is active"
        else:
            return f"User {self.username} is locked (too many failed attempts)"


# Create users
user1 = User("alice", "secret123")
user2 = User("bob", "password456")

print(f"Total users: {User.total_users}")
print(f"Username: {user1.username}")

# Authenticate
print(f"\nAuthenticate with correct password: {user1.authenticate('secret123')}")
print(f"Authenticate with wrong password: {user1.authenticate('wrong')}")

# Change password
print(f"\nChange password:")
user1.change_password("secret123", "newsecret")
print(f"Authenticate with new password: {user1.authenticate('newsecret')}")

print(f"\nUser status: {user1.get_status()}")


print("\n" + "=" * 60)
print("✓ ACCESS MODIFIERS TUTORIAL COMPLETED!")
print("=" * 60)

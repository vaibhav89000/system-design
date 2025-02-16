# Abstract Factory Pattern
# The Abstract Factory Pattern is used to create families of related objects without specifying their concrete classes.

# When to Use?
# When you need to create multiple related objects that belong to different product families.
# When object families must be used together.
# Example (Abstract Factory Pattern)
# Scenario: Creating different car brands with different types of Car

from abc import ABC, abstractmethod

# Step 1: Define Abstract Products
class Sedan(ABC):
    @abstractmethod
    def drive(self):
        pass

class SUV(ABC):
    @abstractmethod
    def drive(self):
        pass

# Step 2: Create Concrete Products for Toyota
class ToyotaSedan(Sedan):
    def drive(self):
        return "Driving a Toyota Sedan"

class ToyotaSUV(SUV):
    def drive(self):
        return "Driving a Toyota SUV"

# Step 3: Create Concrete Products for BMW
class BMWSedan(Sedan):
    def drive(self):
        return "Driving a BMW Sedan"

class BMWSUV(SUV):
    def drive(self):
        return "Driving a BMW SUV"

# Step 4: Define Abstract Factory
class CarFactory(ABC):
    @abstractmethod
    def create_sedan(self) -> Sedan:
        pass

    @abstractmethod
    def create_suv(self) -> SUV:
        pass

# Step 5: Implement Concrete Factories
class ToyotaFactory(CarFactory):
    def create_sedan(self):
        return ToyotaSedan()
    
    def create_suv(self):
        return ToyotaSUV()

class BMWFactory(CarFactory):
    def create_sedan(self):
        return BMWSedan()

    def create_suv(self):
        return BMWSUV()

# Usage
def client(factory: CarFactory):
    sedan = factory.create_sedan()
    suv = factory.create_suv()
    print(sedan.drive())  
    print(suv.drive())    

client(ToyotaFactory())  
# Output:
# Driving a Toyota Sedan
# Driving a Toyota SUV

client(BMWFactory())  
# Output:
# Driving a BMW Sedan
# Driving a BMW SUV

# Key Points
# ✔️ Abstract Factory creates related objects that belong to the same family.
# ✔️ Provides multiple factory methods to create different object types.
# ✔️ Ensures objects from different families do not mix.


# 💡 When to Use Which?
# Use Factory Pattern if you only need to create different variants of a single product (e.g., different types of Car).
# Use Abstract Factory Pattern if you need to create multiple related objects (e.g., different car brands with different car types).
# Would you like an example of how these patterns apply to a real-world system like a hotel management system? 🚀

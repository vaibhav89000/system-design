# Factory Pattern
# The Factory Pattern provides a way to create objects of a specific type without exposing the instantiation logic.

# When to Use?
# When you have a single product family (e.g., different types of Car objects).
# When you want to delegate object creation to a separate class instead of using new directly.
# Example (Factory Pattern)
# Scenario: Creating different types of Car

from abc import ABC, abstractmethod

# Step 1: Create an interface (abstract class)
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

# Step 2: Create concrete classes
class Sedan(Car):
    def drive(self):
        return "Driving a Sedan"

class SUV(Car):
    def drive(self):
        return "Driving an SUV"

# Step 3: Implement Factory
class CarFactory:
    @staticmethod
    def get_car(car_type):
        if car_type == "Sedan":
            return Sedan()
        elif car_type == "SUV":
            return SUV()
        else:
            raise ValueError("Invalid car type")

# Usage
car = CarFactory.get_car("SUV")
print(car.drive())  # Output: Driving an SUV

# Key Points
# ✔️ Factory creates objects but hides object creation logic.
# ✔️ Decouples object creation from client code.
# ✔️ Returns one type of object based on input.

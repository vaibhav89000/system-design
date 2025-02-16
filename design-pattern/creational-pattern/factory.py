# Factory Design Pattern 🏭
# The Factory Pattern is a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created.

# 📌 When to Use the Factory Pattern?
# ✅ When object creation logic is complex and should be separated from the client code.
# ✅ When you need to create multiple related objects without specifying their exact class.
# ✅ When you want to promote loose coupling by not exposing concrete classes to the client.

# 🚀 Real-World Example: Vehicle Factory 🚗
# Imagine an application that needs to create different types of vehicles (Car, Bike, Truck). Instead of instantiating classes directly, we use a factory to encapsulate object creation.

# 🔴 Without Factory Pattern (Direct Instantiation)
class Car:
    def drive(self):
        return "Driving a Car 🚗"

class Bike:
    def drive(self):
        return "Riding a Bike 🏍️"

# Client Code
car = Car()
print(car.drive())

bike = Bike()
print(bike.drive())

# 🚨 Problems:
# The client must know the exact class names (Car, Bike).
# Hard to add new vehicle types.
# Tightly coupled to specific implementations.

# ✅ With Factory Pattern (Encapsulated Object Creation)
# Step 1: Define an Interface (Common Behavior)
class Vehicle:
    def drive(self):
        pass  # To be implemented by subclasses

# Step 2: Concrete Implementations
class Car(Vehicle):
    def drive(self):
        return "Driving a Car 🚗"

class Bike(Vehicle):
    def drive(self):
        return "Riding a Bike 🏍️"

class Truck(Vehicle):
    def drive(self):
        return "Driving a Truck 🚛"

# Step 3: Factory Class
class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        vehicles = {
            "car": Car,
            "bike": Bike,
            "truck": Truck
        }
        return vehicles.get(vehicle_type.lower(), None)()

# Step 4: Client Code
vehicle = VehicleFactory.get_vehicle("car")
print(vehicle.drive())  # Output: Driving a Car 🚗

vehicle = VehicleFactory.get_vehicle("bike")
print(vehicle.drive())  # Output: Riding a Bike 🏍️

vehicle = VehicleFactory.get_vehicle("truck")
print(vehicle.drive())  # Output: Driving a Truck 🚛

# 🔑 Key Benefits of the Factory Pattern
# ✔️ Encapsulation of Object Creation – Clients don't need to know the concrete class names.
# ✔️ Promotes Loose Coupling – Client depends only on the factory, not specific implementations.
# ✔️ Easier to Extend – New vehicle types can be added without modifying client code.
# ✔️ Centralized Object Creation – All logic related to object creation stays in one place.

# 🚀 Real-World Use Cases
# Database Connections – DatabaseFactory can return MySQL, PostgreSQL, or SQLite connections.
# Payment Gateways – A factory can create instances for Stripe, PayPal, or Razorpay payments.
# Notification Services – A factory can create SMS, Email, or Push notification handlers.
# Logger Factory – A factory can provide different loggers like FileLogger, ConsoleLogger, etc.

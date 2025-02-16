# Decorator Design Pattern 🎨
# The Decorator Pattern is a structural design pattern that allows adding new functionalities to objects dynamically without modifying their structure. It is useful when you need to extend the behavior of classes at runtime without altering their code.


# When to Use the Decorator Pattern?
# When you want to dynamically add or modify behavior of an object without changing its class.
# When subclassing is not feasible due to the explosion of subclasses.
# When following Open/Closed Principle (open for extension, closed for modification).

# Real-World Example: Coffee Shop ☕
# Imagine a coffee shop where you can customize your coffee by adding milk, sugar, or caramel.

# Without the Decorator Pattern, we'd need to create a new subclass for each combination:
# ☕ EspressoWithMilk
# ☕ EspressoWithSugar
# ☕ EspressoWithMilkAndSugar
# ☕ EspressoWithCaramel ...

# This leads to a subclass explosion! Instead, the Decorator Pattern allows us to dynamically add toppings to coffee.


# Without Decorator (Using Multiple Subclasses)
class Coffee:
    def cost(self):
        return 5  # Base price of coffee

class CoffeeWithMilk(Coffee):
    def cost(self):
        return super().cost() + 2

class CoffeeWithMilkAndSugar(CoffeeWithMilk):
    def cost(self):
        return super().cost() + 1

coffee = CoffeeWithMilkAndSugar()
print(coffee.cost())  # Output: 8


# 🚨 Problems:
# Too many subclasses needed for different combinations.
# Difficult to scale when adding more toppings.

# With Decorator Pattern (Flexible & Scalable)
# Base Component
class Coffee:
    def cost(self):
        return 5

# Decorator Base Class
class CoffeeDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Concrete Decorators
class Milk(CoffeeDecorator):
    def cost(self):
        return super().cost() + 2

class Sugar(CoffeeDecorator):
    def cost(self):
        return super().cost() + 1

class Caramel(CoffeeDecorator):
    def cost(self):
        return super().cost() + 3

# Client Code
coffee = Coffee()  # Plain Coffee (5)
coffee = Milk(coffee)  # Add Milk (5 + 2)
coffee = Sugar(coffee)  # Add Sugar (7 + 1)
coffee = Caramel(coffee)  # Add Caramel (8 + 3)

print(coffee.cost())  # Output: 11

# 🔑 Key Benefits of the Decorator Pattern
# ✔️ Dynamically add behavior at runtime (instead of modifying code).
# ✔️ More flexible than inheritance (no subclass explosion).
# ✔️ Follows Open/Closed Principle (extend functionality without modifying existing code).
# ✔️ Multiple decorators can be combined easily.

# 🚀 Real-World Use Cases
# GUI Frameworks – Wrapping components (e.g., Scrollbars, Borders on UI elements).
# Logging in Python – Wrapping functions with decorators for logging.
# Flask/Django Middleware – Adding request validation, authentication.
# I/O Streams in Java – Wrapping file streams with compression/encryption.
# Game Development – Applying buffs or effects to characters dynamically.


# Adapter Design Pattern 🔌
# The Adapter Pattern is a structural design pattern that allows incompatible interfaces to work together. It acts as a bridge between two incompatible classes, enabling them to interact without modifying their code.

# 📌 When to Use the Adapter Pattern?
# When integrating legacy code with a new system.
# When an existing class does not have the required interface.
# When working with third-party libraries that have different method names.
# 🚀 Real-World Example: Payment Gateway Integration
# Imagine we are developing an e-commerce application, and we need to integrate two different payment gateways:

# Existing system uses PayPal with a method process_payment(amount).
# New requirement: Integrate Stripe, which has make_transaction(amount_in_dollars).
# Since their interfaces do not match, we use an Adapter to standardize the method calls.

# 🔴 Without Adapter (Incompatible Interfaces)
class PayPal:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} via PayPal")

class Stripe:
    def make_transaction(self, amount_in_dollars):
        print(f"Processing payment of ${amount_in_dollars} via Stripe")

# Client Code
paypal = PayPal()
paypal.process_payment(100)  # Works

stripe = Stripe()
stripe.make_transaction(100)  # Different method name! Not compatible!

# 🚨 Problems:
# The Stripe class has a different method name (make_transaction instead of process_payment).
# We need to modify client code every time a new payment provider is added.
# Tightly coupled with specific implementations.


# ✅ With Adapter Pattern (Bridging the Gap)
# We create an Adapter class that provides a common interface for both PayPal and Stripe.


class PayPal:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} via PayPal")

class Stripe:
    def make_transaction(self, amount_in_dollars):
        print(f"Processing payment of ${amount_in_dollars} via Stripe")

# 🔥 Adapter for Stripe to match PayPal's interface
class StripeAdapter:
    def __init__(self, stripe_instance):
        self.stripe = stripe_instance

    def process_payment(self, amount):  # Standardizing method name
        self.stripe.make_transaction(amount)

# Client Code
paypal = PayPal()
stripe_adapter = StripeAdapter(Stripe())  # Using Adapter

# Using a common interface
paypal.process_payment(100)
stripe_adapter.process_payment(100)  # Calls make_transaction internally

# 🔑 Key Benefits of the Adapter Pattern
# ✔️ Enables Incompatible Systems to Work Together
# ✔️ Prevents Code Modification in Legacy Systems
# ✔️ Improves Code Maintainability
# ✔️ Supports Open/Closed Principle (New adapters can be added without changing existing code)

# 🚀 Real-World Use Cases
# Database Migration – Adapting old SQL queries to a new database ORM.
# Third-party API Integration – Standardizing different API responses.
# Legacy System Modernization – Bridging old software with new frameworks.
# Hardware Drivers – Adapting different device drivers to a common interface.

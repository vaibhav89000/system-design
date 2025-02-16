# Prototype Design Pattern 🏗️
# The Prototype Pattern is a creational design pattern that allows cloning objects instead of creating them from scratch.
# It is useful when object creation is costly, complex, or time-consuming.

# 📌 When to Use the Prototype Pattern?
# When object creation is expensive (e.g., deep object initialization, database calls).
# When you need to create multiple objects with similar properties.
# When you want to avoid the complexity of building an object from scratch.
# 🛠 Example: Hotel Room Booking System
# Imagine we are developing a hotel booking system, where we frequently create new hotel rooms with slight modifications.
# Instead of initializing them from scratch, we can clone existing room templates.

# 🚀 Without Prototype Pattern (Traditional Object Creation)

class HotelRoom:
    def __init__(self, room_type, bed, has_tv, has_wifi, has_minibar):
        self.room_type = room_type
        self.bed = bed
        self.has_tv = has_tv
        self.has_wifi = has_wifi
        self.has_minibar = has_minibar

    def __str__(self):
        return f"Room Type: {self.room_type}, Bed: {self.bed}, TV: {self.has_tv}, WiFi: {self.has_wifi}, Minibar: {self.has_minibar}"

# Creating new rooms manually
room1 = HotelRoom("Deluxe", "King", True, True, False)
room2 = HotelRoom("Deluxe", "King", True, True, False)  # Duplicate code
print(room1)
print(room2)

# 🚨 Problems:
# Manual duplication – The same attributes are repeated.
# Error-prone – If a change is needed (e.g., add a new feature), you must modify all instances manually.
# Performance issues – Creating objects from scratch may be slow.


# ✅ With Prototype Pattern (Using Cloning)
# We clone an existing object instead of creating a new one manually.

import copy

class HotelRoom:
    def __init__(self, room_type, bed, has_tv=False, has_wifi=False, has_minibar=False):
        self.room_type = room_type
        self.bed = bed
        self.has_tv = has_tv
        self.has_wifi = has_wifi
        self.has_minibar = has_minibar

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Room Type: {self.room_type}, Bed: {self.bed}, TV: {self.has_tv}, WiFi: {self.has_wifi}, Minibar: {self.has_minibar}"

# Creating a prototype room
prototype_room = HotelRoom("Deluxe", "King", has_tv=True, has_wifi=True)

# Cloning the prototype and modifying only necessary attributes
room1 = prototype_room.clone()
room2 = prototype_room.clone()
room2.has_minibar = True  # Customization

print(room1)
print(room2)

# 🔑 Key Benefits of the Prototype Pattern
# ✔️ Performance Optimization – Avoids unnecessary object creation overhead.
# ✔️ Simplifies Object Creation – Cloning avoids complex constructor logic.
# ✔️ Reduces Code Duplication – No need to repeatedly initialize the same attributes.
# ✔️ Supports Deep Copying – Ensures all nested objects are copied correctly.

# 🚀 Real-World Use Cases
# Game Development 🎮
# Duplicating characters, weapons, or maps to optimize performance.

# UI/UX Design Systems 🎨
# Cloning reusable UI components (e.g., buttons, modals).

# Database Query Caching 📊
# Cloning query results instead of fetching data from the database every time.

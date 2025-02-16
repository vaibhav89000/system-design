# Builder Design Pattern
# The Builder Pattern is a creational design pattern that allows you to construct complex objects step by step. Instead of requiring all parameters in a constructor, it provides a flexible and readable way to build objects.

# 📌 When to Use?
# When an object has multiple optional parameters.
# When creating an object step by step makes sense.
# When object creation becomes too complex due to many configurations.
# 🛠 Example: Building a Hotel Room
# Imagine you need to build a hotel room with various optional features like a bed, TV, minibar, and WiFi.

# 🚀 Without Builder Pattern (Using a Long Constructor)
class HotelRoom:
    def __init__(self, room_type, bed, has_tv, has_wifi, has_minibar):
        self.room_type = room_type
        self.bed = bed
        self.has_tv = has_tv
        self.has_wifi = has_wifi
        self.has_minibar = has_minibar

    def __str__(self):
        return f"Room Type: {self.room_type}, Bed: {self.bed}, TV: {self.has_tv}, WiFi: {self.has_wifi}, Minibar: {self.has_minibar}"

# Creating a room
room = HotelRoom("Deluxe", "King", True, True, False)
print(room)

# 🚨 Issues:

# Hard to read (True, True, False is unclear).
# Difficult to modify or add new features.

# ✅ With Builder Pattern
# The Builder Pattern allows incremental construction of objects in a readable way.

class HotelRoom:
    def __init__(self, room_type, bed, has_tv=False, has_wifi=False, has_minibar=False):
        self.room_type = room_type
        self.bed = bed
        self.has_tv = has_tv
        self.has_wifi = has_wifi
        self.has_minibar = has_minibar

    def __str__(self):
        return f"Room Type: {self.room_type}, Bed: {self.bed}, TV: {self.has_tv}, WiFi: {self.has_wifi}, Minibar: {self.has_minibar}"

# Builder Class
class HotelRoomBuilder:
    def __init__(self, room_type, bed):
        self.room = HotelRoom(room_type, bed)

    def add_tv(self):
        self.room.has_tv = True
        return self

    def add_wifi(self):
        self.room.has_wifi = True
        return self

    def add_minibar(self):
        self.room.has_minibar = True
        return self

    def build(self):
        return self.room

# Usage
room = (
    HotelRoomBuilder("Deluxe", "King")
    .add_tv()
    .add_wifi()
    .build()
)

print(room)  
# Output: Room Type: Deluxe, Bed: King, TV: True, WiFi: True, Minibar: False


# 🔑 Key Benefits
# ✔️ More Readable – Easy to understand which features are included.
# ✔️ Flexible Object Creation – You can add only the features you need.
# ✔️ Encapsulates Construction Logic – Prevents complex __init__ methods.

# 💡 Where is the Builder Pattern Used?
# Real-Life Examples

# Pizza Ordering System (size, cheese, toppings, extra sauce).
# Computer Configuration (RAM, Storage, Graphics Card).
# Car Manufacturing (engine type, sunroof, GPS).
# In Software Development

# SQL Query Builders (e.g., query.select().where().order_by()).
# GUI Builders (building UI elements step by step).

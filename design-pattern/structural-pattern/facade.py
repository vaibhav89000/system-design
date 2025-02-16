# Facade Design Pattern 🏛️
# The Facade Pattern is a structural design pattern that provides a simplified interface to a complex system.
# It hides the complexity of subsystems and exposes only the necessary functionality.

# 📌 When to Use the Facade Pattern?
# ✅ When you have a complex system with multiple subsystems, and you want to provide a simple, unified interface.
# ✅ When you want to decouple clients from complex subsystems.
# ✅ When you need to improve code readability and maintainability.

# 🚀 Real-World Example: Home Theater System 🎬
# A home theater system has multiple components:

# 📺 TV
# 🔊 Sound System
# 🎥 Projector
# 📀 DVD Player
# Each has its own methods, making it complex to operate. Instead of calling multiple methods for each, we create a simple Facade class that provides a watchMovie() method.

# 🔴 Without Facade (Complicated Interface)
class TV:
    def turn_on(self):
        print("TV turned ON")

    def set_input(self, source):
        print(f"TV input set to {source}")

class SoundSystem:
    def turn_on(self):
        print("Sound system turned ON")

    def set_volume(self, level):
        print(f"Volume set to {level}")

class DVDPlayer:
    def turn_on(self):
        print("DVD player turned ON")

    def play_movie(self, movie):
        print(f"Playing movie: {movie}")

# Client Code (Too many steps!)
tv = TV()
sound = SoundSystem()
dvd = DVDPlayer()

tv.turn_on()
tv.set_input("HDMI")
sound.turn_on()
sound.set_volume(10)
dvd.turn_on()
dvd.play_movie("Inception")

# 🚨 Problems:

# The client has to interact with multiple objects separately.
# Hard to remember which method to call first.
# Complexity increases as new components are added.

# ✅ With Facade (Simplified Interface)
# Facade Class
class HomeTheaterFacade:
    def __init__(self):
        self.tv = TV()
        self.sound = SoundSystem()
        self.dvd = DVDPlayer()

    def watch_movie(self, movie):
        print("\n🎬 Getting ready to watch a movie...\n")
        self.tv.turn_on()
        self.tv.set_input("HDMI")
        self.sound.turn_on()
        self.sound.set_volume(10)
        self.dvd.turn_on()
        self.dvd.play_movie(movie)

# Client Code (Simple API)
home_theater = HomeTheaterFacade()
home_theater.watch_movie("Inception")

# 🔑 Key Benefits of the Facade Pattern
# ✔️ Hides Complexity – Provides a simple interface to a complex system.
# ✔️ Decouples Clients from Subsystems – Clients don’t need to interact with each component individually.
# ✔️ Improves Maintainability – Easier to update subsystems without affecting clients.
# ✔️ Reduces Dependencies – Changes in subsystems don’t directly affect clients.

# 🚀 Real-World Use Cases
# Operating Systems – A GUI acts as a facade for complex system calls.
# Database Access – ORM (Object-Relational Mapping) like SQLAlchemy hides raw SQL queries.
# Web Frameworks – Django provides a high-level interface for request handling.
# Cloud Services – AWS SDKs simplify interactions with multiple cloud services.
# E-commerce Systems – A checkout system integrates payment, shipping, and inventory.

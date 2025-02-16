# Flyweight Design Pattern 

# The Flyweight Pattern is a structural design pattern that helps reduce memory usage by sharing objects instead of creating new ones. It is useful when a large number of similar objects exist, leading to high memory consumption.

# 📌 When to Use the Flyweight Pattern?
# ✅ When an application needs to handle a large number of similar objects efficiently.
# ✅ When objects have common shared state (intrinsic state) and unique external state (extrinsic state).
# ✅ When memory usage is a concern, and object reuse can optimize performance.

# 🚀 Real-World Example: Text Editor with Character Objects
# Imagine a text editor that displays millions of characters. Instead of creating a new object for each character, we reuse character objects to save memory.

# 🔴 Without Flyweight (High Memory Usage)
class Character:
    def __init__(self, char, font, color):
        self.char = char
        self.font = font
        self.color = color

    def render(self, position):
        print(f"Rendering '{self.char}' at {position} with font {self.font} and color {self.color}")

# Creating multiple objects (HIGH MEMORY USAGE)
char1 = Character('A', 'Arial', 'Black')
char2 = Character('A', 'Arial', 'Black')  # Duplicate object ❌
char3 = Character('B', 'Arial', 'Black')

char1.render((10, 20))
char2.render((15, 20))  # Duplicate object wastes memory
char3.render((20, 20))

# 🚨 Problems:

# Each character object has duplicate properties (e.g., 'A' with the same font & color).
# High memory usage when dealing with large documents.

# ✅ With Flyweight (Efficient Memory Usage)
# 🔹 Key Idea:
# Intrinsic State (shared): Character, font, color (stored in Flyweight).
# Extrinsic State (unique): Position (provided dynamically).

# Step 1: Flyweight Factory (Manages Shared Objects)
class CharacterFactory:
    _characters = {}

    @staticmethod
    def get_character(char, font, color):
        key = (char, font, color)
        if key not in CharacterFactory._characters:
            CharacterFactory._characters[key] = Character(char, font, color)
        return CharacterFactory._characters[key]

# Step 2: Flyweight Object (Shared Data)
class Character:
    def __init__(self, char, font, color):
        self.char = char
        self.font = font
        self.color = color

    def render(self, position):
        print(f"Rendering '{self.char}' at {position} with font {self.font} and color {self.color}")

# Step 3: Client Code (Efficient Object Reuse)
char1 = CharacterFactory.get_character('A', 'Arial', 'Black')
char2 = CharacterFactory.get_character('A', 'Arial', 'Black')  # Reuses existing object ✅
char3 = CharacterFactory.get_character('B', 'Arial', 'Black')

char1.render((10, 20))
char2.render((15, 20))  # Same object reused
char3.render((20, 20))

# 🔹 How Does It Work?
# ✅ CharacterFactory ensures that duplicate characters are not created.
# ✅ Memory usage is reduced by sharing common objects.
# ✅ Performance is optimized by reusing already created objects.

# 🔑 Key Benefits of the Flyweight Pattern
# ✔️ Reduces memory consumption – Avoids creating duplicate objects.
# ✔️ Improves performance – Fewer objects = Less memory allocation.
# ✔️ Encourages object reuse – Factory ensures shared instances.
# ✔️ Decouples object creation – Clients request objects from a factory instead of instantiating them directly.

# 🚀 Real-World Use Cases
# Text Editors – Reusing character objects (A, B, etc.) instead of creating new ones.
# Game Development – Reusing tree models, bullets, or enemies to optimize memory.
# Graphical Applications – Icons, buttons, or sprites that appear multiple times on UI.
# Caching Systems – Storing frequently used objects in memory instead of creating new ones.
# Database Connection Pools – Reusing database connections instead of creating new ones.

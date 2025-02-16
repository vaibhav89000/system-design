# Composite Design Pattern 🌳
# The Composite Pattern is a structural design pattern that lets you treat individual objects and groups of objects uniformly. It is useful when you need to build a tree-like structure, such as file systems, UI components, or hierarchical organizations.

# 📌 When to Use the Composite Pattern?
# When you need to treat single objects and collections (composites) the same way.
# When dealing with hierarchical structures (e.g., file systems, organization charts, UI layouts).
# When performing operations on the entire structure recursively.
# 🚀 Real-World Example: File System (Files & Folders)
# A File System consists of Files and Folders (which can contain Files and other Folders).
# Without the Composite Pattern, we would need to handle files and folders separately, leading to complex code.

# With the Composite Pattern, we can treat both Files and Folders uniformly.

# 🔴 Without Composite (Handling Files & Folders Separately)

class File:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"File: {self.name}")

class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, item):
        self.children.append(item)

    def show(self):
        print(f"Folder: {self.name}")
        for child in self.children:
            child.show()

# Client Code
file1 = File("document.txt")
file2 = File("image.png")
folder = Folder("MyFolder")
folder.add(file1)
folder.add(file2)

folder.show()

# 🚨 Problems:
# We need to manually check if an object is a File or Folder.
# The logic becomes more complex when adding more operations.

# ✅ With Composite Pattern (Treating Files & Folders Uniformly)
# Using an abstract class (Component), we treat Files and Folders the same way.

# Component (Base Class)
class FileSystemComponent:
    def show(self):
        pass

# Leaf (File)
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"File: {self.name}")

# Composite (Folder)
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def show(self):
        print(f"Folder: {self.name}")
        for child in self.children:
            child.show()

# Client Code
file1 = File("document.txt")
file2 = File("image.png")

folder = Folder("MyFolder")
folder.add(file1)
folder.add(file2)

root = Folder("Root")
root.add(folder)
root.add(File("video.mp4"))

root.show()

# 🔥 Output:
# Folder: Root
#   Folder: MyFolder
#     File: document.txt
#     File: image.png
#   File: video.mp4

# 🔑 Key Benefits of the Composite Pattern
# ✔️ Simplifies Client Code (Single interface for both individual objects and groups)
# ✔️ Works with Recursive Structures (E.g., file systems, UI elements, organization charts)
# ✔️ Supports Open/Closed Principle (New elements can be added without modifying existing code)
# ✔️ Uniform Treatment of Objects & Collections

# 🚀 Real-World Use Cases
# File System – Files and Folders.
# UI Components – Buttons, Panels, Containers (where a container can hold multiple UI elements).
# Organizational Hierarchy – Employees and Managers (who can have subordinates).
# Graphics System – Shapes, Groups of Shapes (e.g., Vector Graphics).
# E-commerce Categories – Categories and Subcategories containing products.

# Bridge Design Pattern 🌉
# The Bridge Pattern is a structural design pattern that helps decouple abstraction from implementation,
# allowing them to evolve independently. It is useful when you want to avoid rigid class hierarchies and
# prefer composition over inheritance.
# It also solves m*n problem by providing solution with m+n

# 📌 When to Use the Bridge Pattern?
# When you have multiple dimensions of variability (e.g., a hierarchy of Shapes and another hierarchy of Rendering APIs).
# When you want to decouple abstraction from its implementation so both can evolve independently.
# When you need to avoid an explosion of subclasses due to multiple variations.
# 🚀 Real-World Example: Shapes & Rendering APIs
# Imagine a graphics library where we need to draw shapes using different rendering APIs (e.g., Raster API and Vector API).
# Without the Bridge Pattern, we would have too many subclasses (e.g., CircleRaster, CircleVector, SquareRaster, SquareVector).

# Instead, we separate:

# Abstraction: Shape (Circle, Square)
# Implementation: Rendering API (Raster, Vector)
# 🔴 Without Bridge (Rigid & Complex Hierarchy)

class CircleRaster:
    def draw(self):
        print("Drawing Circle using Raster API")

class CircleVector:
    def draw(self):
        print("Drawing Circle using Vector API")

class SquareRaster:
    def draw(self):
        print("Drawing Square using Raster API")

class SquareVector:
    def draw(self):
        print("Drawing Square using Vector API")

# Issue: What if we add Triangle? We need two more classes!

# 🚨 Problems:
# Subclass Explosion: Adding new shapes or rendering APIs requires creating multiple new classes.
# Hard to Maintain: Code is tightly coupled.

# ✅ With Bridge Pattern (Decoupling Abstraction & Implementation)
# We separate Shape (Abstraction) and RenderingAPI (Implementation).

# Implementor (Rendering API)
class Renderer:
    def render(self, shape):
        pass

# Concrete Implementors
class RasterRenderer(Renderer):
    def render(self, shape):
        print(f"Drawing {shape} using Raster API")

class VectorRenderer(Renderer):
    def render(self, shape):
        print(f"Drawing {shape} using Vector API")

# Abstraction (Shape)
class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass

# Refined Abstraction (Concrete Shapes)
class Circle(Shape):
    def draw(self):
        self.renderer.render("Circle")

class Square(Shape):
    def draw(self):
        self.renderer.render("Square")

# Client Code
raster = RasterRenderer()
vector = VectorRenderer()

circle = Circle(raster)
square = Square(vector)

circle.draw()  # Drawing Circle using Raster API
square.draw()  # Drawing Square using Vector API

# 🔑 Key Benefits of the Bridge Pattern
# ✔️ Decouples Abstraction & Implementation (Allows independent evolution)
# ✔️ Prevents Subclass Explosion (Avoids creating too many subclasses)
# ✔️ Improves Code Maintainability & Scalability
# ✔️ Supports Open/Closed Principle (New shapes or rendering APIs can be added easily)

# 🚀 Real-World Use Cases
# Cross-Platform Development – UI components that work with multiple rendering engines.
# Database Drivers – Abstracting database interactions while supporting multiple databases.
# Operating System Independence – File system handlers working across Windows, Linux, macOS.
# Game Development – Supporting multiple rendering engines (e.g., DirectX, OpenGL, Vulkan).

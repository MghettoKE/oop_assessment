from abc import ABC, abstractmethod
import math


# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Subclass Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Subclass Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


# Create instances of Circle and Square
circle = Circle(5)
square = Square(4)

# Call the area method on both objects
print(f"Area of Circle: {circle.area():.2f}")
print(f"Area of Square: {square.area()}")

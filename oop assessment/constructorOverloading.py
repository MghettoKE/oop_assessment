class Rectangle:
    def __init__(self, length, width=None):
        # If only one argument is provided, it's a square
        if width is None:
            self.length = length
            self.width = length
        else:
            self.length = length
            self.width = width

    def area(self):
        return self.length * self.width

# Create a square (one argument)
square = Rectangle(5)

# Create a rectangle (two arguments)
rectangle = Rectangle(4, 6)

# Calculate and print areas
print(f"Area of the square: {square.area()}")
print(f"Area of the rectangle: {rectangle.area()}")

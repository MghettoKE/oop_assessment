class Vector:
    def __init__(self, x, y):
        self.x = x  # x-component of the vector
        self.y = y  # y-component of the vector

    def __add__(self, other):
        # Check if the other object is a Vector
        if isinstance(other, Vector):
            # Return a new Vector object as the result of vector addition
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# Create two Vector objects
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Add the two vectors using the overloaded + operator
v3 = v1 + v2

# Print the result of the vector addition
print(f"v1 + v2 = {v3}")

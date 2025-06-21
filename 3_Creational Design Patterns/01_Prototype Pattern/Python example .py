"""

This script demonstrates the Prototype Design Pattern in Python using a simple example.
Imagine we're creating different types of shapes, and instead of creating new ones from scratch,
we clone existing ones and change only the necessary properties.
"""

import copy
from abc import ABC, abstractmethod

# Prototype Interface
class Shape(ABC):
    """
    The Prototype interface declares a clone method that
    all concrete prototypes must implement.
    """

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def draw(self):
        pass

# Concrete Prototype A
class Circle(Shape):
    def __init__(self, radius: float, color: str):
        self.radius = radius
        self.color = color

    def clone(self):
        # Return a deep copy to avoid shared references
        return copy.deepcopy(self)

    def draw(self):
        print(f"Drawing a {self.color} circle with radius {self.radius}")

# Concrete Prototype B
class Rectangle(Shape):
    def __init__(self, width: float, height: float, color: str):
        self.width = width
        self.height = height
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

    def draw(self):
        print(f"Drawing a {self.color} rectangle of size {self.width}x{self.height}")

# Client code using the Prototype Pattern
def main():
    """
    This function simulates a client that wants to duplicate objects
    using the Prototype pattern rather than creating them from scratch.
    """

    # Create original objects
    red_circle = Circle(5, "red")
    blue_rectangle = Rectangle(4, 6, "blue")

    # Clone objects
    another_red_circle = red_circle.clone()
    another_red_circle.radius = 10  # Modify only necessary fields

    another_blue_rectangle = blue_rectangle.clone()
    another_blue_rectangle.color = "green"

    # Draw original and cloned shapes
    red_circle.draw()
    another_red_circle.draw()
    blue_rectangle.draw()
    another_blue_rectangle.draw()

if __name__ == "__main__":
    main()

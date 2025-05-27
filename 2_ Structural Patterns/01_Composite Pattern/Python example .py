"""
Adapter Design Pattern - Python Example

Scenario: A drawing application needs to use a standard Shape interface,
but we have a legacy Rectangle class that doesn't match it.
The Adapter pattern helps integrate the legacy class without modifying it.
"""

# Target Interface
class Shape:
    """
    The interface that the client expects.
    All shapes should implement a draw() method.
    """
    def draw(self):
        raise NotImplementedError("draw() must be implemented by subclasses")


# Adaptee (Legacy Class)
class LegacyRectangle:
    """
    A legacy class that does not follow the Shape interface.
    It uses a different method name and parameter style.
    """
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw_rectangle(self):
        print(f"Drawing rectangle from ({self.x1}, {self.y1}) to ({self.x2}, {self.y2})")


# Adapter
class RectangleAdapter(Shape):
    """
    Adapter that allows LegacyRectangle to be used as a Shape.
    Implements the draw() method expected by the client.
    """
    def __init__(self, legacy_rectangle):
        self.legacy_rectangle = legacy_rectangle

    def draw(self):
        # Convert the draw() call to draw_rectangle()
        self.legacy_rectangle.draw_rectangle()


# Client Code
if __name__ == "__main__":
    # Client expects to work with objects of type Shape

    # Create a legacy rectangle
    legacy = LegacyRectangle(10, 20, 30, 40)

    # Wrap it in an adapter to make it compatible with the Shape interface
    adapted_shape = RectangleAdapter(legacy)

    print("Client: I'm expecting to use a Shape interface...")
    adapted_shape.draw()  # Output: Drawing rectangle from (10, 20) to (30, 40)

    # Now we can use LegacyRectangle in systems that expect Shape!

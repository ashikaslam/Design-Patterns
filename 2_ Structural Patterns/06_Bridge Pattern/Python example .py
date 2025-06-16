"""

This script demonstrates the Bridge Design Pattern using a shape drawing system
where the abstraction (Shape) is separated from the implementation (DrawingAPI).
This separation allows flexibility in choosing how to draw the shape
without modifying the shape classes themselves.

Useful for avoiding class explosion and decoupling abstraction from implementation.
"""

# --- Implementor Interface ---
class DrawingAPI:
    """
    The Implementor defines the interface for implementation classes.
    In this case, it's an abstract drawing API.
    """
    def draw_circle(self, x: float, y: float, radius: float):
        raise NotImplementedError("You must implement draw_circle().")


# --- Concrete Implementors ---
class DrawingAPI1(DrawingAPI):
    """
    ConcreteImplementor 1: Provides one way to draw a circle.
    """
    def draw_circle(self, x: float, y: float, radius: float):
        print(f"[DrawingAPI1] Drawing circle at ({x}, {y}) with radius {radius}")


class DrawingAPI2(DrawingAPI):
    """
    ConcreteImplementor 2: Provides another way to draw a circle.
    """
    def draw_circle(self, x: float, y: float, radius: float):
        print(f"[DrawingAPI2] Drawing circle at ({x}, {y}) with radius {radius}")


# --- Abstraction ---
class Shape:
    """
    The Abstraction maintains a reference to an Implementor (DrawingAPI),
    and defines the interface for the 'client' code.
    """
    def __init__(self, drawing_api: DrawingAPI):
        self.drawing_api = drawing_api

    def draw(self):
        raise NotImplementedError("You must implement draw().")

    def resize_by_percentage(self, pct: float):
        raise NotImplementedError("You must implement resize_by_percentage().")


# --- Refined Abstraction ---
class CircleShape(Shape):
    """
    A RefinedAbstraction that represents a circle.
    Delegates drawing to the DrawingAPI (Implementor).
    """
    def __init__(self, x: float, y: float, radius: float, drawing_api: DrawingAPI):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        """
        Uses the DrawingAPI to draw the circle.
        """
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

    def resize_by_percentage(self, pct: float):
        """
        Resizes the circle by a given percentage.
        """
        self.radius *= (1 + pct / 100)


# --- Client Code ---
if __name__ == "__main__":
    # Create circles with different drawing APIs
    circle1 = CircleShape(5, 10, 3, DrawingAPI1())
    circle2 = CircleShape(15, 20, 7, DrawingAPI2())

    # Resize and draw the circles
    print("Drawing circle1 using DrawingAPI1:")
    circle1.resize_by_percentage(50)
    circle1.draw()

    print("\nDrawing circle2 using DrawingAPI2:")
    circle2.resize_by_percentage(-30)
    circle2.draw()
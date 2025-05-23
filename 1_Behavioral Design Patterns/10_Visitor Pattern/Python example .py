"""
Visitor Pattern Example in Python

Scenario: Tax calculation on different product types.
We'll implement a visitor that calculates tax based on the product type.
"""

from abc import ABC, abstractmethod

# ========================
# Visitor Interface
# ========================
class TaxVisitor(ABC):
    """
    Visitor Interface: Declares visit methods for each type of concrete element.
    """
    @abstractmethod
    def visit_book(self, book):
        pass

    @abstractmethod
    def visit_electronics(self, electronics):
        pass


# ========================
# Element Interface
# ========================
class Product(ABC):
    """
    Element Interface: Declares the accept method that accepts a visitor.
    """
    @abstractmethod
    def accept(self, visitor: TaxVisitor):
        pass


# ========================
# Concrete Elements
# ========================
class Book(Product):
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def accept(self, visitor: TaxVisitor):
        """Call the appropriate visitor method for this class."""
        return visitor.visit_book(self)


class Electronics(Product):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def accept(self, visitor: TaxVisitor):
        return visitor.visit_electronics(self)


# ========================
# Concrete Visitor
# ========================
class TaxCalculator(TaxVisitor):
    """
    Concrete Visitor: Implements different tax rules for each product type.
    """
    def visit_book(self, book: Book):
        tax = book.price * 0.05  # 5% tax
        print(f"Book: {book.title}, Price: {book.price}, Tax: {tax}")
        return tax

    def visit_electronics(self, electronics: Electronics):
        tax = electronics.price * 0.15  # 15% tax
        print(f"Electronics: {electronics.name}, Price: {electronics.price}, Tax: {tax}")
        return tax


# ========================
# Client Code
# ========================
if __name__ == "__main__":
    # Create products
    items = [
        Book("Design Patterns", 50.0),
        Electronics("Smartphone", 300.0)
    ]

    # Create a visitor
    tax_calculator = TaxCalculator()

    print("\n--- Tax Calculation Using Visitor Pattern ---")
    total_tax = 0.0
    for item in items:
        total_tax += item.accept(tax_calculator)

    print(f"\nTotal Tax: {total_tax}")

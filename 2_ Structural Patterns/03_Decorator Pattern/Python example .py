"""
Decorator Pattern - Python Example

Scenario: Coffee Shop Order Customization
We have a base Coffee object and want to dynamically add ingredients like Milk, Sugar, and Whipped Cream.
"""

from abc import ABC, abstractmethod

# Step 1: Component Interface
class Coffee(ABC):
    """
    The base Component interface declares a method that all concrete components and decorators must implement.
    """
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass


# Step 2: Concrete Component
class SimpleCoffee(Coffee):
    """
    A basic implementation of the Coffee component.
    """
    def cost(self):
        return 5  # base cost in dollars

    def description(self):
        return "Simple Coffee"


# Step 3: Decorator Base Class
class CoffeeDecorator(Coffee):
    """
    The base decorator class wraps a Coffee component.
    """
    def __init__(self, coffee):
        self._coffee = coffee


# Step 4: Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    """
    Adds Milk to the Coffee.
    """
    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return self._coffee.description() + ", Milk"


class SugarDecorator(CoffeeDecorator):
    """
    Adds Sugar to the Coffee.
    """
    def cost(self):
        return self._coffee.cost() + 1

    def description(self):
        return self._coffee.description() + ", Sugar"


class WhipDecorator(CoffeeDecorator):
    """
    Adds Whipped Cream to the Coffee.
    """
    def cost(self):
        return self._coffee.cost() + 3

    def description(self):
        return self._coffee.description() + ", Whip Cream"


# Step 5: Usage Example
if __name__ == "__main__":
    # Start with a simple coffee
    my_coffee = SimpleCoffee()

    # Add milk
    my_coffee = MilkDecorator(my_coffee)

    # Add sugar
    my_coffee = SugarDecorator(my_coffee)

    # Add whipped cream
    my_coffee = WhipDecorator(my_coffee)

    print("Order:", my_coffee.description())
    print("Total cost: $", my_coffee.cost())

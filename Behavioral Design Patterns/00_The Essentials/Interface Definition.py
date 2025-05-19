"""
What is an Interface in Python?

In Python, an interface is a design pattern that defines a set of methods
that a class must implement, but it doesn't provide the implementation itself.

Since Python doesn't have a built-in 'interface' keyword like Java or C#,
we typically use the abc (Abstract Base Class) module to define abstract classes
with @abstractmethod decorators. This enforces that any subclass must implement
the required methods, ensuring a consistent structure across multiple implementations.

Interfaces are useful when we want to enforce a contract between components,
making our code more modular, testable, and extensible—following SOLID principles
like the Dependency Inversion Principle.

Example usage of interface in Python:
"""

from abc import ABC, abstractmethod

# Defining the interface
class PaymentProcessor(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass

# Implementing the interface
class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} payment through PayPal")

class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} payment through Stripe")

# Example function using the interface
def checkout(processor: PaymentProcessor, amount):
    processor.process_payment(amount)

# Driver code
if __name__ == "__main__":
    paypal = PayPalProcessor()
    stripe = StripeProcessor()

    checkout(paypal, 100)
    checkout(stripe, 200)

# --------------------------------------
# This file demonstrates how to implement interfaces in Python
# using the abc module (Abstract Base Classes).
# --------------------------------------

from abc import ABC, abstractmethod

# Step 1: Define an interface using an abstract base class (ABC)
class PaymentProcessor(ABC):
    """
    This is an interface-like class in Python.
    Any class that inherits from this must implement the process_payment method.
    """

    @abstractmethod
    def process_payment(self, amount):
        """
        Abstract method that must be implemented by all subclasses.
        This defines the contract: every PaymentProcessor must handle payment processing.
        """
        pass

# Step 2: Create a class that implements the interface
class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} using PayPal")


# Step 3: Create another class implementing the same interface
class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} using Stripe")


# Step 4: Use the interface in code

def make_payment(processor: PaymentProcessor, amount):
    """
    This function accepts any object that implements the PaymentProcessor interface.
    It doesn't care how the payment is processed, only that the method exists.
    """
    processor.process_payment(amount)


# Example usage:
if __name__ == "__main__":
    paypal = PayPalProcessor()
    stripe = StripeProcessor()

    make_payment(paypal, 100)
    make_payment(stripe, 200)


# Why use interfaces like this?
# -----------------------------
# - They help enforce consistency across classes.
# - They allow dependency injection and loose coupling.
# - You can swap implementations easily (e.g., for testing).
# - It follows SOLID principles, especially the Dependency Inversion Principle.

# Bonus: A class without process_payment() will raise TypeError
# Uncomment below to see it in action:
# class IncompleteProcessor(PaymentProcessor):
#     pass
# This will throw: TypeError: Can't instantiate abstract class IncompleteProcessor



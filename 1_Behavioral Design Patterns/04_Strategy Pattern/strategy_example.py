# strategy_example.py

# This script demonstrates the Strategy Design Pattern.
# The Strategy Pattern allows the behavior of a class to be selected at runtime.
# In this example, we use different payment methods (strategies) for a shopping cart.


from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Strategy A
class CreditCardPayment(PaymentStrategy):
    def __init__(self, name, card_number):
        self.name = name
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card ({self.card_number}) by {self.name}.")

# Concrete Strategy B
class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid ${amount} using PayPal ({self.email}).")

# Context class
class ShoppingCart:
    def __init__(self):
        self.amount = 0
        self.payment_strategy = None

    def set_payment_strategy(self, strategy):
        """
        Sets the payment method dynamically at runtime.
        """
        self.payment_strategy = strategy

    def checkout(self):
        if not self.payment_strategy:
            raise Exception("Payment strategy is not set!")
        self.payment_strategy.pay(self.amount)

    def add_item(self, price):
        self.amount += price
        print(f"Item added. Current total: ${self.amount}")

# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item(50)
    cart.add_item(100)

    # Set strategy to CreditCard
    credit_card = CreditCardPayment("John Doe", "1234-5678-9876-5432")
    cart.set_payment_strategy(credit_card)
    cart.checkout()

    print("\nSwitching to PayPal...\n")

    # Reuse the cart with a different strategy
    cart2 = ShoppingCart()
    cart2.add_item(30)
    paypal = PayPalPayment("john@example.com")
    cart2.set_payment_strategy(paypal)
    cart2.checkout()

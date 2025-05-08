"""
What is Abstraction in Python?

Abstraction is one of the core principles of Object-Oriented Programming (OOP).
It means hiding the internal implementation details of a class and only exposing
what is necessary for the user. This simplifies code interaction and improves security
by preventing direct access to internal states.

In Python, abstraction is typically implemented using the `abc` module (Abstract Base Classes),
which allows us to define abstract classes and methods using the `@abstractmethod` decorator.
This enforces a contract for subclasses to implement the abstract methods.

Abstraction makes it easier to manage complexity by breaking down code into more manageable parts.

Example usage of abstraction in Python:
"""

from abc import ABC, abstractmethod

# Abstract class (Abstraction)
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

# Concrete class implementing abstract methods
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")

# Concrete class implementing abstract methods
class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started")

    def stop_engine(self):
        print("Motorcycle engine stopped")

# Driver code
if __name__ == "__main__":
    vehicle1 = Car()
    vehicle2 = Motorcycle()

    vehicle1.start_engine()
    vehicle1.stop_engine()

    vehicle2.start_engine()
    vehicle2.stop_engine()

"""
This script demonstrates the Factory Method Design Pattern in Python.
We define a base Creator class and let subclasses decide which ConcreteProduct to return.
This is a beginner-friendly example involving transport logistics.
"""
from abc import ABC, abstractmethod

# Product Interface
class Transport(ABC):
    """
    The Product interface declares operations that all concrete products must implement.
    """
    @abstractmethod
    def deliver(self):
        pass

# Concrete Product A
class Truck(Transport):
    def deliver(self):
        print("Delivery by land in a box.")

# Concrete Product B
class Ship(Transport):
    def deliver(self):
        print("Delivery by sea in a container.")

# Creator Abstract Class
class Logistics(ABC):
    """
    The Creator class declares the factory method that returns new Transport objects.
    Subclasses will override this method to specify which transport to instantiate.
    """
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self):
        """
        This method uses the factory method to get a product instance,
        and then uses it to perform a task.
        """
        transport = self.create_transport()
        transport.deliver()

# Concrete Creator A
class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

# Concrete Creator B
class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

# Client code

def main():
    """
    The client code works with an instance of a Logistics subclass,
    and relies on polymorphism and the factory method.
    """

    # Deliver using a truck (land)
    road_logistics = RoadLogistics()
    road_logistics.plan_delivery()

    # Deliver using a ship (sea)
    sea_logistics = SeaLogistics()
    sea_logistics.plan_delivery()

if __name__ == "__main__":
    main()

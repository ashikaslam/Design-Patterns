"""
This script demonstrates the Builder Design Pattern in Python.
We simulate building a computer by assembling parts step by step using a builder.
"""

from abc import ABC, abstractmethod

# Product class
class Computer:
    """
    The product class representing the object being built.
    """
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None

    def show_specs(self):
        """Print the computer's specifications."""
        print("Computer Specifications:")
        print(f"  CPU: {self.cpu}")
        print(f"  GPU: {self.gpu}")
        print(f"  RAM: {self.ram}")
        print(f"  Storage: {self.storage}")

# Builder Interface
class ComputerBuilder(ABC):
    """
    Abstract builder interface that defines all the steps to build a computer.
    """
    @abstractmethod
    def add_cpu(self):
        pass

    @abstractmethod
    def add_gpu(self):
        pass

    @abstractmethod
    def add_ram(self):
        pass

    @abstractmethod
    def add_storage(self):
        pass

    @abstractmethod
    def get_computer(self) -> Computer:
        pass

# Concrete Builder
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def add_cpu(self):
        self.computer.cpu = "Intel Core i9"

    def add_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4090"

    def add_ram(self):
        self.computer.ram = "32GB DDR5"

    def add_storage(self):
        self.computer.storage = "2TB NVMe SSD"

    def get_computer(self) -> Computer:
        return self.computer

# Director class
class ComputerDirector:
    """
    The director defines the sequence in which to build the computer.
    It is optional but helps to organize the building steps.
    """
    def __init__(self, builder: ComputerBuilder):
        self._builder = builder

    def build_computer(self):
        """
        Construct the computer using a series of defined steps.
        """
        self._builder.add_cpu()
        self._builder.add_gpu()
        self._builder.add_ram()
        self._builder.add_storage()

# Client code

def main():
    """
    This function demonstrates using the builder to create a complex object.
    """
    # Create a builder
    builder = GamingComputerBuilder()

    # Create a director and build the computer
    director = ComputerDirector(builder)
    director.build_computer()

    # Get the final product
    computer = builder.get_computer()
    computer.show_specs()

if __name__ == "__main__":
    main()

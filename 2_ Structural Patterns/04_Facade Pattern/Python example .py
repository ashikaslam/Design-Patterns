"""
facade_pattern_example.py

This script demonstrates the Facade Design Pattern using a classical computer system startup example.
The Facade Pattern provides a simplified interface to a complex subsystem.
Here, the 'Computer' class acts as a Facade, hiding the intricate details of
booting a computer by orchestrating interactions with various low-level components
like the CPU, Memory, and Hard Drive.

Author: Md Aslam
"""

# --- Subsystem Classes ---
# These classes represent the individual, low-level components of the computer system.
# They perform specific tasks and are unaware of the 'Computer' Facade or each other.

class CPU:
    """
    Represents the Central Processing Unit (CPU) subsystem.
    Handles basic CPU operations during startup.
    """
    def freeze(self):
        """
        Halts the CPU to prepare for loading new instructions.
        """
        print("CPU: Freezing processor.")

    def jump(self, position):
        """
        Sets the program counter to a specific memory address.
        Args:
            position (int): The memory address to jump to.
        """
        print(f"CPU: Jumping to address {position}.")

    def execute(self):
        """
        Starts executing instructions from the current program counter position.
        """
        print("CPU: Executing instructions.")

class Memory:
    """
    Represents the computer's Memory (RAM) subsystem.
    Handles loading data into memory.
    """
    def load(self, position, data):
        """
        Loads a block of data into a specified memory position.
        Args:
            position (int): The starting memory address.
            data (str): The data (e.g., boot loader code) to load.
        """
        print(f"Memory: Loading data '{data[:20]}...' into position {position}.") # Truncate for display

class HardDrive:
    """
    Represents the Hard Drive subsystem.
    Handles reading data from the hard drive.
    """
    def read(self, lba, size):
        """
        Reads a specified number of bytes from a Logical Block Address (LBA) on the hard drive.
        Args:
            lba (int): The Logical Block Address to start reading from.
            size (int): The number of bytes to read.
        Returns:
            str: Simulated boot loader code.
        """
        print(f"HardDrive: Reading {size} bytes from sector {lba}.")
        # In a real system, this would read actual data.
        # For this example, we return a simulated boot loader code.
        return "boot_loader_code_from_hard_drive"

# --- Facade Class ---
# This is the Facade. It provides a simplified, high-level interface to the complex
# computer startup subsystem. The client (main part of the script) interacts only with this class.

class Computer:
    """
    The Facade class for controlling a computer system's startup process.
    It provides a simplified interface ('start_computer') to hide the complexity
    of interacting directly with the CPU, Memory, and Hard Drive subsystems.
    """
    def __init__(self):
        """
        Initializes the Computer Facade with instances of all necessary subsystem components.
        """
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        """
        Provides a simple, unified interface for clients to start the computer.
        This method orchestrates the calls to the various subsystem components
        in the correct sequence for a successful boot-up.
        """
        print("\n--- Starting computer via Facade ---")
        # 1. Freeze the CPU to prepare for loading
        self.cpu.freeze()
        # 2. Read the boot loader code from the hard drive
        boot_code = self.hard_drive.read(lba=100, size=1024)
        # 3. Load the boot loader code into memory
        self.memory.load(position=0, data=boot_code)
        # 4. Jump the CPU to the start of the loaded boot code in memory
        self.cpu.jump(position=0)
        # 5. Execute the instructions (boot loader)
        self.cpu.execute()
        print("--- Computer startup complete ---")

# --- Client Code ---
# The client interacts only with the 'Computer' Facade, without needing
# to know the intricate details or order of operations of the underlying subsystems.

if __name__ == "__main__":
    print("Client: Requesting computer to start...")
    # 1. The client creates an instance of the Facade.
    computer = Computer()
    # 2. The client calls the simplified method on the Facade.
    computer.start_computer()

    print("\nClient: Computer is now running (simplified interaction).")
    # If the client needed to perform a low-level operation not exposed by the Facade,
    # they would have to access the subsystem objects directly (e.g., computer.cpu.freeze()).
    # However, the Facade discourages this for common operations.

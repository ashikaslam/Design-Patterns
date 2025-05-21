"""
Command Pattern Example in Python

This script demonstrates the Command Pattern, where commands are encapsulated as objects,
allowing them to be executed, undone, or stored for later.

Components:
- Command interface (Command)
- ConcreteCommand classes (TurnOnCommand, TurnOffCommand)
- Receiver (Light)
- Invoker (RemoteControl)
- Client code that ties everything together
"""

from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Receiver Class
class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")

# Concrete Command to turn the light ON
class TurnOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

# Concrete Command to turn the light OFF
class TurnOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()

# Invoker Class
class RemoteControl:
    def __init__(self):
        self.history = []  # Stores command history

    def submit(self, command: Command):
        """
        Executes a command and stores it in history
        """
        command.execute()
        self.history.append(command)

    def undo_last(self):
        """
        Undoes the last command
        """
        if self.history:
            last_command = self.history.pop()
            last_command.undo()
        else:
            print("No commands to undo")

# Client Code
if __name__ == "__main__":
    # Receiver
    living_room_light = Light()

    # Concrete Commands
    turn_on = TurnOnCommand(living_room_light)
    turn_off = TurnOffCommand(living_room_light)

    # Invoker
    remote = RemoteControl()

    # Send commands
    remote.submit(turn_on)   # Output: Light is ON
    remote.submit(turn_off)  # Output: Light is OFF

    # Undo last command
    remote.undo_last()       # Output: Light is ON
    remote.undo_last()       # Output: Light is OFF
    remote.undo_last()       # Output: No commands to undo

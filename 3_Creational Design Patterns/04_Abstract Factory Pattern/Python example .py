"""


This example demonstrates the Abstract Factory Pattern.
We define factories that create related GUI components (buttons and checkboxes)
for different operating systems (Windows and Mac).
"""
from abc import ABC, abstractmethod

# Abstract Product A
class Button(ABC):
    """
    Abstract product interface for Button.
    """
    @abstractmethod
    def render(self):
        pass

# Abstract Product B
class Checkbox(ABC):
    """
    Abstract product interface for Checkbox.
    """
    @abstractmethod
    def render(self):
        pass

# Concrete Product A1
class WindowsButton(Button):
    def render(self):
        print("Rendering a Windows button.")

# Concrete Product B1
class WindowsCheckbox(Checkbox):
    def render(self):
        print("Rendering a Windows checkbox.")

# Concrete Product A2
class MacButton(Button):
    def render(self):
        print("Rendering a Mac button.")

# Concrete Product B2
class MacCheckbox(Checkbox):
    def render(self):
        print("Rendering a Mac checkbox.")

# Abstract Factory
class GUIFactory(ABC):
    """
    Abstract factory interface defining creation methods
    for each type of product in the product family.
    """
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factory 1
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

# Concrete Factory 2
class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# Client Code
class Application:
    """
    The Application class uses the abstract factory to create GUI components.
    This makes the application independent of the concrete classes.
    """
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()

    def render_ui(self):
        """
        Render all UI elements created by the factory.
        """
        self.button.render()
        self.checkbox.render()

# Demo usage

def main():
    """
    This function demonstrates how to use different factories to create
    different families of related products.
    """

    print("Client: Running app with the Windows factory:")
    app1 = Application(WindowsFactory())
    app1.render_ui()

    print("\nClient: Running app with the Mac factory:")
    app2 = Application(MacFactory())
    app2.render_ui()

if __name__ == "__main__":
    main()

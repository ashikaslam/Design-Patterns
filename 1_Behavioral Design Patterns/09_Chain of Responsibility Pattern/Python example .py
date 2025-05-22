"""
Chain of Responsibility Pattern - Python Example

Scenario: Helpdesk Ticket Processing System
Each support level will handle certain types of requests.
If a handler can't process it, it passes the request to the next one in the chain.
"""

from abc import ABC, abstractmethod

class SupportHandler(ABC):
    """
    Abstract Handler:
    Defines the interface for handling requests and optional next handler linkage.
    """
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        """
        Set the next handler in the chain.
        """
        self._next_handler = handler
        return handler  # for chaining

    @abstractmethod
    def handle(self, request):
        pass

class LevelOneSupport(SupportHandler):
    """
    Concrete Handler 1:
    Handles simple issues (e.g., password reset)
    """
    def handle(self, request):
        if request == "password reset":
            print("Level 1 Support: Handling password reset request.")
        elif self._next_handler:
            self._next_handler.handle(request)
        else:
            print("Level 1 Support: No handler found for request.")

class LevelTwoSupport(SupportHandler):
    """
    Concrete Handler 2:
    Handles intermediate issues (e.g., software installation)
    """
    def handle(self, request):
        if request == "install software":
            print("Level 2 Support: Handling software installation request.")
        elif self._next_handler:
            self._next_handler.handle(request)
        else:
            print("Level 2 Support: No handler found for request.")

class ManagerSupport(SupportHandler):
    """
    Concrete Handler 3:
    Handles high-level or urgent issues (e.g., data breach)
    """
    def handle(self, request):
        if request == "data breach":
            print("Manager Support: Handling critical data breach issue!")
        elif self._next_handler:
            self._next_handler.handle(request)
        else:
            print("Manager Support: No handler found for request.")

# Example usage of the pattern
if __name__ == "__main__":
    # Create handlers
    level1 = LevelOneSupport()
    level2 = LevelTwoSupport()
    manager = ManagerSupport()

    # Chain them together
    level1.set_next(level2).set_next(manager)

    # Send different requests
    print("\n--- Request: password reset ---")
    level1.handle("password reset")

    print("\n--- Request: install software ---")
    level1.handle("install software")

    print("\n--- Request: data breach ---")
    level1.handle("data breach")

    print("\n--- Request: unknown issue ---")
    level1.handle("unknown issue")

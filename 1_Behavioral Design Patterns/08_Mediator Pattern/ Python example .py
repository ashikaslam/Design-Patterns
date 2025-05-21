"""
Mediator Pattern - Python Example

This example demonstrates the Mediator Pattern using a simple chat room scenario.
Users (colleagues) communicate through a central ChatRoom (mediator),
not directly with each other.

Suitable for: Learning and demonstration purposes.
"""

from typing import List

# Mediator Interface
class ChatMediator:
    def show_message(self, sender, message):
        raise NotImplementedError("Subclasses must implement this method")


# Concrete Mediator
class ChatRoom(ChatMediator):
    def __init__(self):
        self.participants = []  # List of all users in the chatroom

    def register(self, user):
        self.participants.append(user)

    def show_message(self, sender, message):
        # Notify all users except the sender
        for user in self.participants:
            if user != sender:
                user.receive(sender.name, message)


# Colleague Interface
class User:
    def __init__(self, name: str, mediator: ChatMediator):
        self.name = name
        self.mediator = mediator
        mediator.register(self)  # Register this user with the mediator

    def send(self, message: str):
        print(f"[You] {self.name}: {message}")
        self.mediator.show_message(self, message)

    def receive(self, sender_name: str, message: str):
        print(f"[{sender_name}] to {self.name}: {message}")


# Client Code
if __name__ == "__main__":
    chat_room = ChatRoom()

    alice = User("Alice", chat_room)
    bob = User("Bob", chat_room)
    charlie = User("Charlie", chat_room)

    alice.send("Hello, everyone!")
    bob.send("Hi Alice!")
    charlie.send("Good to see you all.")

"""
Explanation:

- The `ChatRoom` acts as the Mediator. It registers users and distributes messages.
- `User` objects (colleagues) send messages via the mediator, not directly to each other.
- This removes tight coupling between users. If one user leaves or is added, others don’t need to change.

This example mimics real-world chat systems, air traffic control, or even smart home hubs.
"""

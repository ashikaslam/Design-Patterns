# Command Pattern

## Definition

The **Command Pattern** is a behavioral design pattern that turns a request into a stand-alone object containing all the information about the request. This transformation lets you parameterize methods with different requests, delay or queue requests, and support undoable operations.

In short, it encapsulates a command (or action) as an object, thereby decoupling the sender from the receiver.

---

## Main Purpose and Core Idea

* **Encapsulation of a request:** You encapsulate a request (like an action or method call) into a command object.
* **Decoupling:** It separates the object that sends the command from the one that knows how to perform it.
* **Extensibility:** You can add new commands without changing existing code.
* **Undo/Redo capability:** Commands can store state, allowing undo/redo operations.

---

## Real-World Use Cases

* **Remote Controls:** Each button on a remote control can represent a command.
* **Transactional Systems:** Queue or log requests for later processing (like message queues).
* **GUI Buttons or Menu Items:** When clicking a button, the associated command is triggered.
* **Macro Recording:** Record executed commands and play them back in order.

---

## Software Use Cases

* Task scheduling systems
* Game development (e.g., player actions)
* Database operations (undoable actions)
* Command-line interface applications

---

## Advantages

* **Decouples invoker and receiver.**
* **Supports undo and redo.**
* **Commands can be stored, logged, or queued.**
* **Easier to add new commands without modifying existing code.**

---

## Disadvantages

* **Can lead to a large number of command classes.**
* **May increase system complexity due to additional layers.**

---

## UML Structure Explanation (Text Format)

```
Client --> Invoker --> Command (interface)
                      ^
                      |
                 ConcreteCommand --> Receiver
```

### Participants:

* **Client:** Creates a command object and sets its receiver.
* **Invoker:** Stores command object and triggers the command.
* **Command (interface):** Declares an `execute()` method.
* **ConcreteCommand:** Implements the `execute()` method, calls the appropriate method of the receiver.
* **Receiver:** Knows how to perform the actual work.

---

## When to Use It

Use the Command pattern when:

* You want to parameterize objects with operations.
* You need to queue or schedule requests.
* You need to support undo/redo of operations.
* You want to decouple the sender of a request from the object that performs the action.

---

## When Not to Use It

Avoid using it when:

* You don’t need undo functionality or history tracking.
* The system is simple and commands are unlikely to change.
* Too many command classes would add unnecessary complexity.

---

## Summary / Takeaway

The Command Pattern is powerful when you need flexibility in executing, delaying, or undoing operations. By encapsulating actions as objects, you promote decoupling and open your system to extensions like macro recording, queuing, and transactional rollback. However, be cautious of overusing it in simple scenarios, as it can introduce unnecessary class bloat.

> Think of it like pressing a button on a remote — you don’t care how it works internally, but you trust that the command will be executed properly. That’s what Command Pattern is all about!

# 🧩 Mediator Design Pattern

## 📖 Definition

The **Mediator Pattern** is a behavioral design pattern that promotes loose coupling between components by having them communicate indirectly through a **mediator object**. This central object encapsulates how components interact, preventing them from referring to each other explicitly.

---

## 🎯 Purpose & Core Idea

The Mediator pattern's core goal is to manage communication between objects in a **centralized** manner to avoid complex dependencies and tangled object relationships.

Instead of each object managing its own interactions, they defer communication and coordination to a **Mediator**. This promotes **separation of concerns**, cleaner code, and easier maintenance.

---

## 🌍 Real-World Examples

* **Air Traffic Control (ATC):** Planes don't communicate with each other directly; instead, the ATC (mediator) directs all aircraft.
* **Chat Rooms:** Users don't send messages directly to other users—they post to a chat room (mediator) that relays the messages.
* **Smart Home Systems:** Devices like lights, thermostats, and alarms can coordinate via a central hub or app (mediator).

---

## 💻 Software Use Cases

* UI component coordination (buttons, forms, sliders)
* Chat/messaging systems
* Event buses and publish-subscribe mechanisms
* Game engines (managing interaction between game entities)

---

## ✅ Advantages

* **Loose coupling** between components
* Easy to modify interactions without changing many classes
* Promotes **single responsibility**: each class handles only its logic, not communication
* Facilitates centralized logging, control, or security policies

---

## ❌ Disadvantages

* The Mediator can become a **God object** if it grows too large
* May make the flow of control harder to follow in large systems
* Adds a layer of indirection, which may not be needed in simple scenarios

---

## 🔧 UML/Structure (Text Format)

```
+---------------------+         +-----------------------+
|     Mediator        |<--------|      Colleague        |
+---------------------+         +-----------------------+
| + notify(sender)    |         | + send(message)       |
| + register(col)     |         | + receive(message)    |
+---------------------+         +-----------------------+
        ▲                                ▲
        |                                |
+---------------------+         +-----------------------+
|  ConcreteMediator   |         |  ConcreteColleague    |
+---------------------+         +-----------------------+
| - references to all |         | - reference to Mediator|
|   colleagues         |        +-----------------------+
+---------------------+
```

---

## 📝 Summary / Takeaway

* Use the Mediator pattern when multiple classes need to communicate but you want to avoid tight coupling.
* Especially useful when objects are **closely interacting** in many ways.
* By centralizing communication logic, your code becomes easier to manage and extend.

---

**"Don’t let components talk to each other directly**—make them talk through a central mediator."

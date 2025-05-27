# Adapter Design Pattern - Guide

## Definition

The Adapter Pattern is a structural design pattern that allows incompatible interfaces to work together. It acts as a bridge between two incompatible interfaces by wrapping one interface (the adaptee) and exposing a different interface that the client expects.

---

## Purpose and Core Idea

The core idea is to convert the interface of a class into another interface that clients expect. This enables classes to work together that otherwise could not because of incompatible interfaces.

---

## Real-World Analogy

* A power adapter converts one plug shape/voltage to another so your laptop can work in another country.

---

## Software Use Cases

* Integrating legacy code into a modern system
* Connecting third-party libraries with different interfaces
* Wrapping APIs or SDKs to fit internal interfaces

---

## Advantages

* Promotes code reusability
* Enables decoupling between classes
* Supports single responsibility principle
* Allows using existing classes without modifying their code

---

## Disadvantages

* Can add extra complexity
* Excessive use can make code harder to understand
* Might lead to too many layers of abstraction

---

## UML/Structure (Text Format)

```
Client ---> Target Interface <--- Adapter ---> Adaptee (existing/legacy class)
```

* **Client**: Uses the Target interface
* **Target**: Defines the interface expected by the client
* **Adapter**: Converts the interface of the Adaptee into the Target interface
* **Adaptee**: Existing interface that needs adapting

---

## Summary / Takeaway

The Adapter Pattern is perfect for integrating components that have incompatible interfaces. It helps bridge differences between old and new systems or external APIs and internal logic, without changing the original code.

Use it when:

* You want to reuse an existing class, but its interface doesn't match what you need
* You need to interact with third-party or legacy code with different interfaces

Avoid it when:

* You can refactor the source or client code instead
* The Adapter would overly complicate the codebase

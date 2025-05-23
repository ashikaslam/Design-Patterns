# Visitor Design Pattern - Python Guide

## What is the Visitor Pattern?

The **Visitor Pattern** is a behavioral design pattern that lets you separate algorithms from the objects on which they operate. Instead of modifying the classes of the elements you want to operate on, you create a visitor class that implements specific behaviors.

In simple terms, **Visitor allows you to add new operations to existing object structures without modifying the structures.**

---

## Core Idea

* The object structure (e.g., a collection of elements) remains unchanged.
* A Visitor class is introduced to perform operations on elements of the object structure.
* Each element "accepts" a visitor, which allows the visitor to execute the operation.

---

## Real-World Analogies

* **Museum Tour Guide**: Each room in a museum calls the same `accept(visitor)` method when a guide (visitor) enters. The guide knows what to say depending on the room.
* **Tax Calculation**: Different product items can accept a tax calculator visitor that calculates tax differently depending on item type.

---

## Real-World Software Use Cases

* **Compilers**: Abstract Syntax Trees (ASTs) accept visitors for semantic analysis, code generation, etc.
* **UI Frameworks**: Elements like buttons or text fields accept a visitor to render, validate, or localize.
* **File Systems**: File or Folder classes accept visitors for scanning, antivirus, or indexing.

---

## Advantages

* **Open/Closed Principle**: Add new operations without changing the object structure.
* **Clean Separation**: Business logic (visitor) is separated from data structure (elements).
* **Multiple Operations**: Easily add multiple unrelated operations.

---

## Disadvantages

* **Breaking Encapsulation**: Visitors may need to access internal data of elements.
* **Tight Coupling**: Element classes must be aware of visitors (via the `accept` method).
* **Difficult to Add New Element Types**: Every visitor must update to handle the new element.

---

## UML Structure (Text Format)

```
+-----------------+         +------------------+
|     Visitor     |<--------|    Element       |
+-----------------+         +------------------+
| +visitConcreteA()|        | +accept(visitor) |
| +visitConcreteB()|        +------------------+
+-----------------+                   ^
       ^                               |
       |                               |
+------------------+         +------------------+
| ConcreteVisitor1 |         | ConcreteElementA |
+------------------+         +------------------+
| visitConcreteA() |         | accept(visitor)  |
| visitConcreteB() |         +------------------+
+------------------+
```

---

## When to Use the Visitor Pattern

* When your object structure is stable but you need to perform many unrelated operations.
* When operations involve multiple unrelated classes of objects.
* When you want to keep related behaviors in one place (visitor) instead of spreading across many classes.

---

## When NOT to Use the Visitor Pattern

* If the object structure changes frequently (e.g., you add/remove element types).
* If encapsulation is critical and internal details shouldn't be exposed.

---

## Summary

| Feature        | Description                                   |
| -------------- | --------------------------------------------- |
| Type           | Behavioral Pattern                            |
| Problem Solved | Decouple operations from object structure     |
| Good For       | Extending logic without changing data classes |
| Bad For        | Frequently changing element classes           |

**Bottom Line**: Use the Visitor Pattern when you want to apply operations to objects without changing their classes.

# Factory Method Pattern - Design Pattern in Python

## Definition

The **Factory Method Pattern** is a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to **alter the type of objects that will be created**.

## Purpose & Core Idea

The main idea of the Factory Method is to **delegate the responsibility of instantiating objects to child classes**. Instead of calling a constructor directly, you call a factory method, which handles the creation logic and returns the object.

This helps decouple the client code from concrete classes, promoting flexibility and scalability.

## Real-World Analogies

* **Hiring agency**: A client asks for an employee (e.g., designer or developer), but the agency decides which specific employee to provide.
* **Food delivery app**: You order food (interface), and the app internally chooses the right restaurant to fulfill the order (concrete class).

## Software Use Cases

* Frameworks that allow users to extend and override part of the creation process.
* GUI libraries where you create buttons, dialogs, etc., that vary depending on the operating system.
* Logger libraries that produce different types of loggers (e.g., file logger, console logger).
* When the exact type of object isn't known until runtime.

## Advantages

* **Promotes loose coupling** by hiding concrete class instantiations.
* **Makes code easier to extend** (add new product types without modifying existing code).
* Adheres to **Open/Closed Principle**.

## Disadvantages

* Can result in **more classes and complexity**.
* Might require **subclassing** to change product types.
* May be **overkill** for simple object creation.

## UML Structure (Text Format)

```
+-------------------+
|   Creator         |<-----------------------------+
+-------------------+                              |
| + factory_method()|<---+                         |
| + some_operation()|    |                         |
+-------------------+    |                         |
                         |                         |
                         v                         |
                +------------------+              |
                | ConcreteCreator  |--------------+
                +------------------+
                | + factory_method()|
                +------------------+
                        |
                        v
                +----------------+
                |   Product      |
                +----------------+
                | + operation()  |
                +----------------+
                        ^
                        |
                +----------------------+
                |   ConcreteProductA   |
                +----------------------+
```

### Components

* **Product**: Interface of the object to be created.
* **ConcreteProduct**: Concrete implementations of the product.
* **Creator**: Declares the factory method.
* **ConcreteCreator**: Implements the factory method to return specific products.

## Summary

The Factory Method Pattern is a powerful way to handle object creation logic in a scalable and extensible manner. It's especially useful in frameworks and libraries where customization of object creation is necessary. While it adds some complexity, it pays off when flexibility and adherence to SOLID principles are required.


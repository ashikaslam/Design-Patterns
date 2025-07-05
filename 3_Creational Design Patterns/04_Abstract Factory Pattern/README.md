# Abstract Factory Pattern - Design Pattern in Python

## Definition

The **Abstract Factory Pattern** is a creational design pattern that provides an interface for creating **families of related or dependent objects** without specifying their concrete classes.

## Purpose & Core Idea

The main idea of the Abstract Factory Pattern is to **create groups of related products** without depending on their specific implementations. It allows for switching between product families easily and ensures that related products are used together consistently.

This pattern is an extension of the Factory Method pattern, but instead of a single product, it creates a **set of related products**.

## Real-World Analogies

* **UI Toolkits**: A GUI framework that supports multiple themes (e.g., DarkThemeFactory, LightThemeFactory), each creating matching buttons, scrollbars, and text fields.
* **Car factories**: An electric car factory creates electric engines and electric tires; a gas car factory creates gas engines and tires.

## Software Use Cases

* Cross-platform GUI applications (Windows, macOS, Linux)
* Applications requiring theme/style switching (Light theme, Dark theme)
* Families of related objects with specific compatibility requirements
* Dependency injection scenarios

## Advantages

* **Encapsulates product family creation**
* Ensures **consistency** among related objects
* Supports **product interchangeability** (e.g., switch theme or platform easily)
* Promotes adherence to **Open/Closed Principle**

## Disadvantages

* Adding new product types (not families) can be **difficult**, requiring changes in all factories
* Can become **overly complex** with too many product types or families
* Might lead to **class explosion**

## UML Structure (Text Format)

```
+-------------------------+
|     AbstractFactory     |
+-------------------------+
| + create_product_a()    |
| + create_product_b()    |
+-------------------------+
        ^            ^
        |            |
+----------------+ +----------------+
| Factory1       | | Factory2       |
+----------------+ +----------------+
| + create_a()   | | + create_a()   |
| + create_b()   | | + create_b()   |
+----------------+ +----------------+
        |                    |
        v                    v
+---------------+   +----------------+
| ProductA1     |   | ProductA2      |
+---------------+   +----------------+

+---------------+   +----------------+
| ProductB1     |   | ProductB2      |
+---------------+   +----------------+
```

## Summary

The Abstract Factory Pattern is ideal when your system needs to be **independent of how its objects are created** and when you want to ensure **families of related products are used together consistently**. It’s especially helpful for applications that require UI theming or platform independence. Use with caution in simpler systems, as it may introduce unnecessary complexity.


# Builder Pattern - Design Pattern in Python

## Definition

The **Builder Pattern** is a creational design pattern that allows you to **construct complex objects step by step**. It separates the construction of a complex object from its representation so that the same construction process can create different representations.

## Purpose & Core Idea

The core idea of the Builder Pattern is to **build an object gradually** using a builder object that provides methods to construct and assemble parts of the object. This is especially useful when creating objects with many optional parameters or when object construction is complex and should be separated from the object’s logic.

## Real-World Analogies

* **Meal preparation**: You can build a meal by combining different parts (burger, drink, fries), and the same steps can create different combos.
* **Construction process**: A building can be constructed floor by floor, regardless of whether it’s a house, apartment, or office.

## Software Use Cases

* Creating objects with **many optional attributes or parameters**.
* When the object creation involves **multiple steps or complex logic**.
* To construct **immutable objects**.
* For code that needs to support **various configurations or variants** of an object.

## Advantages

* Separates object creation from its structure.
* Makes code easier to read and maintain.
* Helps in constructing complex objects consistently.
* Allows **reuse** of the building process for different object representations.

## Disadvantages

* More classes and code to maintain.
* Can be **overkill** for simple objects.

## UML Structure (Text Format)

```
+-------------------+      +---------------------+
|     Director      |      |      Builder        |
+-------------------+      +---------------------+
| - builder         |<>----| + build_part_a()    |
| + construct()     |      | + build_part_b()    |
+-------------------+      | + get_result()      |
                           +---------------------+
                                    ^
                                    |
               +---------------------------+
               |   ConcreteBuilder          |
               +---------------------------+
               | + build_part_a()          |
               | + build_part_b()          |
               | + get_result()            |
               +---------------------------+
                                    |
                                    v
                           +-----------------+
                           |   Product        |
                           +-----------------+
```

### Components

* **Product**: The complex object being built.
* **Builder Interface**: Declares the building steps.
* **Concrete Builder**: Implements the building steps and returns the product.
* **Director**: Orchestrates the building steps in a specific order.

## Summary

The Builder Pattern is ideal for constructing complex objects step by step. It decouples the construction logic from the representation and provides a clear, maintainable way to handle various configurations of an object. While it introduces extra classes, its flexibility and clarity make it a solid choice for object creation in many applications.


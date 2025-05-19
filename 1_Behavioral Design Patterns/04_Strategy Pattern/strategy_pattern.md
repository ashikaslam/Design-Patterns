# Strategy Design Pattern

## Definition

The **Strategy Pattern** is a behavioral design pattern that enables selecting an algorithm's behavior at runtime. It defines a family of algorithms, encapsulates each one, and makes them interchangeable without changing the code that uses them.

## Purpose and Core Idea

The main purpose of the Strategy Pattern is to allow a client class to delegate a specific behavior (or algorithm) to a separate class (called a strategy) instead of implementing it directly.

It helps in adhering to the **Open/Closed Principle** — your code is open for extension but closed for modification.

## Real-World Examples

* **Navigation apps** like Google Maps offer different routing strategies: shortest distance, least time, avoid tolls.
* **Payment methods** in e-commerce: credit card, PayPal, bank transfer, etc.
* **Compression tools** that allow users to choose between different algorithms like ZIP, RAR, or 7z.

## Software Use Cases

* Selecting different data sorting algorithms at runtime.
* Applying different tax strategies based on country.
* Logging strategies: write logs to file, database, or external service.

## Advantages

* Avoids multiple `if-else` or `switch` statements.
* Promotes code reusability and separation of concerns.
* Makes code easier to maintain and extend.
* Strategies can be tested independently.

## Disadvantages

* Adds more classes to the codebase.
* Clients must be aware of the different strategies.
* Slightly more complex to design initially than hard-coding behavior.

## UML Structure (Text Format)

```
+----------------+       uses       +---------------------+
| Context        |---------------->| Strategy (Interface) |
+----------------+                 +---------------------+
| - strategy     |                 | + execute()         |
| + setStrategy()|                 +---------------------+
| + execute()    |                         /   \
+----------------+                        /     \
                                          /       \
                           +--------------------+ +--------------------+
                           | ConcreteStrategyA  | | ConcreteStrategyB  |
                           +--------------------+ +--------------------+
                           | + execute()        | | + execute()        |
                           +--------------------+ +--------------------+
```

## Summary / Takeaway

* The Strategy Pattern is ideal when you need different variants of an algorithm.
* It promotes cleaner code with better separation of responsibility.
* It’s one of the key patterns to master for writing maintainable and extendable software.

This pattern is particularly useful in Python due to the language’s support for first-class functions, which can serve as strategies.

---

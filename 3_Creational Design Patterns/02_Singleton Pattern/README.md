# Singleton Pattern - Design Pattern in Python

## Definition

The **Singleton Pattern** is a creational design pattern that ensures a class has **only one instance** and provides a **global access point** to that instance.

## Purpose & Core Idea

The main goal of the Singleton Pattern is to **control object creation**, limiting the number of instances to just **one**. This is useful when exactly one object is needed to coordinate actions across the system (e.g., configuration manager, logging, cache).

## Real-World Analogies

* **President of a country**: There can be only one president at a time.
* **Database connection**: You might want to have a single shared connection throughout your app.
* **Print spooler**: Ensures only one queue manages print jobs.

## Software Use Cases

* **Logging services**
* **Configuration managers**
* **Database connection pools**
* **Thread or job schedulers**
* **Caching and in-memory storage**

## Advantages

* Ensures **controlled access** to sole instances
* **Saves memory** by not recreating objects
* Can **enforce constraints** on shared resources (like only one logger writing to a file)

## Disadvantages

* Can **introduce global state**, making unit testing harder
* Can **violate the Single Responsibility Principle**
* **Multithreading issues** if not implemented correctly
* Overuse can lead to **tight coupling**

## UML Structure (Text Format)

```
+-------------------+
|   SingletonClass  |
+-------------------+
| - _instance       |
+-------------------+
| + get_instance()  |
| + some_method()   |
+-------------------+
```

* `_instance`: A class-level private variable holding the single instance.
* `get_instance()`: A public static method to access the singleton.
* `some_method()`: Business logic method(s).

## Summary

The Singleton Pattern is useful when a class must have **exactly one object**. While it's commonly used in areas like logging, configuration, or state tracking, it should be used with care to avoid issues related to **testing, concurrency, and global state**.


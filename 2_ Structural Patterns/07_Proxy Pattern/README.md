# Proxy Design Pattern

## Definition

The **Proxy Pattern** is a structural design pattern that provides a surrogate or placeholder object for another object to control access to it. It acts as an intermediary, which can perform additional actions (like access control, logging, lazy initialization, etc.) before delegating a request to the real object.

## Main Purpose and Core Idea

The core idea of the Proxy Pattern is to provide controlled access to an object by creating a proxy object that acts as a substitute. The proxy can:

* Control access to the real object
* Add additional functionality (e.g., caching, logging, lazy loading)
* Act as a placeholder when the real object is resource-intensive or remote

## Real-World Use Cases

* **Virtual Proxy**: Load heavy objects (like images) on demand
* **Protection Proxy**: Authorize access to sensitive resources
* **Remote Proxy**: Communicate with objects in different address spaces (e.g., RMI in Java)
* **Smart Proxy**: Add additional behaviors like logging, reference counting

### Software Examples

* ORM lazy-loading features
* API gateways
* File access with permission checks

## Advantages

* Adds a layer of control without modifying the actual object
* Can delay object creation (lazy loading)
* Can enhance performance with caching
* Helps in managing access rights

## Disadvantages

* Adds complexity and additional classes
* May slow down performance due to the added indirection
* Overuse may lead to unnecessary abstraction

## UML / Structure Explanation (Text Format)

```
Client --> Subject Interface <-- Proxy --> RealSubject

Client: Uses the Subject interface
Subject: Interface for RealSubject and Proxy
Proxy: Implements Subject and controls access to RealSubject
RealSubject: The actual object that does the work
```

## When to Use It

* When you want to add access control to an object
* When dealing with resource-intensive objects and want to load them on demand
* When you want to add functionality (e.g., logging, caching) transparently

## When Not to Use It

* When performance is critical and the overhead of the proxy is not acceptable
* When object access is simple and doesn’t need extra logic

## Summary

The Proxy Pattern is a powerful way to manage access to objects and add extra behavior transparently. It fits well when you need lazy initialization, security layers, or distributed communication. However, it should be used judiciously to avoid over-engineering.


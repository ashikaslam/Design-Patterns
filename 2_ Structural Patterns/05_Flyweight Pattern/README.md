# Flyweight Design Pattern

## Definition

The **Flyweight Pattern** is a structural design pattern that aims to **minimize memory usage** by sharing as much data as possible with similar objects. It achieves this by storing shared data (called **intrinsic state**) externally from the unique data (called **extrinsic state**) and reusing existing instances of objects instead of creating new ones.

## Purpose and Core Idea

The core idea of the Flyweight Pattern is to reduce the number of objects being created and to decrease memory usage and increase performance by sharing objects that are identical in terms of intrinsic data.

* **Intrinsic state**: Shared state stored in the Flyweight object; does not change between different contexts.
* **Extrinsic state**: Context-specific state passed to the object from outside.

## Real-World and Software Use Cases

* **Text editors**: Characters are shared; only their positions and styles are external.
* **Map applications**: Icons (like trees or cars) can be reused instead of creating a new object every time.
* **Game development**: Tiles, enemies, or bullets that look the same can reuse the same object.
* **Caching mechanisms**: Shared database connections or loaded images.

## Advantages and When to Use It

* **Reduces memory usage**: Especially effective when you have thousands or millions of similar objects.
* **Improves performance**: Fewer objects = less overhead.
* **Object sharing**: Centralizes control over object state.

**Use it when:**

* You have a large number of objects that share common data.
* Memory usage is a concern.
* The overhead of managing shared state is acceptable.

## Disadvantages or When Not to Use It

* **Complexity**: Adds architectural complexity by separating intrinsic and extrinsic state.
* **Not always worth it**: Overhead of managing the pool/factory might outweigh the benefits for smaller object sets.
* **Thread-safety**: Shared objects might need synchronization.

## UML / Structure Explanation (Text Format)

```
+-----------------+           +-----------------+
|  Flyweight      |<>-------->| FlyweightFactory|
+-----------------+           +-----------------+
| +operation()    |           | +get_flyweight()|
+-----------------+           +-----------------+
        ^
        |
+---------------------+
|  ConcreteFlyweight  |
|  -intrinsic_state   |
|  +operation(ext)    |
+---------------------+

Client -- uses --> FlyweightFactory -- returns shared --> ConcreteFlyweight
```

* **Flyweight**: Interface declaring methods that ConcreteFlyweights implement.
* **ConcreteFlyweight**: Implements Flyweight, stores intrinsic state.
* **FlyweightFactory**: Creates and manages the Flyweight pool.
* **Client**: Uses the Flyweights and supplies extrinsic state.

## Summary / Takeaway

* The Flyweight Pattern is a memory-saving technique used when many objects share common properties.
* It’s useful in high-performance environments like game development, GUIs, or simulations.
* It’s all about separating what can be shared (intrinsic) from what must be unique (extrinsic).

---

> ✅ "Don’t create more than you need — reuse what you can."

---

A corresponding Python example file is provided to demonstrate how this works in practice.

# Iterator Pattern

## ✅ Definition

The Iterator Pattern provides a way to access elements of a collection sequentially without exposing its internal structure.

---

## 🧠 When to Use

- When you want to **traverse** a collection without exposing its internal structure.
- When you want to **support multiple types of traversals** (forward, backward, filtering).
- When you want to implement **custom iteration logic** over a collection.
- When multiple clients need to traverse the same collection independently.

---

## ❌ When *Not* to Use

- If your language (like Python) already provides adequate iteration constructs (`__iter__`, `__next__`).
- If the object structure is trivial and you don’t need abstraction for iteration.
- If you don’t need to encapsulate or customize traversal behavior.

---

## 🔧 Use Cases

- Tree traversal (in-order, pre-order, etc.)
- Browsing history
- Playlist navigation
- Undo/Redo functionality
- Custom filtering or lazy evaluation

---

## 🧱 Components

- **Iterator**: Defines an interface for accessing and traversing elements.
- **ConcreteIterator**: Implements the Iterator interface and keeps track of the current position in the traversal.
- **Aggregate (Iterable)**: The collection object that provides an interface to create the iterator.
- **Client**: Uses the iterator to access elements of the collection.

---

## 📌 UML Diagram (Conceptual)


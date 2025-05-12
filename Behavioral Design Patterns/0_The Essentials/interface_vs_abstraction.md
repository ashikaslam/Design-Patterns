

# Interface vs Abstraction in Python

Python does not have a built-in `interface` keyword like Java or C#, but we can still define interfaces and abstract classes using the `abc` module. While both interfaces and abstractions are implemented using Abstract Base Classes (ABCs), they serve different purposes.

---

## ✅ Quick Comparison Table

| Feature                    | Interface                              | Abstraction                              |
|----------------------------|----------------------------------------|-------------------------------------------|
| **Focus**                 | *What* methods must be implemented     | *What* to expose, *how* to hide details   |
| **Implementation**        | Only abstract methods                  | Can have both abstract & concrete methods |
| **Use case**              | Enforce consistent API across classes  | Hide complexity and enable code reuse     |
| **Code reuse**            | ❌ Not allowed                          | ✅ Allowed (with concrete methods)         |
| **Common in**             | Design contracts and plugin systems    | Base classes with shared logic            |
| **Example**               | `class Interface(ABC): ...`            | `class AbstractBase(ABC): ...`            |

---

## 🧠 Explanation

### 🔹 Interface
An **interface** is a design pattern that defines a set of methods that a class must implement. It acts as a *contract*.

- Focuses only on method names (no implementation)
- Helps in creating loosely coupled components
- Promotes polymorphism

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


🔚 Final summary:
"We need abstraction to not just define what should be done (like an interface) but also to hide internal logic and reuse common code. Interfaces focus on enforcing structure, while abstraction also helps manage complexity."
# Template Method Design Pattern

## Definition

The **Template Method** is a behavioral design pattern that defines the skeleton of an algorithm in a method, deferring some steps to subclasses. It allows subclasses to redefine certain steps of an algorithm without changing its structure.

---

## Core Idea

The Template Method pattern is based on the idea that while parts of an algorithm may vary, the overarching structure should remain the same. The pattern encourages code reuse and enforces a consistent workflow by having the common parts of the logic in a base class and delegating the variable parts to subclasses.

---

## Real-World Use Cases

* **Online Forms**: You may have different forms (registration, contact, feedback), but they all follow a general flow (validate, process, save).
* **Cooking Recipes**: The steps are generally the same (prepare ingredients, cook, serve), but the implementation differs.
* **Document Generation**: Every report may follow a similar format (header, content, footer), but the content generation varies.
* **Game Development**: Game loops follow a common structure: initialize, update, render.

---

## When to Use

Use the Template Method pattern when:

* You have a set of classes that share a common algorithm structure but differ in some steps.
* You want to enforce a standard procedure while allowing flexibility in specific parts.
* Code duplication occurs across subclasses.

---

## Advantages

* Promotes **code reuse** by keeping shared logic in the base class.
* Encourages **separation of concerns** by letting subclasses focus only on the steps they need to customize.
* Improves **maintainability** and **readability**.

---

## Disadvantages

* Increases the number of classes, which may complicate the design.
* A change in the base algorithm can affect all subclasses.
* Violates the Open/Closed Principle if changes in algorithm logic require modification of the base class.

---

## UML Structure (in text)

```
+--------------------+
| AbstractClass      |  <-- defines the template method and abstract steps
+--------------------+
| +templateMethod()  |
| +step1()           | (concrete)
| +step2()           | (abstract)
| +step3()           | (hook/optional)
+--------------------+
         /\
         ||
+----------------------+
| ConcreteClassA       |  <-- implements abstract/optional methods
+----------------------+
| +step2()             |
| +step3() (optional)  |
+----------------------+

+----------------------+
| ConcreteClassB       |
+----------------------+
| +step2()             |
+----------------------+
```

---

## Summary / Takeaway

The Template Method pattern is ideal when multiple subclasses share the same workflow but differ in specific parts. It promotes code reuse, enforces structure, and makes behavior easier to understand and modify. It’s especially useful when building frameworks or libraries where common control flows are needed.

> "The Template Method lets you define the blueprint of an algorithm and allow subclasses to fill in the blanks."

---

Next: Check out the `template_method_example.py` file for a hands-on implementation in Python!

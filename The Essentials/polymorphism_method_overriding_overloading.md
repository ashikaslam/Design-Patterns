# Polymorphism in Python: Method Overriding vs Method Overloading

Polymorphism means *many forms*. In Python, it allows objects of different classes to be treated as objects of a common superclass, especially when they share the same method name.

---

## 🔁 What is Polymorphism?

Polymorphism allows us to write code that works on the **interface**, not the implementation. This improves flexibility and reusability.

**Types of Polymorphism:**
- **Compile-Time Polymorphism (Method Overloading)**
- **Run-Time Polymorphism (Method Overriding)**

---

## 🔸 Method Overriding (Run-Time Polymorphism)

When a subclass provides a specific implementation of a method already defined in its parent class.

### ✅ Example:
```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

def make_sound(animal):
    print(animal.speak())

make_sound(Dog())  # Output: Bark
make_sound(Cat())  # Output: Meow

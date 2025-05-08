# Python does not support traditional method overloading (like in Java or C++), but you can simulate it using:

# Default arguments

# Variable arguments (*args, **kwargs)

# Type checking

# ✅ Example:


class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2))        # Output: 2
print(calc.add(2, 3))     # Output: 5
print(calc.add(2, 3, 4))  # Output: 9


#  ro 


class Printer:
    def print_data(self, *args):
        for item in args:
            print(item)

p = Printer()
p.print_data("Hello")         # Output: Hello
p.print_data("A", "B", "C")   # Output: A B C



# | Feature        | Method Overriding              | Method Overloading (Simulated)     |
# | -------------- | ------------------------------ | ---------------------------------- |
# | Definition     | Subclass changes parent method | Same method name, different params |
# | Type           | Run-time polymorphism          | Compile-time (simulated)           |
# | Python Support | ✅ Native                       | ❌ Not native, simulated with args  |
# | Use case       | Custom behavior in subclasses  | Flexible method parameters         |


# 🔚 Final Thoughts
# Polymorphism is a powerful concept that allows one interface to be used for a general class of actions. Whether you override or simulate overloads, your code becomes more flexible and maintainable.

# "Different objects, same interface, different behaviors — that's polymorphism!"
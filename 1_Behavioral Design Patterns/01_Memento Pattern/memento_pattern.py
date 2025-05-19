"""
Memento Design Pattern in Python

This script demonstrates the Memento pattern with proper classes:
- Originator: TextEditor
- Memento: Memento
- Caretaker: History
"""

# Memento class
class Memento:
    """
    Stores the internal state of the Originator (TextEditor).
    Immutable from the outside.
    """
    def __init__(self, text):
        self._text = text

    def get_saved_state(self):
        return self._text


# Originator class
class TextEditor:
    """
    The object whose state we want to save and restore.
    """
    def __init__(self):
        self._text = ""

    def write(self, new_text):
        """Appends new text to the editor."""
        self._text += new_text

    def save(self):
        """Returns a Memento containing the current state."""
        return Memento(self._text)

    def restore(self, memento):
        """Restores the editor's state from a Memento."""
        self._text = memento.get_saved_state()

    def show(self):
        """Prints the current text."""
        print(self._text)


# Caretaker class
class History:
    """
    Stores and manages Memento objects.
    Responsible for undo operations.
    """
    def __init__(self):
        self._history = []

    def save_state(self, memento):
        self._history.append(memento)

    def undo(self):
        if not self._history:
            return None
        return self._history.pop()


# Example usage
if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    editor.write("Hello")
    history.save_state(editor.save())  # Save state

    editor.write(", World!")
    editor.show()  # Output: Hello, World!

    editor.restore(history.undo())  # Undo to previous state
    editor.show()  # Output: Hello

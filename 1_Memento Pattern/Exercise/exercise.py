# document_editor.py

class Document:
    """
    The Originator class that holds the actual state (content, font name, font size).
    It can create a memento (snapshot) of its current state and restore it later.
    """
    def __init__(self):
        self.content = ""
        self.font_name = ""
        self.font_size = 0

    def create_memento(self):
        """
        Creates a snapshot of the current state.
        """
        return DocumentMemento(self.content, self.font_name, self.font_size)

    def restore(self, memento):
        """
        Restores the state from the given memento.
        """
        self.content = memento.content
        self.font_name = memento.font_name
        self.font_size = memento.font_size

    def __str__(self):
        return f"Document(content='{self.content}', font='{self.font_name}', size={self.font_size})"


class DocumentMemento:
    """
    The Memento class that holds a snapshot of the Document state.
    This class should not be modified externally.
    """
    def __init__(self, content, font_name, font_size):
        self.content = content
        self.font_name = font_name
        self.font_size = font_size


class History:
    """
    The Caretaker class that stores the history of mementos.
    It allows undo operations by popping the last saved state.
    """
    def __init__(self):
        self._mementos = []

    def push(self, memento):
        self._mementos.append(memento)

    def pop(self):
        if self._mementos:
            return self._mementos.pop()
        return None


# Usage example
if __name__ == "__main__":
    doc = Document()
    history = History()

    doc.content = "Hello"
    doc.font_name = "Arial"
    doc.font_size = 12
    history.push(doc.create_memento())  # Save state

    doc.content = "Hello, World!"
    doc.font_size = 14
    history.push(doc.create_memento())  # Save new state

    doc.content = "Hi!"
    print("Current State:", doc)

    # Undo
    doc.restore(history.pop())
    print("After Undo 1:", doc)

    doc.restore(history.pop())
    print("After Undo 2:", doc)

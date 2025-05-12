

class Document:
    def __init__(self):
        self.content = ""
        self.font_name = ""
        self.font_size = 0

    def create_memento(self):
        return DocumentMemento(self.content, self.font_name, self.font_size)

    def restore(self, memento):
        self.content = memento.content
        self.font_name = memento.font_name
        self.font_size = memento.font_size

    def __str__(self):
        return f"Document(content='{self.content}', font='{self.font_name}', size={self.font_size})"


class DocumentMemento:
    def __init__(self, content, font_name, font_size):
        self.content = content
        self.font_name = font_name
        self.font_size = font_size


class History:
    def __init__(self):
        self._mementos = []

    def push(self, memento):
        self._mementos.append(memento)

    def pop(self):
        if self._mementos:
            return self._mementos.pop()
        return None



doc = Document()
history = History()

doc.content = "Hello"
doc.font_name = "aslam"
doc.font_size = 12
history.push(doc.create_memento())  

doc.content = "Hello, World!"
doc.font_size = 14
history.push(doc.create_memento())  

doc.content = "Hi!"
print("Current State:", doc)


doc.restore(history.pop())
print("After Undo 1:", doc)

doc.restore(history.pop())
print("After Undo 2:", doc)

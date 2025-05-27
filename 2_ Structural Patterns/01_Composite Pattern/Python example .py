"""
Composite Design Pattern - Python Example

Scenario: File System Hierarchy
We simulate a file system with files and directories.
Both files and directories support a common method: display().
Directories can contain other files or directories.
"""

from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    """
    Abstract Component:
    Declares the interface for all concrete components.
    Both File and Directory will implement this.
    """
    @abstractmethod
    def display(self, indent=0):
        pass

class File(FileSystemComponent):
    """
    Leaf Component:
    Represents files in the file system. Has no children.
    """
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print('  ' * indent + f"File: {self.name}")

class Directory(FileSystemComponent):
    """
    Composite Component:
    Represents directories which can contain other files or directories.
    """
    def __init__(self, name):
        self.name = name
        self.children = []  # list of FileSystemComponent

    def add(self, component):
        """Add a file or directory to this directory."""
        self.children.append(component)

    def remove(self, component):
        """Remove a file or directory from this directory."""
        self.children.remove(component)

    def display(self, indent=0):
        print('  ' * indent + f"Directory: {self.name}")
        for child in self.children:
            child.display(indent + 1)

# Example Usage
if __name__ == "__main__":
    """
    Creating a file system structure:
    root/
        file1.txt
        file2.txt
        subdir1/
            file3.txt
            file4.txt
    """
    root = Directory("root")
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    subdir1 = Directory("subdir1")
    file3 = File("file3.txt")
    file4 = File("file4.txt")

    subdir1.add(file3)
    subdir1.add(file4)
    root.add(file1)
    root.add(file2)
    root.add(subdir1)

    # Display the entire structure
    root.display()

    """
    Output:
    Directory: root
      File: file1.txt
      File: file2.txt
      Directory: subdir1
        File: file3.txt
        File: file4.txt
    """

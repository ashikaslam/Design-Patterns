"""
flyweight_pattern_example.py

This script demonstrates the Flyweight Design Pattern using a character formatting
system similar to a text editor. Instead of creating separate objects for each
character with the same style, it shares style objects across multiple characters.

This helps reduce memory usage and improves performance, especially when
dealing with large documents.
"""

# --- Flyweight (Shared) Class ---
class CharacterStyle:
    """
    The Flyweight class that contains the intrinsic (shared) state,
    such as font family, size, and weight.
    """
    def __init__(self, font_family: str, font_size: int, bold: bool = False, italic: bool = False):
        self.font_family = font_family
        self.font_size = font_size
        self.bold = bold
        self.italic = italic

    def render(self, character: str, line: int, column: int):
        """
        Simulates rendering a character with the current style
        (the extrinsic state: character, position).
        """
        style = f"{self.font_family}, {self.font_size}px"
        if self.bold:
            style += ", bold"
        if self.italic:
            style += ", italic"
        print(f"Rendering '{character}' at ({line}, {column}) with style [{style}]")


# --- Flyweight Factory ---
class StyleFactory:
    """
    Factory that creates and manages shared CharacterStyle instances.
    Ensures that styles with the same properties are reused.
    """
    _styles = {}

    @classmethod
    def get_style(cls, font_family, font_size, bold=False, italic=False):
        """
        Returns a shared CharacterStyle object based on its properties.
        If it already exists, reuse it; otherwise, create and store a new one.
        """
        key = (font_family, font_size, bold, italic)
        if key not in cls._styles:
            cls._styles[key] = CharacterStyle(font_family, font_size, bold, italic)
        return cls._styles[key]


# --- Context Class ---
class Character:
    """
    The context that uses a Flyweight (CharacterStyle) and adds extrinsic state:
    the actual character and its position.
    """
    def __init__(self, char: str, line: int, column: int, style: CharacterStyle):
        self.char = char
        self.line = line
        self.column = column
        self.style = style

    def render(self):
        """
        Render the character using the shared style object.
        """
        self.style.render(self.char, self.line, self.column)


# --- Client Code ---
if __name__ == "__main__":
    # Create a style factory
    factory = StyleFactory()

    # Shared style
    style_normal = factory.get_style("Arial", 12)
    style_bold = factory.get_style("Arial", 12, bold=True)

    # Create characters with shared styles
    document = [
        Character("H", 0, 0, style_bold),
        Character("e", 0, 1, style_normal),
        Character("l", 0, 2, style_normal),
        Character("l", 0, 3, style_normal),
        Character("o", 0, 4, style_normal),
        Character("!", 0, 5, style_bold),
    ]

     
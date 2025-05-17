from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        if not isinstance(text_type, TextType):
            raise TypeError("text_type must be enum")
        if (text_type == TextType.LINK) or (text_type == TextType.IMAGE):
            if url is None:
                raise TypeError("link or image requires url")

        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url)

    def __repr__(self):
        return(f"TextNode({self.text}, {self.text_type}, {self.url})")

import textwrap

class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""

        return " " + " ".join([f'{key}="{value}"' for key, value in self.props.items()])

    def __repr__(self):
        str = text.wrap.dedent(f"""
              HTMLNode(
                {tag=},
                {value=},
                {children=},
                {props=}
              )""")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, props = props) 

    def to_html(self):
        if not self.value:
            raise ValueError("leaf node must have value")
        elif not self.tag:
            return self.value 
        else:
            open_tag = f"<{self.tag}{self.props_to_html()}>"
            close_tag = f"</{self.tag}>"
            return open_tag + self.value + close_tag

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, children = children, props = props)

    def to_html(self):
        if not self.tag:
            raise ValueError("parent node needs tag")
        elif not self.children:
            raise ValueError("parent node needs children")
        else:
            open_tag = f"<{self.tag}{self.props_to_html()}>" 
            close_tag = f"</{self.tag}>"
            children_html = [child.to_html() for child in self.children]
            return open_tag + "".join(children_html) + close_tag 



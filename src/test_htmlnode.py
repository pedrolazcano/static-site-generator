import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_default_none(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_props_to_html(self):
        props_dict = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        props_html = ' href="https://www.google.com" target="_blank"'
        node = HTMLNode(props = props_dict)  

        self.assertEqual(node.props_to_html(), props_html)

    def test_to_html(self):
        with self.assertRaises(NotImplementedError):
            node = HTMLNode()
            node.to_html()

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        text = "Unencumbered text!"
        node = LeafNode(None, text)
        self.assertEqual(node.to_html(), text)

    def test_leaf_to_html_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode(None, None)
            node.to_html()

    def test_parent_to_html_w_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_parent_to_html_w_grandchild(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_to_html_w_two_children(self):
        child1 = LeafNode("b", "child1")
        child2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>child1</b><span>child2</span></div>",
        )

    def test_parent_to_html_wo_child(self):
        with self.assertRaises(ValueError):
            node = ParentNode("div", [])
            node.to_html()
        
if __name__ == "__main__":
    unittest.main()

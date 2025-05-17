import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_property(self):
        node1 = TextNode('a', TextType.BOLD)
        node2 = TextNode('a', TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_invalid_enum(self):
        with self.assertRaises(TypeError):
            node = TextNode("uepa", "uepa")

    def test_url(self):
        url = "http://boot.dev"
        node = TextNode("uepa", TextType.LINK, url)
        self.assertEqual(node.url, url)

    def test_link_requires_url(self):
        with self.assertRaises(TypeError):
            node = TextNode("uepa", TextType.LINK)



if __name__ == "__main__":
    unittest.main()

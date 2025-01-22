import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(
            '<p>This is a paragraph of text.</p>', node.to_html()
        )
    
    def test_eq2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            '<a href="https://www.google.com">Click me!</a>', node.to_html()
        )

    def test_repr(self):
        node = LeafNode("p", "This is a paragraph of text.", "")
        self.assertEqual(
            "LeafNode(\"p\", \"This is a paragraph of text.\", \"\")", repr(node)
        )
if __name__ == "__main__":
    unittest.main()
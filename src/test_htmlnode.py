import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<a>","click me!","",{"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"', node.props_to_html()
        )
    
    def test_eq2(self):
        node = HTMLNode("<a>","click me!","")
        self.assertEqual(
            '', node.props_to_html()
        )

    def test_repr(self):
        node = HTMLNode("<a>","click me!","",{"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(
            "HTMLNode(<a>, click me!, , {'href': 'https://www.google.com', 'target': '_blank'})", repr(node)
        )
    
    def test_repr2(self):
        node = HTMLNode("","","",{"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(
            "HTMLNode(, , , {'href': 'https://www.google.com', 'target': '_blank'})", repr(node)
        )

if __name__ == "__main__":
    unittest.main()
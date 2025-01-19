import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq_leafs(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>', node.to_html()
        )

    def test_eq_sub_parents(self):
        node = ParentNode(
            "sections",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            '<sections><b>Bold text</b>Normal text<p><b>Bold text</b>Normal text</p>Normal text</sections>', node.to_html()
        )

    def test_none(self):
        node = ParentNode(
            "p",
            LeafNode("b", "Bold text"),
        )

        self.assertEqual(
            '<p><b>Bold text</b></p>', node.to_html()
        )

if __name__ == "__main__":
    unittest.main()
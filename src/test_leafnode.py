import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        html = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), html)

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        html = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), html)

if __name__ == "__main__":
    unittest.main()
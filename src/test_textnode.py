import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode('this is a text node', 'bold', 'www.google.com')
        node2 = TextNode('this is a text node', 'bold', 'www.google.com')
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = TextNode('this is a text node', 'bold', 'www.google.com')
        node2 = TextNode('this is a text node', 'bold', 'www.facebook.com')
        self.assertNotEqual(node1, node2)

    def test_not_eq_url_none(self):
        node1 = TextNode('this is a text node', 'bold')
        node2 = TextNode('this is a text node', 'italic')
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
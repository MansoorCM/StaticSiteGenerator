import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        htmlnode = HTMLNode(props = { 'href':'https://www.google.com', 'target':'_blank' } )
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(htmlnode.props_to_html(), expected)

if __name__ == "__main__":
    unittest.main()
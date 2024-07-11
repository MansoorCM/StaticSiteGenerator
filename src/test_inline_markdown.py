import unittest
from textnode import (
    TextNode,
    text_type_text,
    text_type_code
    )
from inlinemarkdown import split_nodes_delimiter

class TestInlineMarkdown(unittest.TestCase):
    def test_inline_markdown_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        expected = [
                    TextNode("This is text with a ", text_type_text),
                    TextNode("code block", text_type_code),
                    TextNode(" word", text_type_text),
                ]
        self.assertEqual(expected, new_nodes)

if __name__ == "__main__":
    unittest.main()
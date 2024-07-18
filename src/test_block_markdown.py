import unittest
from blockmarkdown import (
    markdown_to_block,
    block_to_block_type,
    block_type_paragraph,
    block_type_code,
    block_type_heading,
    block_type_ordered_list,
    block_type_unordered_list,
    block_type_quote,
    )

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_block(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        expected = [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ]
        self.assertEqual(expected, markdown_to_block(md))

    def test_block_to_block_type_paragraph(self):
        block = "This is **bolded** paragraph"
        self.assertEqual(block_type_paragraph, block_to_block_type(block))
    
    def test_block_to_block_type_code(self):
        block = "```This is a code block```"
        self.assertEqual(block_type_code, block_to_block_type(block))

    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_type_heading, block_to_block_type(block))

    def test_block_to_block_type_quote(self):
        block = ">this is quote 1\n>this is quote 2\n>this is quote 3"
        self.assertEqual(block_type_quote, block_to_block_type(block))

    def test_block_to_block_type_unorderedlist(self):
        block = "* this is item 1\n* this is item 2\n* this is item 3"
        self.assertEqual(block_type_unordered_list, block_to_block_type(block))

    def test_block_to_block_type_orderedlist(self):
        block = "1. this is item 1\n2. this is item 2\n3. this is item 3"
        self.assertEqual(block_type_ordered_list, block_to_block_type(block))

if __name__== "__main__":
    unittest.main()
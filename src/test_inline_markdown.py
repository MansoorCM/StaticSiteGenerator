import unittest
from textnode import (
    TextNode,
    text_type_text,
    text_type_code
    )
from inlinemarkdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links
)

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

    def test_inline_markdown_extract_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        alt_links = extract_markdown_images(text)
        self.assertEqual(expected, alt_links)
    
    def test_inline_markdown_extract_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        anchor_links = extract_markdown_links(text)
        self.assertEqual(expected, anchor_links)

if __name__ == "__main__":
    unittest.main()
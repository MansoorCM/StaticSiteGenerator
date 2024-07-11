import unittest
from textnode import (
    TextNode,
    text_type_text,
    text_type_code,
    text_type_image,
    text_type_link,
    text_type_bold,
    text_type_italic
    )
from inlinemarkdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
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

    def test_inline_markdown_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
            )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode(
                "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
            ),
            ]
        self.assertEqual(expected, new_nodes)

    def test_inline_markdown_split_nodes_image(self):
        node = TextNode(
                "This is text with a link ![to boot dev](https://www.boot.dev/img/bootdev-logo-full-small.webp) " + 
                "and ![to youtube](https://t3.ftcdn.net/jpg/04/74/05/94/360_F_474059464_qldYuzxaUWEwNTtYBJ44VN89ARuFktHW.jpg)",
                text_type_text,
                )
        new_nodes = split_nodes_image([node])
        expected = [
                TextNode("This is text with a link ", text_type_text),
                TextNode("to boot dev", text_type_image, "https://www.boot.dev/img/bootdev-logo-full-small.webp"),
                TextNode(" and ", text_type_text),
                TextNode(
                        "to youtube", text_type_image, "https://t3.ftcdn.net/jpg/04/74/05/94/360_F_474059464_qldYuzxaUWEwNTtYBJ44VN89ARuFktHW.jpg"
                    ),
                ]
        self.assertEqual(expected, new_nodes)

    def test_text_to_textnode(self):
        text = ('This is **text** with an *italic* word and a `code block` and an ' + 
            '![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) ' + 
            'and a [link](https://boot.dev)'
            )
        nodes = text_to_textnodes(text)
        expected = [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ]
        self.assertEqual(expected, nodes)

if __name__ == "__main__":
    unittest.main()
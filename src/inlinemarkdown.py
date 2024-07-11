from textnode import (
    TextNode,
    text_type_text,
    text_type_code,
    text_type_bold,
    text_type_italic
    )
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == text_type_text:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0: # mismatch in num of delimiters
                raise ValueError('Invalid markdown syntax, delimiter mismatch.')
            for i, part in enumerate(parts):
                if part == '':
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, text_type_text))
                else:
                    new_nodes.append(TextNode(part, text_type))
        else:
            new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    pattern = r'!\[(.*?)\]\((.*?)\)'
    return re.findall(pattern, text)

def extract_markdown_links(text):
    pattern = r'\[(.*?)\]\((.*?)\)'
    return re.findall(pattern, text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == text_type_text:
            alt_links = extract_markdown_images(node.text)
            text = node.text
            for alt, link in alt_links:
                part, text = text.split(f"![{alt}]({link})", 1)
                if part != '':
                    new_nodes.append(TextNode(part, text_type_text))
                new_nodes.append(TextNode(alt, 'image', link))
            if text != '':
                new_nodes.append(TextNode(text, text_type_text))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == text_type_text:
            anchor_links = extract_markdown_links(node.text)
            text = node.text
            for anchor, link in anchor_links:
                part, text = text.split(f"[{anchor}]({link})", 1)
                if part != '':
                    new_nodes.append(TextNode(part, text_type_text))
                new_nodes.append(TextNode(anchor, 'link', link))
            if text != '':
                new_nodes.append(TextNode(text, text_type_text))
        else:
            new_nodes.append(node)
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    new_nodes = split_nodes_delimiter(nodes, '`', text_type_code)
    new_nodes = split_nodes_delimiter(new_nodes, '**', text_type_bold)
    new_nodes = split_nodes_delimiter(new_nodes, '*', text_type_italic)
    new_nodes = split_nodes_image(new_nodes)
    return split_nodes_link(new_nodes)
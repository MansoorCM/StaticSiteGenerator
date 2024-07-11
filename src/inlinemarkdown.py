from textnode import (
    TextNode,
    text_type_text,
    )

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
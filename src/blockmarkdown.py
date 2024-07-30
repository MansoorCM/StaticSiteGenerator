from leafnode import LeafNode
from parentnode import ParentNode

block_type_paragraph = 'paragraph'
block_type_heading = 'heading'
block_type_code = 'code'
block_type_quote = 'quote'
block_type_unordered_list = 'unordered_list'
block_type_ordered_list = 'ordered_list'

def markdown_to_block(string):
    filtered_blocks = []
    for line in string.split("\n\n"):
        modified = line.strip()
        if modified == "":
            continue
        filtered_blocks.append(modified)
    return filtered_blocks

def block_to_block_type(block):
    if (block.startswith('# ') or 
        block.startswith('## ') or 
        block.startswith('### ') or 
        block.startswith('#### ') or 
        block.startswith('##### ') or 
        block.startswith('###### ')):
        return block_type_heading
    lines = block.split('\n')
    if lines[0].startswith('```') and lines[-1].endswith('```'):
        return block_type_code
    if lines[0].startswith('>'):
        return is_block_of_given_type(lines, '>', block_type_quote)
    if lines[0].startswith('*'):
        return is_block_of_given_type(lines, '* ', block_type_unordered_list)
    if lines[0].startswith('-'):
        return is_block_of_given_type(lines, '- ', block_type_unordered_list)
    if is_block_of_type_orderedlist(lines):
        return block_type_ordered_list
    return block_type_paragraph

def is_block_of_given_type(lines, pattern, block_type):
    for i in range(len(lines)):
        if not lines[i].startswith(pattern):
            return block_type_paragraph
    return block_type

def is_block_of_type_orderedlist(lines):
    for i in range(len(lines)):
        if not (lines[i].startswith(f"{i + 1}. ")):
            return False
    return True

def markdown_to_htmlnode(string):
    blocks = markdown_to_block(string)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_paragraph:
            children.append(LeafNode('p', block))
        elif block_type == block_type_heading:
            children.append(block_heading_to_html(block))
        elif block_type == block_type_code:
            children.append(block_code_to_html(block))
        elif block_type == block_type_quote:
            children.append(block_quote_to_html(block))
        elif block_type == block_type_unordered_list:
            children.append(block_list_to_html(block, 'ul'))
        elif block_type == block_type_ordered_list:
            children.append(block_list_to_html(block, 'ol'))
        else:
            raise ValueError("invalid block type")
    return ParentNode('div', children)

def block_heading_to_html(block):
    idx = block.find(' ')
    return LeafNode(f"h{idx}", block[idx + 1:])

def block_code_to_html(block):
    html_code_node = LeafNode('code', block[3:-3])
    return ParentNode('pre', [html_code_node])

def block_quote_to_html(block):
    filtered = []
    for line in block.split('\n'):
        filtered.append(line[1:])
    block = '\n'.join(filtered)
    return LeafNode('blockquote', block)

def block_list_to_html(block, tag):
    children = []
    for line in block.split('\n'):
        idx = line.find(' ')
        children.append(LeafNode('li', line[idx + 1:]))
    return ParentNode(tag, children)
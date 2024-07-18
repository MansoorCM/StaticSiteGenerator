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
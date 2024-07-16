def markdown_to_block(string):
    filtered_blocks = []
    for line in string.split("\n\n"):
        modified = line.strip()
        if modified == "":
            continue
        filtered_blocks.append(modified)
    return filtered_blocks
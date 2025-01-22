# def markdown_to_blocks(markdown):
#     blocks = []
#     blocks = markdown.split("\n\n")
#     blocks = list(map(lambda x: x.strip(), blocks))
#     return blocks

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

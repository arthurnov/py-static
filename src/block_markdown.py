import re
# def markdown_to_blocks(markdown):
#     blocks = []
#     blocks = markdown.split("\n\n")
#     blocks = list(map(lambda x: x.strip(), blocks))
#     return blocks

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    lines = block.split("\n")
    ul = True
    ol = True
    if re.findall(r"^#{1,6} ", block) != []:
        return block_type_heading
    if re.findall(r"^`{3}\n", block) != [] and re.findall(r"\n`{3}$", block) != []:
        return block_type_code
    if re.findall(r"^[^>]", block) == [] and re.findall(r"\n[^>]", block) == []:
        return block_type_quote
    for line in lines:
        if re.findall(r"^\* ", line) == [] and re.findall(r"^- ", line) == []:
            ul = False
    if ul == True:
        return block_type_ulist
    for i in range(len(lines)):
        regex = r"^" + str(i+1) + ". "
        if re.findall(regex, lines[i]) == []:
            ol = False
    if ol == True:
        return block_type_olist
    return block_type_paragraph

# paragraph
# heading
# code
# quote
# unordered_list
# ordered_list
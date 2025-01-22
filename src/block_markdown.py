import re
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

def block_to_block_type(block):
    lines = block.split("\n")
    print(lines)
    if re.findall(r"^#{1,6} ", block) != []:
        return "heading"
    if re.findall(r"^`{3}\n", block) != [] and re.findall(r"\n`{3}$", block) != []:
        return "code"
    if re.findall(r"^[^>]", block) == [] and re.findall(r"\n[^>]", block) == []:
        return "quote"
    if (re.findall(r"^[^(\* )]", block) == [] and re.findall(r"\n[^(\* )]", block) == []) or (re.findall(r"^[^(- )]", block) == [] and re.findall(r"\n[^(- )]", block) == []):
        return "unordered_list"
    return "paragraph"


text = '''* ijfeijf
* jiejfirfj
 ijirj
'''
print(block_to_block_type(text))

# paragraph
# heading
# code
# quote
# unordered_list
# ordered_list
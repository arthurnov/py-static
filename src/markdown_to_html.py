from block_markdown import markdown_to_blocks, block_to_block_type
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
from parentnode import ParentNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        type = block_to_block_type(block)
        if type == "paragraph":
            text_nodes = text_to_textnodes(block)
            for node in text_nodes:
                nodes.append(text_node_to_html_node(node))
        if type == " heading":
            
        # print(f"BLOCK: \"{block}\"\nTYPE: {type}")
        # tnodes = text_to_textnodes(block)
        # print(f"TNODES: {tnodes}")
        # hnodes = []
        # for node in tnodes:
        #     hnodes.append(text_node_to_html_node(node))
        # nodes.extend(hnodes)
    div_node = ParentNode("div",nodes)
    print(div_node.to_html())
    return div_node
####

# block_type_paragraph = "paragraph"
# block_type_heading = "heading"
# block_type_code = "code"
# block_type_quote = "quote"
# block_type_olist = "ordered_list"
# block_type_ulist = "unordered_list"

markdown = '''
# this is my header

## sub header here

this is a fake **markdown** file.
you know what *markdown* is, right?

* its great
* its easy

also, visit [boot.dev](https://www.boot.dev)
'''

print(markdown_to_html_node(markdown))
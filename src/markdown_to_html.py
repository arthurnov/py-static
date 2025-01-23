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
            
        # print(f"BLOCK: \"{block}\"\nTYPE: {type}")
        # tnodes = text_to_textnodes(block)
        # print(f"TNODES: {tnodes}")
        # hnodes = []
        # for node in tnodes:
        #     hnodes.append(text_node_to_html_node(node))
        # nodes.extend(hnodes)
    html = ParentNode("div",nodes)
    print(html.to_html())
    return html
####

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
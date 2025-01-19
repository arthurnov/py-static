from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    print(f"INPUT NODES: {old_nodes}")
    for node in old_nodes:
        sentance = ""
        print(f"NODE: {node}")
        
    new_nodes.append(old_nodes[0].text.split(delimiter, maxsplit=1))
    return new_nodes

node = TextNode("This is text with a `code block` word", TextType.NORMAL)
node2 = TextNode("This is another text with a `code block` word, maybe even `two code blocks`", TextType.NORMAL)
new_nodes = split_nodes_delimiter([node, node2], "`", TextType.CODE)
print(new_nodes)
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    print(f"INPUT NODES: {old_nodes}")
    for node in old_nodes:
        print(f"NODE: {node}")
        index = node.text.find(delimiter)
        print(f"JUST TAGGED: {index}")
        new_nodes.append(node.text.split(delimiter))
        
    return new_nodes

def rec(text, deli):
    if text.count(deli) < 2:
        retur

node = TextNode("This is text with a `code block` word", TextType.NORMAL)
node2 = TextNode("This is another text with a `code block` word, maybe even `two code blocks`", TextType.NORMAL)
node3 = TextNode("And this is text with a **bold** word", TextType.NORMAL)
new_nodes = split_nodes_delimiter([node, node2], "`", TextType.CODE)
new_nodes.extend(split_nodes_delimiter([node3], "**", TextType.BOLD))
print(new_nodes)
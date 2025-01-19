from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    print(f"INPUT NODES: {old_nodes}")
    for node in old_nodes:
        print(f"NODE: {node}")
        new_nodes.append(node_worker(node.text, delimiter, text_type))
        # new_nodes.append(node.text.split(delimiter))
    return new_nodes

def node_worker(node, deli, text_type):
    splitted = node.split(deli)
    splitted_obj = list(map(lambda x: sub_worker(x, text_type), enumerate(splitted)))
    return splitted_obj

def sub_worker(x, text_type):
    i, txt = x
    if txt == "":
        pass
    if i%2 == 0:
        return TextNode(txt, TextType.NORMAL)
    return TextNode(txt, text_type)

    
# node = TextNode("This is text with a `code block` word", TextType.NORMAL)
# node2 = TextNode("This is another text with a `code block` word, maybe even `two code blocks`", TextType.NORMAL)
node3 = TextNode("And this is text with a **bold** word", TextType.NORMAL)
node4 = TextNode("**And****this** is text with a bold word", TextType.NORMAL)
new_nodes = split_nodes_delimiter([node3, node4], "**", TextType.BOLD)

print(new_nodes)

# ['', 'And', ' this is text with a bold ', 'word', '']
# ['', 'And', ' this is text with a ', 'bold', ' word']
# ['', 'And', ' ', 'this', ' is text with a bold word']
# ['', 'And', '', 'this', ' is text with a bold word']
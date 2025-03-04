from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.NORMAL))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.NORMAL))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.NORMAL))
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

# OG approach, switched to one provided by boot.dev
# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     new_nodes = []
#     print(f"INPUT NODES: {old_nodes}")
#     for node in old_nodes:
#         print(f"NODE: {node}")
#         new_nodes.append(node_worker(node.text, delimiter, text_type))
#         # new_nodes.append(node.text.split(delimiter))
#     return new_nodes

# def node_worker(node, deli, text_type):
#     splitted = node.split(deli)
#     splitted_obj = list(map(lambda x: sub_worker(x, text_type), enumerate(splitted)))
#     return splitted_obj

# def sub_worker(x, text_type):
#     i, txt = x
#     if txt == "":
#         pass
#     if i%2 == 0:
#         return TextNode(txt, TextType.NORMAL)
#     return TextNode(txt, text_type)

    
# node = TextNode("This is text with a `code block` word", TextType.NORMAL)
# node2 = TextNode("This is another text with a `code block` word, maybe even `two code blocks`", TextType.NORMAL)
# node3 = TextNode("And this is text with a **bold** word", TextType.NORMAL)
# node4 = TextNode("**And****this** is text with a bold word", TextType.NORMAL)
# new_nodes = split_nodes_delimiter([node3, node4], "**", TextType.BOLD)

# print(new_nodes)

# ['', 'And', ' this is text with a bold ', 'word', '']
# ['', 'And', ' this is text with a ', 'bold', ' word']
# ['', 'And', ' ', 'this', ' is text with a bold word']
# ['', 'And', '', 'this', ' is text with a bold word']

# [
#     TextNode("This is ", TextType.NORMAL), 
#     TextNode("text", TextType.BOLD), 
#     TextNode(" with an ", TextType.NORMAL), 
#     TextNode("italic", TextType.ITALIC), 
#     TextNode(" word and a ", TextType.NORMAL), 
#     TextNode("code block", TextType.CODE), 
#     TextNode(" and an ", TextType.NORMAL), 
#     TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), 
#     TextNode(" and a ", TextType.NORMAL), 
#     TextNode("link", TextType.LINK, "https://boot.dev")
# ]
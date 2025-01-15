from textnode import TextNode

def main():
    node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    node3 = TextNode("This is a text node!", "bold", "https://www.boot.dev")

    print(f"node1: {node1}\nnode1 == node2: {node1==node2}\nnode1 == node3: {node1==node3}")

if __name__ == "__main__":
    main()

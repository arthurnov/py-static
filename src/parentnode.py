from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Missing tag")
        if self.children == None or not self.children:
            raise ValueError("Missing children")
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
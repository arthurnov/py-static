from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Missing tag")
        if self.children == None or not self.children:
            raise ValueError("Missing children")
        if not isinstance(self.children, list):
            return f"<{self.tag}{self.props_to_html()}>{self.children.to_html()}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{''.join(list(map(lambda x: x.to_html(), self.children)))}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode(\"{self.tag}\", children: {self.children}, \"{self.props}\")"
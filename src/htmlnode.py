class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    # replaced with lambda inside props_to_html()
    # def helper(self, item):
    #     return f" {item[0]}=\"{item[1]}\""
    
    def props_to_html(self):
        # replaced "helper()" func with lambda
        if not self.props:
            return ""
        props = list(map(lambda item: f" {item[0]}=\"{item[1]}\"", self.props.items()))
        props = "".join(props)
        return props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

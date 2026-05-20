# Base class for game objects
class HtmlNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        htmlString =""
        if self.props is None:
            return ""
        for key, value in self.props.items():
            htmlString += " "+ key +'="' + value+'"'
        return htmlString
    
    def __repr__(self):
        return (f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})")
    
class LeafNode(HtmlNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag,value, None, props)

    def to_html(self):
        leafString =""
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        else:
            leafString +="<"+self.tag

            if self.props is not None:
                for key, value in self.props.items():
                    leafString += " "+ key +'="' + value+ '"'

            leafString += '>'+self.value + "</"+self.tag+">"
        return leafString

    def __repr__(self):
        return (f"LeafNode({self.tag}, {self.value}, {self.props})")


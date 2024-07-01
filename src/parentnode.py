from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError('tag should not be empty.')
        if not self.children:
            return ValueError('parent node should have child nodes.')
        html = []
        html.append(f'<{self.tag}{self.props_to_html()}>')

        for child in self.children:
            html.append(child.to_html())

        html.append(f'</{self.tag}>')

        return ''.join(html)
    
    def __repr__(self):
        return f'ParentNode({self.tag}, {self.children}, {self.props})'
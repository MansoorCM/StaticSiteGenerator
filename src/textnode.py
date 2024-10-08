from leafnode import LeafNode

text_type_text = 'text'
text_type_bold = 'bold'
text_type_italic = 'italic'
text_type_code = 'code'
text_type_link = 'link'
text_type_image = 'image'

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def textnode_to_htmlnode(textnode):
    if textnode.text_type == 'text':
        return LeafNode(None, textnode.text)
    if textnode.text_type == 'bold':
        return LeafNode('b', textnode.text)
    if textnode.text_type == 'italic':
        return LeafNode('i', textnode.text)
    if textnode.text_type == 'code':
        return LeafNode('code', textnode.text)
    if textnode.text_type == 'link':
        return LeafNode('a', textnode.text, {'href':textnode.url})
    if textnode.text_type == 'image':
        return LeafNode('img', '', {'src':textnode.url, 'alt':textnode.text})
    raise Exception('invalid text type')
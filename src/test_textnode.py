import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a textrt node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD,"www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.hpe.com")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_Bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_IMAGE(self):
        node = TextNode("Akiko", TextType.IMAGE, "www.boobies.com/asian.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":"www.boobies.com/asian.jpg","alt":"Akiko"})
    
    def test_URL(self):
        node = TextNode("Oh La la!!!", TextType.LINK, "https://www.xhamster.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Oh La la!!!")
        self.assertNotEqual(html_node.props, {'href':"https://www.pornhub.com"})
if __name__ == "__main__":
    unittest.main()
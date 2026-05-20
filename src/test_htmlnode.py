import unittest
from htmlnode import HtmlNode, LeafNode

class HtmlTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HtmlNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_error_html(self):
        node = HtmlNode(props={"href": "https://www.google.com"})
        self.assertNotEqual(node.props_to_html(), ' href="https://www.pornhub.com"')

    def test_no_props_to_html(self):
        node = HtmlNode(props=None)
        self.assertEqual(node.props_to_html(), '')
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_props(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, world!</a>')

    def test_leaf_broken(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
        self.assertNotEqual(node.to_html(), '<a href="https://www.xhamster.com">Oh La La!!!!</a>')

if __name__ == "__main__":
    unittest.main()
import unittest
from htmlnode import HtmlNode

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

if __name__ == "__main__":
    unittest.main()
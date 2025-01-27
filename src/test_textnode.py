import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
        
    def test_text_type(self):
        t_node = TextNode("This is a text node", TextType.BOLD_TEXT)
        t_node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(t_node.text_type, t_node2.text_type)
        
    def test_url_defualt(self):
        t_node = TextNode("This is a text node", TextType.BOLD_TEXT,)
        self.assertTrue(t_node.url == None)
        
    def test_url_set(self):
        url = "https://www.boot.dev"
        node = TextNode("This is a text node", TextType.BOLD_TEXT, url)
        self.assertEqual(node.url, url)


if __name__ == "__main__":
    unittest.main()

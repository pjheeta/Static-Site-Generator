from enum import Enum
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HtmlNode, ParentNode
from inline import split_nodes_delimiter
from regex import extract_markdown_images,extract_markdown_links, split_nodes_image,split_nodes_link, text_to_textnodes
# from htmlnode import props_to_html
import unittest
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def block_to_block_type(blockNode: enumerate):
    lines = blockNode.split("\n")
    isQuote = True
    isUnordered = True
    isOrdered = True

    for i, line in enumerate(lines):
        if not line.startswith(">"):
            isQuote = False
        if not line.startswith("- "):
            isUnordered = False
        if not line.startswith(f"{i+1}. "):
            isOrdered = False
                
    if re.match(r"^#{1,6} ", blockNode):
        return BlockType.HEADING
    elif re.match(r"^```[\r\n](.*?)```$", blockNode, re.DOTALL):
        return BlockType.CODE    
    elif isQuote:
        return BlockType.QUOTE
    elif isUnordered:
        return BlockType.ULIST
    elif isOrdered:
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH  

def markdown_to_blocks(markdown):
    block = []
    newText=markdown.split("\n\n")
    for temp in newText:
        if temp !="":
            temp = temp.strip()
            block.append (temp) 
    return block

def markdown_to_html_node(markdown):
    blockNode = []
    newNode = markdown_to_blocks(markdown)

    for nodes in newNode:
        childNode = text_to_children(nodes)
        blockType =block_to_block_type(nodes)
  
        if blockType == BlockType.PARAGRAPH:
            blockNode.append(ParentNode("p", childNode))
        elif blockType == BlockType.CODE:
            blockNode.append(ParentNode("pre",[ParentNode("code", childNode)]))
        elif blockType == BlockType.QUOTE:
            blockNode.append(ParentNode("blockquote", childNode))
        elif blockType == BlockType.ULIST:
            blockNode.append(ParentNode("ul", childNode))
        elif blockType == BlockType.OLIST:
            blockNode.append(ParentNode("ol", childNode))
        else:
            level = len(nodes) - len(nodes.lstrip("#"))
            blockNode.append(ParentNode(f"h{level}", childNode))            

    return ParentNode("div", blockNode)


def text_to_children(text):
    childrenNode = []
    textNode = text_to_textnodes(text)
    for singleNode in textNode:
        htmlNode = text_node_to_html_node(singleNode)
        childrenNode.append(htmlNode)

    return childrenNode


md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
markdown_to_html_node(md)
import re
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HtmlNode
from inline import split_nodes_delimiter

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return (matches)

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return (matches)



def split_nodes_image(old_nodes):
    newNode = []

    for splitnode in old_nodes:
        nodeText = splitnode.text
        if splitnode.text_type is not TextType.TEXT:
            newNode.append(splitnode)
        else:
            getLinks=extract_markdown_images(nodeText)

            for indiLink in getLinks:
                sections = nodeText.split(f"![{indiLink[0]}]({indiLink[1]})", 1)
                if sections[0] != "":
                    newNode.append(TextNode(sections[0], TextType.TEXT))
                newNode.append(TextNode(indiLink[0], TextType.IMAGE, indiLink[1]))
                nodeText = sections[1]  
            if nodeText != "":
                newNode.append(TextNode(nodeText, TextType.TEXT))    
    return newNode

def split_nodes_link(old_nodes):
    newNode = []

    for splitnode in old_nodes:
        nodeText = splitnode.text
        if splitnode.text_type is not TextType.TEXT:
            newNode.append(splitnode)
        else:
            getLinks=extract_markdown_links(nodeText)

            for indiLink in getLinks:
                sections = nodeText.split(f"[{indiLink[0]}]({indiLink[1]})", 1)
                if sections[0] != "":
                    newNode.append(TextNode(sections[0], TextType.TEXT))
                newNode.append(TextNode(indiLink[0], TextType.LINK, indiLink[1]))
                nodeText = sections[1]
            if nodeText != "":
                newNode.append(TextNode(nodeText, TextType.TEXT))
    return newNode

def text_to_textnodes(text):

    newText = TextNode(text, TextType.TEXT)
    new_Bold = split_nodes_delimiter([newText], "**", TextType.BOLD)
    newItalic = split_nodes_delimiter(new_Bold, "_", TextType.ITALIC)
    newCode = split_nodes_delimiter(newItalic, "`", TextType.CODE)    
    newImage = split_nodes_image(newCode)
    newLink = split_nodes_link(newImage)

    return (newLink)

text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
result = text_to_textnodes(text)



import re
from textnode import TextNode, TextType

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
                newNode.append(TextNode(sections[0], TextType.TEXT))
                newNode.append(TextNode(indiLink[0], TextType.IMAGE, indiLink[1]))
                nodeText = sections[1]  
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
                newNode.append(TextNode(sections[0], TextType.TEXT))
                newNode.append(TextNode(indiLink[0], TextType.LINK, indiLink[1]))
                nodeText = sections[1]  
    return newNode

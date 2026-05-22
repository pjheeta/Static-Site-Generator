from textnode import TextNode, TextType
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    newNode = []

    for parts in old_nodes:
        if parts.text_type is not TextType.TEXT:
            newNode.append(parts)
        else:
            nodes = parts.text.split (delimiter)
            if len(nodes)%2 == 0:
                raise Exception ("Matching closing delimiter not found")
            else:
                for i, newText in enumerate(nodes):
                    if i %2 == 0: 
                        newNode.append(TextNode(newText,TextType.TEXT,None))
                    else:
                        newNode.append(TextNode(newText,text_type,None))
    return newNode



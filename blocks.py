def markdown_to_blocks(markdown):
    block = []
    newText=markdown.split("\n\n")
 #   block.extend(newText)
    for temp in newText:
        if temp !="":
            temp = temp.strip()
            block.append (temp) 
    return block
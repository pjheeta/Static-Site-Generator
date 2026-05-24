from enum import Enum
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


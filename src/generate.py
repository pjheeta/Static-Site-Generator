import re
import os
import shutil
from blocks import markdown_to_html_node

def extract_title(markdown):
    markdown = markdown.splitlines()
    for temp in markdown:
        if temp.startswith("# "):
            return (re.sub(r"^#\s*", "", temp))
    raise Exception("No h1 header found") 

def generate_page(from_path, template_path, dest_path):
    print (f'Generating page from "{from_path}" to "{dest_path}" using "{template_path}"')
    markdown = open(from_path).read() 
    template = open(template_path).read() 
    newNode = markdown_to_html_node(markdown)
    markHtml=newNode.to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}",title)
    template = template.replace("{{ Content }}",markHtml)
    open(dest_path, "w").write(template)
    #print(template)





#print(extract_title(open("content/index.md").read()))
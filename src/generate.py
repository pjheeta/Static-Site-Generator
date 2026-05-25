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

def generate_page(from_path, template_path, dest_path, basepath):
    print (f'Generating page from "{from_path}" to "{dest_path}" using "{template_path}"')
    markdown = open(from_path).read() 
    template = open(template_path).read() 
    newNode = markdown_to_html_node(markdown)
    markHtml=newNode.to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}",title)
    template = template.replace("{{ Content }}",markHtml)
    ##  NEW FOR THE LAST ASSIGNMENT ##
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    open(dest_path, "w").write(template)


#def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path,basepath):    
    print (f'Generating page froms "{dir_path_content}" to "{dest_dir_path}" using "{template_path}"')
    dirContents = os.listdir(dir_path_content)
    print (dirContents)
    for item in dirContents:
        if os.path.isfile(os.path.join(dir_path_content,item)) is True:
            convertItem = item.replace(".md",".html")
            generate_page(os.path.join(dir_path_content,item),template_path,os.path.join(dest_dir_path,convertItem), basepath)
        else:
            generate_pages_recursive(os.path.join(dir_path_content,item),template_path,os.path.join(dest_dir_path,item), basepath)


